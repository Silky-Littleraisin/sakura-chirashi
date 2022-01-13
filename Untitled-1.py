from abc import abstractclassmethod
import re
from base64 import b64decode as bd
import urllib.request, urllib.parse, importlib, socket, random, base64, json, time, sys, os
import ast
import chardet


def OOOOO(s):
    return base64.b64encode(s.encode(encoding='utf-8'))
def OOOO0(b):
    return base64.b64encode(b)
def OOO0O(b):
    return base64.b64decode(b).decode(encoding='utf_32')
def OOO01(b):
    return base64.b64decode(base64.b64decode(b).decode(encoding='utf_32'))
def OOO00(b):
    return base64.b64decode(b)


a =[]
# with open("ce3.py") as obj:
  #   a = obj.readlines()
# htre=re.compile("(.*)[\(,\,](.*?\(b'.+?'\))(.*)")
htre=re.compile("(.*)eval\((b'[a-zA-Z]+?.+?')\)(.*)")
for n,b in enumerate(a):
    #continue
    h1 = htre.match(b)
    if h1!=None:
        pass
        print("#############################")
    
        # print(h1.group(2))
      #   print('"'+h1.group(2)+'"')
      #   print( bytes([ord(char) for char in h1.group(2)[2:-1]]))
        print(type(bytes([ord(char) for char in h1.group(2)[2:-1]])))
        print(chardet.detect(bytes([ord(char) for char in h1.group(2)[2:-1]][20:])))
        print(chardet.detect(base64.b64decode(bytes([ord(char) for char in h1.group(2)[2:-1]][20:]))))
        print(chardet.detect(base64.b64decode(bytes([ord(char) for char in h1.group(2)[2:-1]]))))

       #  print(OOO01(bytes([ord(char) for char in h1.group(2)[2:-1]])))
        # print(OOOO0(h1.group(2)))
      #   print(OOOOO(h1.group(2)))
      #   asss=OOOOO(h1.group(2))
      #   break
        
        # if type(eval(h1.group(2))) is bytes:
        #     print(eval(h1.group(2)).decode('utf-8'))
        # else:
        #     print(eval(h1.group(2)))

        # if type(eval(h1.group(2))) is bytes:
        #     a[n]=b.replace(h1.group(2),eval(h1.group(2)).decode('utf-8'))
        # else:
       #  a[n]=b.replace(h1.group(2),OOO0O(bytes([ord(char) for char in h1.group(2)[2:-1]])))

        # print(a[n])


        # print("#############################")

assss=b"aHR0cHM6Ly93d3cuY2diM2QuY29tLw=="


print(os.path.basename(os.path.dirname(__file__)))
print(type(assss))

# print(OOO0O(assss))
print(OOO00(assss))
print(OOOO0(assss))
print(OOOOO(assss))


with open("ce4.py","w") as obj:
    
    obj.writelines(a)

