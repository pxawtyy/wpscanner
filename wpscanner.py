import requests
import json
import re
import time
import sys
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from colorama import Fore, init

init()
Dgreen = Fore.LIGHTGREEN_EX
Lgreen = Fore.LIGHTGREEN_EX
Lyellw = Fore.LIGHTYELLOW_EX
Lred = Fore.LIGHTRED_EX
Lcyan = Fore.LIGHTCYAN_EX

ua = UserAgent()
session = requests.Session()
session.headers.update({"User-Agent": ua.random})

def user_finder(new_u):
    new_url2 = f"{new_u}/wp-json/wp/v2/users"

    try:
        r2 = session.get(new_url2)
        if r2.status_code == 200:
            print(Dgreen + '\n[+] Enumerando usernames:\n')
            time.sleep(1.3)
            data = json.loads(r2.text)
            for info in data:
                print(Lgreen + f" [*] Username Encontrado: {info['slug']}")
                time.sleep(0.2)
        else:
            print(Lyellw + '\n[-] Nenhum username encontrado.')
    except Exception as e:
        print(Lred + f'\n[-] Erro ao buscar usuários: {e}')

def adminpanel_finder(org_url):
    urlA = f"{org_url}/wp-login.php?action=lostpassword&error=invalidkey"

    try:
        r3 = session.get(urlA)
        if r3.status_code == 200:
            pagesoup = BeautifulSoup(r3.text, 'lxml')
            ptag = pagesoup.find_all("p", {"id": "nav"})

            if ptag:
                for ptags in ptag:
                    for atags in ptags.find_all('a'):
                        if 'Log in' in atags.text:
                            admin_url = atags['href']
                            print(Lgreen + f'\n[+] Painel admin encontrado: {admin_url}')
                            return
            print(Lyellw + '\n[-] Painel admin não encontrado.')
        else:
            print(Lyellw + '\n[-] Painel admin não encontrado.')
    except Exception as e:
        print(Lred + f'\n[-] Erro ao buscar painel admin: {e}')

banner = """
 █ █ █ █▀█   █▀ █▀▀ ▄▀█ █▄ █ █▄ █ █▀▀ █▀█  
 ▀▄▀▄▀ █▀▀   ▄█ █▄▄ █▀█ █ ▀█ █ ▀█ ██▄ █▀▄"""
dashline = "-------------------------------------------"
author = " [+] Coded by GH0STH4CKER, optimized by pxawtyy [+] v3.1 "

print(Lgreen + banner)
print(Lgreen + dashline)
print(Lyellw + author)
print(Lgreen + dashline)

# Entrada do usuário
url = input(Dgreen + '\nDigite a URL do site (com https://): ' + Lgreen)
org_url = url

roboturl = f"{url}/robots.txt"
feedurl = f"{url}/feed"
rssurl = f"{url}/rss"
json_url = f"{url}/wp-json"

try:
    testreq = session.get(org_url)
except Exception as e:
    print(Lred + f'\n[-] Erro ao conectar ao site: {e}')
else:
    r = session.get(json_url)
    if r.status_code == 200:
        print(Dgreen + '\n[+] Status do site: ' + Lgreen + 'Online')

        robotres = session.get(roboturl).text
        feedTXT = session.get(feedurl).text
        rssTXT = session.get(rssurl).text

        if 'wp-admin' in robotres or 'wordpress.org' in feedTXT or 'wordpress.org' in rssTXT:
            print(Dgreen + '\n[+] WordPress Detectado: ' + Lgreen + 'Sim')

            try:
                feedres = session.get(feedurl)
                soup = BeautifulSoup(feedres.text, 'lxml-xml')
                wpversion = soup.find_all('generator')
                
                if wpversion:
                    wpversion = re.sub('<[^<]+>', "", str(wpversion[0])).replace('https://wordpress.org/?v=', '')
                    print(Dgreen + '\n[+] Versão do WordPress: ' + Lgreen + wpversion)
                else:
                    rnew = session.get(org_url)
                    if rnew.status_code == 200:
                        newsoup = BeautifulSoup(rnew.text, 'lxml')
                        generatorTAGS = newsoup.find_all('meta', {"name": "generator"})
                        for metatags in generatorTAGS:
                            if "WordPress" in str(metatags):
                                altwpversion = metatags['content'].replace('WordPress', '')
                                print(Dgreen + '\n[+] Versão do WordPress: ' + Lgreen + altwpversion)
                    else:
                        print(Lyellw + '[-] Versão do WordPress: Não encontrada!')
            except Exception as e:
                print(Lred + f'[-] Erro ao buscar versão do WordPress: {e}')

            time.sleep(0.8)

            try:
                data = json.loads(r.text)
                siteName = data.get('name', 'Desconhecido')
                siteDesc = data.get('description', 'Nenhuma descrição disponível')

                plugins = data.get('namespaces', [])

                print(Dgreen + '\n[+] Nome do site       : ' + Lgreen + siteName)
                time.sleep(0.8)
                print(Dgreen + '\n[+] Descrição do site : ' + Lgreen + siteDesc)
                time.sleep(0.8)

                print(Dgreen + '\n[+] Enumerando Plugins:\n')
                plugin_names = set(i.split('/')[0].lower() for i in plugins)
                print(Dgreen + '\n[+] Plugins encontrados:')
                for plugin in sorted(plugin_names):
                	time.sleep(0.1)
                	print(Lgreen + f' [*] {plugin}')

                
                adminpanel_finder(org_url)
                time.sleep(1)
                user_finder(org_url)

            except Exception as e:
                print(Lred + f'[-] Erro ao processar dados JSON: {e}')

        else:
            print(Dgreen + '\n[+] WordPress Detectado: ' + Lred + 'Não')
    else:
        print(Dgreen + '\n[+] Status do site: ' + Lred + f'Offline ({r.reason})')

print(Lcyan + '')
print('[ Obrigado por usar a ferramenta! ]')
sys.exit(0)