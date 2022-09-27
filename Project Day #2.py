#100 Days of Code: Project Day #2

print("Welcome to the tip calculator!")

#Bill Amount
amount = float(input("Please enter the bill amount in R's: "))

#Asking how many people are splitting the bill
splitamount = int(input("How many people will be splitting the bill? "))

#How much do you want to tip?
percentageAmount = int(input("How much % do you want to tip? "))

#Turning the int into a percentage
percentage = percentageAmount/100

#Calc the total with the tip added
total = amount*percentage + amount

#Dividing the bill plus tip between the amount of people
finalamount = total/splitamount

#Printing out how much each person owes
print("Each person will pay R", finalamount, " for the bill!")
