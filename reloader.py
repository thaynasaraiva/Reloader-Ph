from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Instancia um objeto do tipo WebDriver
driver = webdriver.Chrome()

# Abre a página desejada
driver.get("https://www.kabum.com.br/")

# Espera 5 segundos para a página carregar
sleep(10)

# Faz o reload da página
driver.refresh()

# Espera 5 segundos para a página recarregar
sleep(10)

# Fecha o navegador
driver.quit()