from utils import utils


def main():
	for value in ["123", 1.5, 23]:
		for function in [utils.reversed, utils.formatter]:
			try:
				output = function(value)
			except TypeError as error:
				assert str(error) == "Invalid input. Expected int"
			else:
				print("Valid output:", output)


if __name__ == "__main__":
	main()
