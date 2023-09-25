years = int(input())
washingmachine = float(input())
one_toy_price = int(input())
toys_count = 0
money = 0
even_brother =0
total_birthday_money = 0

for i in range(1, years+1):

    if i % 2 == 0:
        money += 10
        total_birthday_money += money
        even_brother +=1
    else:
        toys_count +=1

savings = (toys_count * one_toy_price + total_birthday_money) - even_brother
diff = abs(savings - washingmachine)
if savings >= washingmachine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


