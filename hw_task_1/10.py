lst = [2, 4, 5, 8, 9, 13]

# for number in range(len(lst)):
#     lst[number] *= number
#     print(lst)
# результат [0, 4, 10, 24, 36, 65]

index = 0
while index < len(lst):
    lst[index] = lst[index] * index
    index += 1
print(lst)
