#create your own password locally!
import random
import string
total = string.ascii_letters + string.digits + string.punctuation
#define length of password
length = 12
password = "".join(random.sample(total, length))
print(password)