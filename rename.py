import os
def getnumb(n):
    if n.find('000', 0, 2)!=-1:
        return int(n[-1])
    elif n.find('00', 0, 1)!=-1:
        return int(n[2:])
    elif n[0]=='0':
        return int(n[1:])
    else:
        return int(n)
def getnumc(n):
    if len(n)==1:
        s = str("000")
        return s+n
    elif len(n)==2:
        s = str("00")
        return s+n
    elif len(n)==3:
        s = str("0")
        return s+n
    else:
        return n

def getnum(n):
    if len(str(n))==1:
        s = str("000")
        return s+str(n)
    elif len(str(n))==2:
        s = str("00")
        return s+str(n)
    elif len(str(n))==3:
        s = str("0")
        return s+str(n)
    else:
        return str(n)

# Function to rename multiple files
def main():
    i = 0
    c = 1162
    cx =os.listdir("E:\\fci19sec2\\graduation\\gehad\\taher\\taher1\\t2\\")

    for filename in cx:
        xc = filename.split('.')
        x=int(xc[0])+c
        dst = "ARAB NORM " + getnum(x) + ".wav"
        src = 'E:\\fci19sec2\\graduation\\gehad\\taher\\taher1\\t2\\' + filename
        dst = 'E:\\fci19sec2\\graduation\\gehad\\taher\\taher1\\t3\\' + dst


        # rename() function will
        # rename all the files
        os.rename(src, dst)



# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()