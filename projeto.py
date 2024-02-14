from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

#Extrair todos os titulos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

#Extrair todos os preços
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

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
workbook.save('Produtos.xlsx')