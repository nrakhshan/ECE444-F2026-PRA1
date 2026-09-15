class utils:

	def reversed(num_int):
		"""Return the int in reverse order."""
		sign = -1 if num_int < 0 else 1
		return sign * int(str(abs(num_int))[::-1])

	def formatter(num_int):
		"""Return the int in binary and octal format."""
		return format(num_int, "b"), format(num_int, "o")
