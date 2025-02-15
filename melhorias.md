## O que mudou?

### Removido:

<ul>
	<li> Uso de **random_useragent** (substituído por **fake_useragent**). </li>
	<li> Uso ineficiente de **requests.get()**. </li>
	<li> Parser **xml** do BeautifulSoup (substituído por **lxml**)
	<li> **Má formatação** de mensagens. </li>
</ul>

### Adicionado:

<ul>
	<li> **requests.Session()**, substituindo o uso de vários **requests.get()**.</li>
	<li> Blocos **try/except**. </li>
	<li> Caso a versão do WordPress não apareça no **xml**, procura no **HTML**. </li>
	<li> Correção na detecção do **painel admin**. </li>
	<li> Melhoria na **listagem de plugins**. </li>
</ul>