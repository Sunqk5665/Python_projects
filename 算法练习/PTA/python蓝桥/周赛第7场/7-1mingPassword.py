count = 0
for i in range(9+1):
    for j in range(9+1):
        for k in range(9+1):
            if (31*10000+i*1000+j*100+k*10+k*1)%16==0 and (31*10000+i*1000+j*100+k*10+k*1)%46==0:
                print(("3"+"1"+str({})+str({})+str({})+str({})).format(i,j,k,k))
                count += 1
print(count)