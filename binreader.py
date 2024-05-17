filepath = './data0002.bin'
data = 0

with open(filepath, 'rb') as file: 
    data = file.readlines()
    
    
with open("output.txt", 'w') as output:
    for i in range(len(data)):
        output.write( str(data[i]) )
        output.write('\n')