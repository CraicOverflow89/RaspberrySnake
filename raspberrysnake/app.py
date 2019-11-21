from riem.core import Application

# Game Class
class RaspberrySnake(Application):

	# Constants
	highscore = 0

	def __init__(self):
		super().__init__(self, "Raspberry Snake", "StateIntro", "raspberrysnake/states")

	def get_score(self):
		return Application.highscore

	def new_score(self, value):
		if value > Application.highscore:
			Application.highscore = value
			return True
		return False

# Launch Application
RaspberrySnake()