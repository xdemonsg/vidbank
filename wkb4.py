import os
master = os.getcwd()



#jj = open("testbank.html", "a")
notes_file = open("video_list.json", "a")

st1='<video width="320" height="240" controls><source src="'
st2='" type="video/mp4"></video>' 
st3='<h2>'
st4='</h2><br>'
file_counter = 0
file_counter2 = 0

star_string = '"rating":"3/5'

for path, dirs, files in os.walk(master):
  for c in files:
    tt = c[-3:]
    if tt == "mp4" and path == master:  
        file_counter2+=1
    

notes_file.write('[ \n')
for path, dirs, files in os.walk(master):
  for f in files:
    print(str(file_counter2) + "**len of F**")
    q = path + '\\' + f + " " + "\n"
    #qt = st1+f+st2+st3+f+st4 
    tt = f[-3:]
    
    if tt == "mp4" and path == master:
        file_counter+=1
        notes_file.write('   { \n')
        notes_file.write('      "id":' + str(file_counter) +", \n")
        notes_file.write('      "filename":"' + f + '", \n')
        notes_file.write('      ' + star_string +'" \n')
        if file_counter < file_counter2:        
           notes_file.write('   }, \n')
        else:
           notes_file.write('   } \n')
        #jj.write(qt)
        #print(qt + " added to file ")
	


notes_file.write("]")
#jj.close()
notes_file.close()