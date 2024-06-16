from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def loguim(usuario, filial, senha, url):
    # Instanciando o driver
    driver = webdriver.Chrome()
    # URL que eu vou entrar
    driver.get(url)
    sleep(5)

    # Mudando para o frame do menu
    driver.switch_to.frame("menu")

    # Localizando o campo de entrada do usuário e inserindo o usuário
    user_input = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/input")
    user_input.send_keys(usuario)

    # Localizando e preenchendo os outros campos
    filial_input = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]/input")
    filial_input.send_keys(filial)

    senha_input = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/input")
    senha_input.send_keys(senha)

    # Localizando e clicando no botão de login (assumindo que é um botão de tipo submit)
    login_button = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[5]/td/table/tbody/tr/td/input")
    login_button.click()
    sleep(5)

    # Mudando para o frame do menu do usuário
    driver.switch_to.default_content()  # Sair do frame atual
    driver.switch_to.frame("menuusuario")

    # Clicando no texto ao lado da imagem para abrir OS
    abrir_os_link = driver.find_element(By.XPATH,
                                        "//span[contains(text(), 'TL11800 - Realização de Manutenção Corretiva')]")
    abrir_os_link.click()
    sleep(3)
    # Lidando com o alerta (se houver)
    try:
        alert = Alert(driver)
        alert.accept()  # Ou alert.dismiss() se quiser rejeitar
    except:
        print("Nenhum alerta foi encontrado.")

    # Mudando para o frame principal para inserir os dados
    driver.switch_to.default_content()  # Sair do frame atual
    driver.switch_to.frame("main")

    # Exemplo de como inserir dados na tela principal
    # Exemplo:
    # os_input = driver.find_element(By.XPATH, "xpath_do_input_na_tela_principal")
    # os_input.send_keys("Dados da OS")

    # Espera para visualizar o resultado
    sleep(5)

    # Fechar o navegador
    driver.quit()


loguim(os.getenv("SYSTEM_USER"), os.getenv("SYSTEM_FILIAL"), os.getenv("SYSTEM_PASSWORD"), os.getenv("SYSTEM_URL"))
