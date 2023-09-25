num_tabs = int(input())
salary = float(input())

for i in range(num_tabs):
    tabs = input()
    if tabs == "Facebook":
        salary -= 150
    elif tabs == "Instagram":
        salary -= 100
    elif tabs == "Reddit":
        salary -= 50
    if salary <=0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))
