#Python com pyautogui... automatizando trabalho de inserção de dados planilhados do CSV para uma base hospedada ou SITE.
#Essa ideia foi construida com curso.

import pyautogui
import time
import pandas
import numpy


pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")   #site ou programa 
pyautogui.press("enter")

#endereço navegador
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#direcionador, para clicar aonde você precisa, click e posição.
time.sleep(1)
pyautogui.click(x=754, y=409)
pyautogui.write("teste@teste.com.br")
pyautogui.press("tab")
pyautogui.write("teste@10")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
print(tabela)
time.sleep(1)

for linha in tabela.index:
    
    pyautogui.click(x=707, y=292)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str (tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(2000)

