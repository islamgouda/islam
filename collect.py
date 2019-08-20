from phonetise-Arabic import phonetise
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

with open('metadata-Copy.csv', encoding='utf8') as f:
 with open('hhh.txt', 'w', encoding='utf8') as m:
    c = 1163
    while True:
       line = f.readline()
       if not line:
           break


       x = line.split(',')
       phonemes = phonetise(x[1])
       s = str("000")
       line = x[0]+','+' '+x[1]
       c += 1
       m.writelines(line)
f.close()