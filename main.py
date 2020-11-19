import pyqrcode
import sys

color=[[0,255,255,255],
       [255,0,255,255],
       [255,255,0,255]]
def outQR(a):
    i=0
    for data in a:
        url=pyqrcode.create(data)
        with open(str(i)+'.png','w') as fstream:
            url.png()

if __name__ == "__main__":
    #take data from console
    a=' '.join(map(str,sys.argv[1:])).encode('utf-8') #select all the words if spaces in between and join them to make a string
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
    #a=a[:].encode('utf-8')
    print(a[:])
    