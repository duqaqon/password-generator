import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "!#¤%&/()=?@£$€"

all=lower + upper + NUMBER + Symbol
length = 12
password = "".join(random.sample(all,length))
print(" Your new generated password is: ",password)


# Generator made by Munken