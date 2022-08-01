import re

from home.utils import convertPrice, convertVND

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checkemail(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def checkpassword(passwd):
    if passwd is None:
        return False
    else:
        return True

def checkusername(username):
    if re.match(r'^[\w.-]+$', username):
        return True
    else:
        return False

def convertProductVND(cartDetail):
    for i in range(len(cartDetail)):
        cartDetail[i].product.price = convertVND(cartDetail[i].product.price)
        cartDetail[i].product.sale = convertVND(cartDetail[i].product.sale)
    return cartDetail

def totalPrice(cartDetail):
    total = 0
    for i in range(len(cartDetail)):
        total += cartDetail[i].product.price
    return convertVND(total)
