num_groups = int(input())
musala_range = 0
monblan_range = 0
kilimandjaro_range = 0
k2_range = 0
everest_range = 0
total_trecking = 0
for i in range(num_groups):

    people_treking = int(input())
    if people_treking <= 5 :
        musala_range += people_treking
       # total_trecking += people_treking
    elif 6 <= people_treking <= 12:
        monblan_range += people_treking
       # total_trecking += people_treking
    elif 13 <= people_treking <= 25:
        kilimandjaro_range += people_treking
        #total_trecking += people_treking
    elif 26 <= people_treking <= 40:
        k2_range += people_treking
        #total_trecking += people_treking
    elif people_treking >= 41:
        everest_range += people_treking
        #total_trecking += people_treking

total_trecking = musala_range + monblan_range + kilimandjaro_range + k2_range + everest_range


musala_range = musala_range/total_trecking*100
monblan_range = monblan_range/total_trecking*100
kilimandjaro_range = kilimandjaro_range/total_trecking*100
k2_range = k2_range/total_trecking*100
everest_range = everest_range/total_trecking*100
print(f"{musala_range:.2f}%")
print(f"{monblan_range:.2f}%")
print(f"{kilimandjaro_range:.2f}%")
print(f"{k2_range:.2f}%")
print(f"{everest_range:.2f}%")
