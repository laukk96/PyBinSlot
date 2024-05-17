filepath = './data0002.bin'
outputpath = './output_bin.txt'
data = 0

with open(filepath, 'rb') as file: 
    data = file.readlines()

print(f'{outputpath} Creating data of length: {len(data)}')
with open(outputpath, 'w') as output:
    for i in range(len(data)):
        output.write( str(data[i]) )
        output.write('\n')