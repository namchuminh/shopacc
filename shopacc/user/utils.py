import re

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
