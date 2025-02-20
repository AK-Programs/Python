def temperature():
    while True:
        converter = str(input("What you want to convert: Celsius to Fahreneit (F) or Fahrenheit to Celsius (C): "))

        
        if(converter == "F"):
            celsius_value = float(input("Enter a value to convert in Fahrenheit: "))
            fahrenheit_converter = (9/5 * celsius_value) + 32
            round_fahrenheit = round(fahrenheit_converter, 2)
            print(celsius_value,"°C is equal to",round_fahrenheit,"°F")


        elif(converter == "C"):
            fahrenheit_value = float(input("Enter a value to convert in Celsius: "))
            celsius_converter = (fahrenheit_value - 32) * 5/9
            round_celsius = round(celsius_converter, 2)
            print(fahrenheit_value,"°F is equal to",round_celsius,"°C")

        else:
            print("Invalid Option Please choose converting Celsius to Fahrenheit (F) or Fahrenheit to Celsius (C)")

temperature()