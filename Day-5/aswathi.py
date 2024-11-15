current_temperature= float(input("Enter temperature: "))
if current_temperature > 30:
    print("It's hot!")
elif 20 <= current_temperature <= 29:
    print("It's warm!")
elif 10 <= current_temperature <= 19:
    print("It's cool!")
elif current_temperature<10:
    print("It's cold!")
else:
    print("It's ok!")


