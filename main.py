"""
3dr-Code v1.0

Aim: To increase the amount of data stored per unit area in a QR code using colors and multiplexing technique.

"""

from time import sleep
from Encoder.encoder import encodr
from Decoder.scanner import ipcam

def main():
    choice=int(input("1. Decode\n2. Encode\nEnter your choice: "))
    if choice==1:
        ipcam()
        pass
    else:
        print("Initiating encoder...")
        sleep(0.5)
        print("Enter the data: ")
    
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        text = '\n'.join(lines)
        #print(text)
        encodr(text)
    
if __name__=='__main__':
    main()
