n = input().split()
z1 = eval(n[0] + '+' + n[1] + 'j')
# z1 = eval('1'+'+'+'2')
# print(n)
# print(z1)
z2 = eval(n[2] + '+' + n[3] + 'j')

add = z1 + z2
sub = z1 - z2
mul = z1 * z2
div = z1 / z2

q = [add,sub,mul,div]
ls = sorted(q,key=lambda x:(x.real,-x.imag),reverse=True)

lsl=[z1,z2,add,sub,mul,div,ls[0]]
for c in lsl:
    if int(c.real)==0:  # 实部为 0
        if int(c.imag)==0:
            print("{0}")
        else:
            print("{",end='')
            print("{:.0f}i".format(c.imag),end='')
            print("}")
    else:
        if int(c.imag)==0:
            print("{",end='')
            print("{:.0f}".format(c.real),end='')
            print("}")
        elif int(c.imag)>0:
            print("{",end='')
            print("{:.0f}+{:.0f}i".format(c.real,c.imag),end='')
            print("}")
        else:
            print("{",end='')
            print("{:.0f}{:.0f}i".format(c.real,c.imag),end='')
            print("}")



q = [1+2j,1-1j,2+1j,3-5j,3-4j]
ls=sorted(q,key=lambda x:(x.real,-x.imag),reverse=True)
print(ls)
# print("{:.0f}".format(2.111))