num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
sorted_list = sorted(num_list)
# for i in sorted_list:
#     if i > 45:
#         print (f"over 45 {i}")
#     else :
#         print (f"under 45 {i}")
x = 0
for index,value in  enumerate(num_list):
    x += 1
    if value == 36:
        print(index,value)
        break
a = isinstance("aa",int)

print(a)  