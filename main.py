import sys
import pandas as pd
import datetime
import json

# Check if the number of command line arguments is equal to 2, the python file, and then the amount
if(len(sys.argv) != 2):
    raise Exception("Invalid command line arguments!!")

amount = 0

# Check if the command line argument passed is a number and throw an exception if it is not
try:
    amount = int(sys.argv[1])
except ValueError:
    raise Exception("The command line argument provided is not a valid amount! The amount must be greater than or equal to 0.")

# Check if the spending amount is greater than or equal to 0, you can't spend a negative amount
if amount < 0:
    raise Exception("You cannot spend a negative number of points")

transactions = []

# Read in the CSV using pandas and create a list of the rows of the data frame that is read in, if there are no transactions throw an exception
try:
    transactions = pd.read_csv("./data/same_time_transactions.csv").values.tolist()
except pd.errors.EmptyDataError:
    raise Exception("No payer transactions were found on record!")
    
# Sort the transactions by the converted date time objects
sorted_transactions = sorted(transactions, key=lambda t: datetime.datetime.strptime(t[2], "%Y-%m-%dT%H:%M:%SZ"))

payerMap = {}

# Go through each transaction:
# if the transaction amount is negative, add it to your running amount
# if the transaction amount is less than or equal to the running amount, subtract it from the running amount
# if the transaction amount is greater than the running amount, add the difference to the map storing the results
for transaction in sorted_transactions:
    payer, points, time = transaction
    if payer not in payerMap:
        payerMap[payer] = 0
    if points < 0:
        amount -= points
    elif amount >= points:
        amount -= points
    elif points > amount:
        payerMap[payer] = payerMap[payer] + (points - amount)
        amount = 0

# Print the remaining number of points if all points haven't been spent
if amount > 0:
    print(f"You weren't able to consume all of your points. You have {amount} points left.")

# Convert map to json object and print the result
user_points = json.dumps(payerMap, indent = 4) 
print(user_points)


    

