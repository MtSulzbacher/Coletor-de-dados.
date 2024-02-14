Para criar um README adequado para o código que automatiza a coleta de dados de produtos da página de ofertas do dia do site Kabum e os salva em uma planilha do Excel, incluindo links diretos para os produtos, segue um exemplo de como poderia ser estruturado:

---

# Coletor de Ofertas Kabum

Este script em Python automatiza a coleta de dados das ofertas do dia no site da Kabum, incluindo nomes de produtos, preços originais, preços com desconto e a porcentagem de desconto. Além disso, ele adiciona um hyperlink na descrição de cada produto, direcionando para a página de compra correspondente.

## Funcionalidades

- Extração de nomes, preços originais e preços com desconto dos produtos listados na página de ofertas do dia.
- Cálculo da porcentagem de desconto para cada produto.
- Criação de uma planilha do Excel para armazenar os dados coletados.
- Inclusão de hyperlinks diretos para as páginas de compra dos produtos na descrição de cada um na planilha.

## Tecnologias Utilizadas

- Python
- Selenium WebDriver
- OpenPyXL

## Como Usar

### Pré-Requisitos

- Python instalado em sua máquina.
- Bibliotecas Selenium e OpenPyXL instaladas. Você pode instalá-las usando o pip:

```bash
pip install selenium openpyxl
```

- WebDriver do Chrome (ChromeDriver) compatível com a versão do seu navegador instalado.

### Execução

1. Clone ou baixe o script para o seu computador.
2. Certifique-se de que o ChromeDriver esteja no PATH do seu sistema ou no mesmo diretório do script.
3. Execute o script:

```bash
python coletor_ofertas_kabum.py
```

4. Após a execução, uma planilha chamada "Ofertas do dia.xlsx" será salva no mesmo diretório do script, contendo as informações coletadas.

## Nota

Este script foi desenvolvido para fins educacionais e de demonstração. A estrutura do site da Kabum pode mudar, o que pode requerer ajustes no script.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

Esse README fornece uma visão geral clara do propósito do script, como configurar o ambiente para rodá-lo, e como executá-lo. Lembre-se de ajustar qualquer parte do README conforme necessário para refletir qualquer particularidade ou pré-requisito específico do seu projeto ou ambiente.
