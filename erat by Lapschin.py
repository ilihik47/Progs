import pickle
def erat(n):
    s=set(range(2,n+1))
    f=open('erat.data','bw')
    pp=[]
    while s:
        p=min(s)
        pp.append(p)
        s-=set(range(p,n+1,p))
    pickle.dump(pp,f)
    f.close()
    return(pp)
print(erat(20))