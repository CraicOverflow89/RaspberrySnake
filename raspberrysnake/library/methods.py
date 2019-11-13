def when(value, result, fallback = None):

	# Iterate Options
	for condition in result.keys():

		# Test Condition
		if value == condition:
			result[condition]()
			return

	# Invoke Fallback
	if fallback is not None:
		fallback()