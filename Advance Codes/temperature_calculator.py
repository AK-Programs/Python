def temperature():
    while True:
        converter = str(input("What you want to convert: Celsius to Fahreneit (F) or Fahrenheit to Celsius (C): "))

        if(converter == "F"):
            celsius_value = float(input("Enter a value to convert in Fahrenheit: "))
            fahrenheit_converter = (9/5 * celsius_value) + 32
            print(celsius_value,"°C is equal to",fahrenheit_converter,"°F")

        elif(converter == "C"):
            fahrenheit_value = float(input("Enter a value to convert in Celsius: "))
            celsius_converter = (fahrenheit_value - 32) * 5/9
            print(fahrenheit_value,"°F is equal to",celsius_converter,"°C")

        else:
            print("Invalid Option Please choose converting Celsius to Fahrenheit (F) or Fahrenheit to Celsius (C)")

temperature()