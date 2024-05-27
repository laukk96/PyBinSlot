a = input("Input your binary here in the format of x00\\x00\\:")

a = a.replace("\\", " ")
a = a.replace("x", "")

print(a)