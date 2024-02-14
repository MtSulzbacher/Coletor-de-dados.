# Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Configuração do WebDriver para usar o Chrome
driver = webdriver.Chrome()
# Acessa a página de ofertas do dia do site Kabum
driver.get('https://www.kabum.com.br/ofertas/ofertadodia?pagina=1')

# Extrai todos os títulos dos produtos usando XPATH
# O XPATH é ajustado para buscar elementos específicos que contêm os títulos dos produtos
titulos = driver.find_elements(By.XPATH, "//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")

# Extrai todos os preços dos produtos usando XPATH
# Similar aos títulos, o XPATH aqui busca por elementos que contêm os preços
precos = driver.find_elements(By.XPATH, "//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

# Cria uma nova planilha Excel
workbook = openpyxl.Workbook()
# Adiciona uma nova aba chamada 'Produtos'
workbook.create_sheet('Produtos')
# Seleciona a aba 'Produtos' para manipulação
sheet_produtos = workbook['Produtos']

# Configura os títulos das colunas na primeira linha da planilha
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

# Itera sobre os títulos e preços dos produtos extraídos
for titulo, preco in zip(titulos, precos):
    # Adiciona o texto do título e do preço na próxima linha disponível da planilha
    sheet_produtos.append([titulo.text, preco.text])

# Salva a planilha no disco com o nome 'Ofertas do dia.xlsx'
workbook.save('Ofertas do dia.xlsx')

# Fecha o navegador
driver.quit()
#teste