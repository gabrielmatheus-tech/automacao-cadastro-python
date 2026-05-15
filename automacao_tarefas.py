import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.8


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=490, y=409)
pyautogui.write("zygabriel.matheus@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234abc")
pyautogui.press("enter")
time.sleep(5)

import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=668, y=283)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)