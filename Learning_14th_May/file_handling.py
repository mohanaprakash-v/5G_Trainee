files = open("file.txt","r")
content =files.read()
print(content)

file1 =open("file.txt","w")
content=file1.write("Hey this is mohan")
print(content)

file2 = open("file.txt", "a")
content=file2.writelines("helo this is me")
print(content)

with open("file.txt") as file3:
    content=file3.read()
    print(content)

try:
    files = open("file.txt","r")
    content =files.read()
    print(content)
except FileNotFoundError:
    print("File not found")
else:
    print("Bye")
finally:
    files.close()
    print("File read success")
