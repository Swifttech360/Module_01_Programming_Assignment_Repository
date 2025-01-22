while True:
	try:
		baseCharge = float(input('Enter meal price: '))
	except ValueError:
		print("invalid input, please try again")
		continue
	tip = (baseCharge * .18)
	tax = (baseCharge * .07)
	total = (baseCharge + tip + tax)
	print(f"\nMeal Price: {baseCharge:.2f} \n"
	      f"18% Tip: ${tip:.2f}\n"
	      f"7% Tax: ${tax:.2f}\n\n"
	      f"TOTAL: ${total:.2f}")
	loopQuestion = input("again? (y/n)\n").lower()
	if loopQuestion in ("n", "no", "break"):
		print("Have a good one!")
	else:
		print("\n")
	
		
