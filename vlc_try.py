#!/usr/bin/python3


import threading
import subprocess

def play():
	args=['vlc','https://www.youtube.com/watch?v=ixPIjt5or-g']
	subprocess.call(args)
	
	
def pause():
	choice = input("")
	if choice == 'q':
		subprocess.call(['vlc://quit'])
	else :
		play()

threading._start_new_thread(play,())
threading._start_new_thread(pause,())


while True:
	pass

