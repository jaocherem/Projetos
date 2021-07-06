import pyautogui
import time

"""
Rode o programa e abra o whatsapp web para enviar a mensagem
"""

def annoyer(n):
    for i in range(n):
        pyautogui.typewrite("escreva aqui")
        pyautogui.press("enter")

time.sleep(3)

# número de vezes que a mensagem será digitada
annoyer(3000)
