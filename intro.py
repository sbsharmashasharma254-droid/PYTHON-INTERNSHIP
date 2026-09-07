
a = 1
b = 0

print(a | b )

# 2/2 -> 0 : even
# 3/2 -> !0 :odd
# if mera_condition:
#    hamara operation

if 3%2 == 0 :
    print("EVEN")

# check age
age = int(input("Enter your age"))
if age >= 18:
   print("You can vote.")


# Multi case
diary = 50
book = 100
pen = 10
user_money = int(input("Your money:"))

if user_money >= 160:
    print("You can buy: diary, book and pen.")
elif user_money <= 100 & user_money >= 10 :
    print("You can buy:pen, book")
else:
    print("Thanks")


#if cond.:
 #  operation.



#if cond.1:
 #   opera...
#elif con2:
#    opera 2...


if user_money < 100:
    if user_money == 0:
        print("You can't buy anything.")
    if user_money == 50:
        print("You can only either pen or book")
elif user_money > 100:
    if user_money == 150:
        print("You can buy only book")
    elif user_money >= 160 :
        print("you can buy anything..")    



if False:
    print("I'm running")
elif False:
    print("I'm running")
else:
    print("I'm here")       


