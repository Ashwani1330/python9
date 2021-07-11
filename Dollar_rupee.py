def price_converter(amount,conv_price):
    rupee_amount=amount*conv_price
    return rupee_amount
    
amount=float(input("Enter the amount in dollars: " ))
conv_price=float(input("Enter the dollar-to-rupee conversion price: "))

rupee_amount=price_converter(amount,conv_price)
print("Amount in rupees: ", rupee_amount)


	