def price_checker():
    while True:
        price = float(input("Enter the price of item: "))
        quantity = int(input("Enter the quantity of item: "))
        disscount = float(input("Enter how many percentage of disscount of item (If not type 0)(Don't use % symbol) : "))

        total_price = price * quantity 

        if(disscount > 0):
            print("Total price of item after applying ",disscount,"% discount =",total_price - (total_price * disscount/100))
        
        elif(disscount == 0):
            print("Total price of item =",total_price)

        elif(disscount < 0):
            print("Discount can't be negative value. Please Enter a positve value")

        else:
            print("Something is wrong Please check and Try Again!")

price_checker()