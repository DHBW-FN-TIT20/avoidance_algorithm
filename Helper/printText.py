from ev3dev2.display import Display
import ev3dev2.fonts as fonts
import time

screen = Display()
font = fonts.load("luIS19")

#prints the message on the screen of the ev3 brick
def writeScreen(message):
	screen.clear()
	screen.draw.text((0, 64), message, font=font)
	screen.update()
