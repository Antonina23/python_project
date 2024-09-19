greeting = "Hello, my dear friends!"

list = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        list.append(i)

print(count)
print(list)