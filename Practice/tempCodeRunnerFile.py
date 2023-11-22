print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage_tip = input("what percentage of tip would you like to give 10,12 or 15? ")
converted_percenatge_bill = int(percentage_tip)/100+1
Split= input("How many people to split the bill ? ")
total_bill = float(bill)*float(converted_percenatge_bill)
rounded_bill = round(total_bill,2)
print(f"Each person has to pay ${rounded_bill/int(Split)}")