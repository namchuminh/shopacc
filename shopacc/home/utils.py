from posixpath import split
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from matplotlib.pyplot import pink

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

def checkPay(price, money):
    money = money - price
    if(money >= 0):
        return money
    else:
        return False

def sendAcc(emailacc, username, password):
    try:
        subject = 'Fo4Shop.com - Thông tin mua tài khoản Fifa Online 4!'
        message = 'Chào bạn! Bạn đã hoàn tất quá trình mua tài khoản và thanh toán tại Fo4Shop.com. \nTài khoản:  ' + username + '\nMật khẩu: ' + password + '\nCảm ơn bạn đã tin tưởng và ủng hộ chúng tôi!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emailacc,]
        print(emailacc)
        if (send_mail(subject, message, 'Fo4Shop.Com ' + email_from, recipient_list, fail_silently=False)):
            return True
        else:
            return False
    except:
        return False

def convertPrice(acc):
    for i in range(len(acc)):
        acc[i].price = convertVND(acc[i].price)
        acc[i].sale = convertVND(acc[i].sale)
    return acc


def sendMess(email, fullname, mess):
    try:
        subject = 'Fo4Shop.com - Tin nhắn khách hàng!'
        message = 'Khách hàng: ' + fullname + '\nEmail: ' + email + '\nTin nhắn: ' + mess
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['chuminhnamma@gmail.com',]
        if (send_mail(subject, message, 'Fo4Shop.Com ' + email_from, recipient_list, fail_silently=False)):
            return True
        else:
            return False
    except:
        return False