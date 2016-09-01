#! /usr/bin/python2.7
import os
def encrypt (text, key):
    if key == 1:
       return text

    rail=[]
    for row in range(key):
       rail.append('')

    row=0
    dir=1
    for ch in text:
       rail[row]=rail[row]+ch
       #print rail
       row=row+dir
       if row == key:
           dir=-1
           row=row-2
       if row == -1:
           dir=1
           row=row+2

    cipher=''
    for row in range(key):
       cipher=cipher+rail[row]

    return cipher


def decrypt(text, key):
 if key == 1:
       return text
 crail=[]
 for row in range(key):
       crail.append('')
 
 row=0
 dir=1
 for ch in text:
       crail[row]=crail[row]+ch
       row=row+dir
       if row == key:
           dir=-1
           row=row-2
       if row == -1:
           dir=1
           row=row+2    
 countRail=[]
 for row in range(key):
       countRail.append(0)
      
 for row in range(key):
       countRail[row]=len(crail[row])
       
     
 rail=[] 
 for row in range(key):
       rail.append([])
     
              
 begin=0
 for row in range(key):
       end=begin+countRail[row]
       rail[row]=list(text[begin:end])
       begin=end
       
  
 row=0
 txt=''
 dir=1
 for i in range (len(text)):
       txt=txt+rail[row].pop(0)
       row=row+dir
       if row == key:
           dir=-1
           row=row-2
       if row==-1:
           dir=1
           row=row+2
 return txt


filename=raw_input("please enter the filename : ")
key=input("please enter you secret key :")
mode=raw_input("encrypt or decrypt : ")
read= open(filename,"r+" )
lele=read.read().split("\n")
s=''
for m in lele:
        s+=m
        
read.close()
result1=encrypt(s, key)

result2=decrypt(s,key)
if mode == 'encrypt':
                os.rename(filename,"encrypted")
                write=open("encrypted","w+")
                write.write(result1)
else:
                os.rename("encrypted","test.txt")
                write=open("test.txt","w+")
                write.write(result2)


write.close()
print "Done.. "
