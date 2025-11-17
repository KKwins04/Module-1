temperature = float(input("Enter the temperature in °C: "))

if temperature >= 25:
    print("It is warm enough to wear light clothes.")
elif 18 <= temperature < 25:
    print("You can wear light clothes, but you may need a light jacket.")
elif 10 <= temperature < 18:
    print("It is not ideal for light clothes. Wear something warmer.")
else:
    print("It is too cold for light clothes. Dress warmly!")
