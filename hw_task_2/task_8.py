elements = [(2, 12, 'Mg'), (1, 11, 'Na'), (1, 3, 'Li'), (2, 4, 'Be')]

elements_sorted = sorted(elements, key=lambda x: x[1])
print(elements_sorted)
