from riem.core import Application

# Game Class
class RaspberrySnake(Application):

	def __init__(self):
		self.highscore = 0
		super().__init__("Raspberry Snake", "StateTitle", "raspberrysnake/states", {"colour": "white", "font": "Inconsolata 14"}, "icon")

	def get_score(self):
		return self.highscore

	def new_score(self, value):
		if value > self.highscore:
			self.highscore = value
			return True
		return False

# Launch Application
RaspberrySnake()