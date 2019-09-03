stringData = str(input())
data = list(stringData)
d = str(input())
d = list(d)
container = []
for i in range(len(data)):
    if data[i] != d and d not in container:
        container.append(data[i])
print(container)