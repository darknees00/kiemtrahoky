
name = str(input("Nhap ten minh: "))
print(len(name))

d = {}
for i in range(1, len(name) + 1):
    d[i] = i * i

print("\ndictionary = ", d)