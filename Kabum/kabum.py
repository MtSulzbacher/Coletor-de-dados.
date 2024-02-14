from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/ofertas/ofertadodia?pagina=1')

#Extrair todos os titulos
titulos = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")

#Extrair todos os preços
precos = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

#Criando a planilha
workbook = openpyxl.Workbook()
#Criando a pagina "produtos"
workbook.create_sheet('Produtos')
#Selecionando a página "produtos"
sheet_produtos = workbook['Produtos']
sheet_produtos['A1'].value = 'Produtos'
sheet_produtos['B1'].value = 'Preços'


for titulo, precos in zip(titulos, precos):
    pass
    sheet_produtos.append([titulo.text,precos.text])
workbook.save('Ofertas do dia.xlsx')