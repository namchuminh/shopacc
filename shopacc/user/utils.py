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

def totalPrice(cartDetailTotal):
    total = 0
    for i in range(len(cartDetailTotal)):
        if(cartDetailTotal[i].product.product == True):
            total += cartDetailTotal[i].product.price
    return convertVND(total)


def checkCard(type,seri,code):
    if(type == "" ):
        return "Vui lòng chọn loại thẻ!"
    if(type != "viettel" or type != "mobifone" or type != "vinaphone"):
        return "Vui lòng chỉ chọn loại thẻ là: Viettel hoặc Mobifone hoặc VinaPhone!"
    if(seri == ""):
        return "Vui lòng nhập vào seri thẻ!"
    else:
        if(re.match(r'^([\s\d]+)$', seri) == False):
            return "Vui lòng nhập lại seri thẻ!"
    
    if(code == ""):
        return "Vui lòng nhập vào mã thẻ!"
    else:
        if(re.match(r'^([\s\d]+)$', code) == False):
            return "Vui lòng nhập lại mã thẻ!"
    return True