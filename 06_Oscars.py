actor = str(input())
points_academi = float(input())
jugers = int(input())
points_jugers = points_academi
for i in range(jugers):
    name_jugers = str(input())
    one_juger_points = float(input())
    points_jugers += (len(name_jugers) * one_juger_points) / 2

    if points_jugers >= 1250.5:
        break

if points_jugers >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {points_jugers:.1f}!")
else:
    diff = abs(1250.5 - points_jugers)
    print(f"Sorry, {actor} you need {diff:.1f} more!")
