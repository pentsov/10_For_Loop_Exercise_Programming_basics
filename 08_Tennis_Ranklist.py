import math
num_tournirs = int(input())
starting_points = int(input())
total_points = 0
win_tournirs = 0
for i in range(num_tournirs):
    level = str(input())
    if level == "W":
        total_points += 2000
        win_tournirs += 1
    elif level == "F":
        total_points += 1200
    elif level == "SF":
        total_points += 720

average = total_points / num_tournirs
percent = win_tournirs / num_tournirs * 100
print(f"Final points: {total_points + starting_points}")
print(f"Average points: {math.floor(average)}")
print(f"{percent:.2f}%")
