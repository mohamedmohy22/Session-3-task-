# Task: Weather Advisor

temp = float(input("\nEnter the current temperature in Celsius: "))
if temp >= 30:
    print("It's a hot day. Stay hydrated!\n")
elif 20 <= temp <= 29:
    print("It's a warm day. Enjoy the weather!\n")
elif 10 <= temp <= 19:
    print("It's a cool day. Wear a jacket!\n")
elif temp < 10:
    print("It's a cold day. Stay warm!\n")

#------------------------------

# Task: Filter and Transform a List (find all the numbers in the list that are divisible by 3)

li = list (range(1, 21))
print("Numbers divisible by 3:", end=" ")

for num in li:
    if num % 3 == 0:
        print(num, end=" ")
print("\n")