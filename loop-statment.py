months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthlyExpense = [2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 12500, 13500]
total = 0
totalExpense = sum(monthlyExpense)
eventMonthTotal = 0
oddMonthTotal = 0
for i in range(1, 11):
    if i % 2 == 0:
        eventMonthTotal = eventMonthTotal + monthlyExpense[i]
        continue
    else:
        oddMonthTotal = oddMonthTotal + monthlyExpense[i]
        continue

for item in range(len(monthlyExpense)):
    print("Expense for the month of " + str(months[item]) + " is " + str(monthlyExpense[item]))

print("Total expense :", totalExpense)
print("Total expense of event month from range:", eventMonthTotal)
print("Total expense of odd month from range:", oddMonthTotal)

key_location = "chair"
locations = ["Chair", "Closet", "Garage", "Living Room"]
for i in map(str.lower, locations):
    if i == key_location:
        print("keys found in", i)
        break
    else:
        print("keys is not found in", i)
