out_file = open('C:/Users/rwmo2/Documents/Python Scripts/mydata.txt', 'w')
#\n for line break
#out_file.write('Hello\n')
#out_file.write('world!')

#forces data to be written immediately
#out_file.flush()

weekends = ['Saturday', 'Sunday']
out_file.writelines(weekends)
out_file.writelines(weekends)

#closes file
out_file.close()

#read file
in_file = open('C:/Users/rwmo2/Documents/Python Scripts/mydata.txt', 'r')
print(in_file.read(1))
#read() and readline() do the same thing w/o bytes
#print(in_file.read())
print(in_file.readline())
in_file.close()
