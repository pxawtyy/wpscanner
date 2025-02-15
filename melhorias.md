## O que mudou?

### Removido:

<ul>
	<li> Uso de <strong>random_useragent</strong> (substituído por <strong>fake_useragent</strong>). </li>
	<li> Uso ineficiente de <strong>requests.get()</strong>. </li>
	<li> Parser <strong>xml</strong> do BeautifulSoup (substituído por <strong>lxml</strong>)
	<li> <strong>Má formatação</strong> de mensagens. </li>
</ul>

### Adicionado:

<ul>
	<li> <strong>requests.Session()</strong>, substituindo o uso de vários <strong>requests.get()</strong>.</li>
	<li> Blocos <strong>try/except</strong>. </li>
	<li> Caso a versão do WordPress não apareça no <strong>xml</strong>, procura no <strong>HTML</strong>. </li>
	<li> Correção na detecção do <strong>painel admin</strong>. </li>
	<li> Melhoria na <strong>listagem de plugins</strong>. </li>
</ul>
