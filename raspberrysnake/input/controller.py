from input.action import Action
import pygame
import threading

class Controller:

	def __init__(self, app):
		self.app = app

		# Detect Controller
		pygame.init()
		pygame.joystick.init()
		if pygame.joystick.get_count() == 1:

			# Create Listener
			pygame.joystick.Joystick(0).init()
			threading.Thread(target = self.listener, args = (), daemon = True).start()

	def listener(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
					self.app.action(Action.ACTION)
				elif event.type == pygame.JOYAXISMOTION and (event.axis == 0 or event.axis == 1):
					if event.axis == 0:
						if event.value >= 0.8:
							self.app.action(Action.RIGHT)
						elif event.value <= -0.8:
							self.app.action(Action.LEFT)
					elif event.axis == 1:
						if event.value >= 0.8:
							self.app.action(Action.DOWN)
						elif event.value <= -0.8:
							self.app.action(Action.UP)