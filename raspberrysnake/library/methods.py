def when(value, result, fallback = None):

	# Iterate Options
	for condition in result.keys():

		# Test Condition
		if value == condition:
			return result[condition]

	# Return Fallback
	if fallback is not None:
		fallback()

	# Return None
	return None