file = open("output.txt", 'r')
Data = file.read()
data = Data.split("\n")
data1 = data[0].split()
data2 = data[1].split()
print(data1)

char = []
for x in data1:
    char.append(chr(int(x)))
print(char)

encode = []
for x in data2:
    encode.append(x)
print(encode)