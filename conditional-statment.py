#num = input("Enter a Number: ")
#num = int(num)
#print("You entered a", "even number" if num % 2 == 0 else "odd number")

indianCuisine = ["Samosa", "Daal", "Sambher"]
chineseCuisine = ["Fried Rice", "Pot Sticker", "Noodles"]
italianCuisine = ["Pasta", "Pizza", "Macaronis"]

dish = input("Enter your dish name:").lower()

if dish in map(str.lower, indianCuisine):
    print("Indian Cuisine")
elif dish in map(str.lower, chineseCuisine):
    print("Chinese Cuisine")
elif dish in map(str.lower, italianCuisine):
    print("Italian Cuisine")
else:
    print("Dish is not in the Menu")
