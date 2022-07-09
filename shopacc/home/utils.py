from posixpath import split


def convertVND(price):
    price = str(price)
    split = price.split(".")

    if(len(split[0]) == 4):
        price = price[:1] + "." + price[1:]
        return price
    
    if(len(split[0]) == 5):
        price = price[:2] + "." + price[2:]
        return price
    
    return price

    


price = convertVND(356.000)

print(price)
