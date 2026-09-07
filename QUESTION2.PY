# NUMBER ANALIZE



n = int(input("Enter a number: "))

sum_all = 0
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    print(i)

    sum_all = sum_all + i

    if i % 2 == 0:
        print("Even")
        sum_even = sum_even + i
    else:
        print("Odd")
        sum_odd = sum_odd + i

print("Sum of all numbers =", sum_all)
print("Sum of even numbers =", sum_even)
print("Sum of odd numbers =", sum_odd)

if sum_all % 2 == 0:
    print("Total sum is Even")
else:
    print("Total sum is Odd")