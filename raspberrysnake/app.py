from riem.core import Application

# Game Class
class RaspberrySnake(Application):

	def __init__(self) -> None:
		self.highscore: int = 0
		super().__init__("Raspberry Snake", "StateTitle", "raspberrysnake/states", {"colour": "white", "font": "Inconsolata 14"}, "icon")

	def get_score(self) -> int:
		return self.highscore

	def new_score(self, value: int) -> bool:
		if value > self.highscore:
			self.highscore = value
			return True
		return False

# Launch Application
RaspberrySnake()