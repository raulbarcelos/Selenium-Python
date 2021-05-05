import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import info_user as usuario


# 1. Abrindo o site no webdriver
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(usuario.url)


def realizar_login():
    try:
        # carregar elemento do campo input do formulário (email)
        login_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_email"))
        )
        login_email.click()
        email = usuario.email
        login_email.send_keys(email)  # Enviar key email

        #carregar elemento do campo formulário de preencher senha
        login_senha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_senha"))
        )
        login_senha.click()
        senha = usuario.senha
        login_senha.send_keys(senha)  # Enviar key password

        # carregar elemento do botão de login
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='ui-button -warning -medium -block--sm']"))
        )
        login_form.click()  # Clicar no botão login
    
    except:
        print("Erro ao realizar login!")
        driver.quit()
    finally:
        print("Login realizado!")


realizar_login()