import pyautogui as pg
import time
a=input("enter no of refreshes: ")
pg.keyDown('win')
pg.press('d')
pg.keyUp('win')
for i in range(int(a)):
	pg.rightClick(442, 207)
	pg.click(495, 271)
	time.sleep(0.5)
print("refreshes done!")
pg.keyDown('win')
pg.press('d')
pg.keyUp('win')
input("")