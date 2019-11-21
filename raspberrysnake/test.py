from riem.library import ArrayList
from riem.states import State
import importlib, inspect, os, re

def load(directory):

	# Module Logic
	def load(module):

		# List Classes
		result = ArrayList(list(module.__dict__.keys())).filter(lambda it: inspect.isclass(getattr(module, it)))

		# Map Classes
		result = result.reject(lambda it: it == "State").map(lambda it: getattr(module, it))
		# NOTE: could reject "State" then map getattr to remove repetition
		#       instead of calling getattr for filter isclass AND map

		# Return States
		return result.filter(lambda it: issubclass(it, State))

	# Directory Path
	directory_path = os.path.join(os.getcwd(), directory)

	# List Files
	file_list = ArrayList(os.listdir(directory_path)).reject(lambda it: it.startswith("_")).map(lambda it: it.split(".")[0])
	# NOTE: current reject is not going to ignore directories

	# Return States
	return ArrayList(file_list.map(lambda it: load(importlib.import_module("%s.%s" % (directory.split("/")[-1], it)))))
	# NOTE: construcrtor/add_all should be creating ArrayList<State>
	#       but currently getting ArrayList<ArrayList<State>>
	#       wrapping in list() doesn't work and shouldn't have to do that
	#       check that arrays and ArrayList objects with only one element are still unpacked correctly

print(load("raspberrysnake/states"))
# NOTE: would be better to not have to include subdirectory in project