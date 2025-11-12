costprice = int(input("Enter the Cost Price: "))
sellingprice = int(input("Enter the Selling Price: "))

if(sellingprice > costprice):
    print("Profit: ")
    profit = sellingprice - costprice
    print(profit)
else :
    print("Loss: ")
    loss = costprice - sellingprice
    print(loss)