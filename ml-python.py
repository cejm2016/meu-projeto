#aula hash lira.
#passo 1

import pyautogui
import time
import pandas

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
print(pyautogui.position())
pyautogui.click(x=707, y=292)

codigo = "A01234567B"
pyautogui.write(codigo)
pyautogui.press("tab")

marca = "Samsung"
pyautogui.write(marca)
pyautogui.press("tab")

tipo = "Tela"
pyautogui.write(tipo)
pyautogui.press("tab")

categoria = "Eletronicos"
pyautogui.write(categoria)
pyautogui.press("tab")

preco_unitario = "1000.00"
pyautogui.write(preco_unitario)
pyautogui.press("tab")

custo = "800.00"
pyautogui.write(custo)
pyautogui.press("tab")

obs = ""
pyautogui.write(obs)
pyautogui.press("tab")

pyautogui.press("enter")

pyautogui.scroll(2000)

