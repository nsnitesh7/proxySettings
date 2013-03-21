#str= "http://172.16.29.150:8080 https://172.16.29.150:8080"
#s="172.16.29.150:8080"
#t="172.16.29.120:2121"
#print str.replace(s,t)

import os

new=raw_input("Enter the new proxy : ")

os.system("echo $http_proxy > temp")
f1=open("temp","r")
current_proxy=f1.read()
old = current_proxy[7:]
f1.close()

os.system("rm temp")

#print new
#print old
old=old[:len(old)-1]

f1=open("/etc/bash.bashrc","r")
str=f1.read()
temp=str.replace(old,new)
f1.close()
f1=open("/etc/bash.bashrc","w")
f1.write(temp)
f1.close()

f2=open("/etc/apt/apt.conf","r")
str=f2.read()
temp=str.replace(old,new)
f2.close()
f2=open("/etc/apt/apt.conf","w")
f2.write(temp)
f2.close()

f3=open("/etc/wgetrc","r")
str=f3.read()
temp=str.replace(old,new)
f3.close()
f3=open("/etc/wgetrc","w")
f3.write(temp)
f3.close()
