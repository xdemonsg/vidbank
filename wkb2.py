import os
master = os.getcwd()

with open('file.txt','w') as h:
    h.write("")    

jj = open("wankbank.html", "a")
st1='<video width="320" height="240" controls><source src="'
st2='" type="video/mp4"></video>' 


for path, dirs, files in os.walk(master):
  for f in files:
    q = path + '\\' + f + " " + "\n"
    qt = st1+f+st2 
    tt = f[-3:]
    
    if tt == "mp4" and path == master:
        jj.write(qt)
        print(qt + " added to file ")



jj.close()