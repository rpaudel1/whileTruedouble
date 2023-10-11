def double(number):
	doubled = number * 2
	return doubled
def main():
	while True:
		num = input("Give me a number to double: ")
		if num.isnumeric():
			num_doubled = double(int(num))
			print(num_doubled)
		else:
			print("That’s not a number! Exiting...")
			break
	print("Game over!")
if __name__ == "__main__":
	main()
