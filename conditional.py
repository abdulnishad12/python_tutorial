# ###
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
###
## admin,admin ==  admin login
## user,user == user login
lista = [1,2,3,4,5]
list_even = []
list_odd =  []
for i in lista:
    if (i % 2 == 0):
        list_even.append(i)
    else:
        list_odd.append(i)
print("odd numbers are ",list_odd)
print("even numbers are ",list_even)
        

username = input("Enter the username")
password = input("Enter the password")
if username == 'admin' and password == 'admin':
    print("Logged in as admin")
elif username == 'user' and password == 'user':
    print("user login successfull")
else:
    print("Login Failed")
