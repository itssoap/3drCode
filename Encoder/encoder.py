import pyqrcode
import sys
import os
from Encoder.blend import blendr

color=[[0,255,255,255], #cyan
       [255,0,255,255], #magenta
       [255,255,0,255]] #yellow

bg=[0,0,0,0] #(r,g,b,a) scheme. Alpha channel for Bg is 0 for transparency
def outQR(a):
    i=0
    for data in a:
        #os.system("mkdir out")
        url=pyqrcode.create(data)
        file=os.path.join('',str(i+1)+'.png')
        url.png(file, scale=100, module_color=color[i], background=bg)
        i+=1

def encodr(text):
    #take data from console
    a=''.join(map(str,text)).encode('utf-8') #a=text.encode(encoding='utf-8') #select all the words if spaces in between and join them to make a string
    #Unicode-8 encoding in case data includes non-ASCII characters
    #print(a)
    n=int(len(a)/3) if (len(a)>=3) else int(len(a)) #define 'n'
    a=[a[i:i+n] for i in range(0, len(a), n)] #split string in 'n' equal parts
    #print(a)
    try: #if 4th part exist, merge it with 3rd part
        if len(a[3]):
            a[2]+=a[3]
            a.pop(3)
    except IndexError: #if it doesn't, leave the list as it is
        pass
    #print(a)
    #a=a[:].encode('utf-8')
    outQR(a)
    blendr()

