import pyautogui
import time
from termcolor import colored

def spam_text(a, b):
	time.sleep(10)
	for i in range (1, b+1):
		pyautogui.typewrite(a + str(i))
		pyautogui.press("enter")


txt = input(colored("Masukkan Text : ", "blue"))
banyak = int(input(colored("Banyaknya text di ulang : ", "blue")))

print(colored("Perhatikan kursor Pastikan kursor berada di textbox saat program berjalan!", "red"))
print(colored("Jeda waktu 10s saat program benar-benar berjalan ", "red"))
ready = input(colored("Apakah anda sudah siap ? [Y/n] : ", "yellow"))

if ready == "Y" or ready == "y":
	print(colored("Program berjalan ! [10s] arahkan kursor", "green"))
	spam_text(txt, banyak)
else:
	print(colored("Program di interupsi !", "red"))
