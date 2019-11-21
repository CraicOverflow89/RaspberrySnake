from riem.library import ArrayList
from riem.states import State
import importlib, inspect, os, re

def load(directory):

	# Directory Path
	directory_path = os.path.join(os.getcwd(), directory)

	# List Files
	file_list = ArrayList(os.listdir(directory_path)).reject(lambda it: it.startswith("_")).map(lambda it: it.split(".")[0])
	# NOTE: current reject is not going to ignore directories

	# Module Logic
	def load_module(module):

		# List Attributes
		result = ArrayList(list(module.__dict__.keys())).reject(lambda it: it == "State")

		# Map Classes
		result = result.map(lambda it: (it, getattr(module, it)))
		# NOTE: should maybe create tuple after map getattr and call method on it to get id for the name data

		# Return States
		return result.filter(lambda it: inspect.isclass(it[1]) and issubclass(it[1], State))

	# Return States
	result = {}
	for module in file_list.map(lambda it: load_module(importlib.import_module("%s.%s" % (directory.split("/")[-1], it)))):
		for name, state in module:
			result[name] = state
	return result

print(load("raspberrysnake/states"))
# NOTE: would be better to not have to include subdirectory in project
# NOTE: need to handle errors when directory is invalid or no State children are found