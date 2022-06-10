import os
master = os.getcwd()

filenumber= 100
filename = 'file' #number of files to create
filetype = '.txt' #output filetype
file_list = list(range(1,filenumber+1))

for i in file_list:
  print(i)
  next_file = filename+str(i)+filetype
  file_list[i-1]=next_file    
  with open(next_file, 'w') as h:
    h.write("a")
    h.close()

print(file_list)