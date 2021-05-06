import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login import driver

def list_disciplinas(lista):
    disciplinas = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h1[contains(@class, 'sc-eHgmQL bnjYx')]"))
    )
    contador = 0
    titulo_em_texto=[]
    for disciplina in disciplinas:                          # para cada elemento encontrado
        contador+=1
        lista.append(disciplina)                            # adiciona webelement à lista que foi passada como paramentro
        linha = "{} - {}".format(contador, disciplina.text) # atribui texto do webelement (disciplina) atual da iteração
        subst_text = linha.replace("/", "ara")              # substitui as barras para conseguir criar diretórios
        texto_modif = subst_text.replace(":", "-")          # substitui o : (dois pontos) para conseguir criar diretórios
        titulo_em_texto.append(texto_modif)                 # adiciona string titulo modificado à lista titulo em texto.
        print(texto_modif)

lista=[]
list_disciplinas(lista)