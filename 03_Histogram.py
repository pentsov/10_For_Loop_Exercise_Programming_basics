num = int(input())
first_range = 0
second_range = 0
third_range = 0
forth_range = 0
fifth_range = 0
for i in range(num):

    number = int(input())
    if number < 200:
        first_range += 1
    elif 200 <= number <= 399:
        second_range += 1
    elif 400 <= number <= 599:
        third_range += 1
    elif 600 <= number <= 799:
        forth_range += 1
    elif number >= 800:
        fifth_range += 1


first_range = first_range/num*100
second_range = second_range/num*100
third_range = third_range/num*100
forth_range = forth_range/num*100
fifth_range = fifth_range/num*100
print(f"{first_range:.2f}%")
print(f"{second_range:.2f}%")
print(f"{third_range:.2f}%")
print(f"{forth_range:.2f}%")
print(f"{fifth_range:.2f}%")
