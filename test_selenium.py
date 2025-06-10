
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configurar Chrome headless para ambiente do Colab
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Acessar o site
driver.get("https://example.com")

# Verificações
assert "Example Domain" in driver.title

# Clicar no link
elem = driver.find_element(By.XPATH, '//a[text()="More information..."]')
elem.click()

time.sleep(2)  # Aguarda carregamento da nova página

assert "IANA" in driver.title

driver.quit()
