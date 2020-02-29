results = []
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
    results.append(i)
print("The number of  elements are ", len(results), ".")
print("Bye")
