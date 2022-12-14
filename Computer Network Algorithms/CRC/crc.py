def crc():
    st=list(input("Enter the string\n"))
    a=list(''.join(format(ord(i),'08b')for i in st))
    c=[int(i)for i in a]
    m=len(a)
    k=[1,1,0,1]
    n=len(k)
    for i in range(m-n):
        for j in range(n):
            c[i+j]=c[i+j]^k[j]
    code=c[-3:]
    print("\nCode word is " + str(code))
    a.extend(code)
    print("\nFinal encoded bit is " + (''.join([str(i) for i in a])))
    
crc()
