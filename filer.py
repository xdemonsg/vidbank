import os, shutil
master = os.getcwd()
filecount = 0
max_files = 25
folder_no = 0
folders_name = 'file'
filetype ="txt"
target_filelist = []

for path, dirs, files in os.walk(master):
  for f in files:
    suffix = f[-3:]    
    if suffix == filetype and path == master:
      filecount +=1
      target_filelist.append(f)
      #print(f)

#print(target_filelist)


folder_no = filecount // max_files

if filecount / max_files > folder_no:
  folder_no+=1


file_list = list(range(0,folder_no))

for i in file_list:

  next_file = folders_name+str(i)
  file_list[i]=next_file

print(file_list)


def create_files():
  for i in file_list:
    os.mkdir(i)

def move_files():
  file_count = 0
  folder_count = 0
  for i in target_filelist:
    try:
      shutil.move(i, file_list[folder_count])
      file_count+=1
      if file_count == max_files:
        folder_count += 1
        file_count = 0 
    except:
      print("error moving " + i)
    
create_files()
move_files()
