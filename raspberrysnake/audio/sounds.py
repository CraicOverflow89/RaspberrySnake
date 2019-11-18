from playsound import playsound

class SoundLoader:

	def play(sound):
		playsound("resources/sounds/%s.mp3" % sound)