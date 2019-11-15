from input.action import Action
from threading import Event, Thread
import pygame

class Controller:

	def __init__(self, app):
		self.app = app

		# Detect Controller
		pygame.init()
		pygame.joystick.init()
		if pygame.joystick.get_count() == 1:

			# Create Listener
			pygame.joystick.Joystick(0).init()
			self.halt = Event()
			self.thread = Thread(target = self.listener, args = (), daemon = False)
			self.thread.start()

	def listener(self):
		while True:
			if self.halt.is_set():
				break
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

	def terminate(self):
		pygame.joystick.Joystick(0).quit()
		self.halt.set()
		# NOTE: if controller was used to perform this action then it causes issues
		#       and the thread is unable to join (but works fine if keyboard called it)
		#self.thread.join()
		pygame.joystick.quit()
		pygame.quit()