f = open("test.txt",'r')

for line in f:
    line = line.decode('utf-8')
    print line

def 