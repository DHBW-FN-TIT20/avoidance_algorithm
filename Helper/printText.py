from ev3dev2.display import Display
import ev3dev2.fonts as fonts
import time

screen = Display()
font = fonts.load("luIS19")

def writeScreen(message):
	#print("Write to the screen...")
	screen.clear()
	screen.draw.text((0, 64), message, font=font)
	screen.update()
