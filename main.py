# http://numbers.computation.free.fr/Constants/Algorithms/nthdecimaldigit.pdf

import math

def compute(n: int) -> float:
    assert(n>=2)
    n0=min(n//4,15)
    M=2*int(math.ceil(n/pow(math.log(n),3)))
    N=int(math.ceil((n+n0+1)*math.log(10)/math.log(2*math.e*M)))
    b=0.0
    for k in range((M+1)*N):
        mod=2*k+1
        x=pow(10,n,mod)
        x*=4
        x%=mod
        if k%2:
            b-=x/mod
        else:
            b+=x/mod
    def modinv(a: int, b: int) -> int:
        p=b
        x0,y0,x1,y1=1,0,0,1
        while b:
            q,a,b=a//b,b,a % b
            x0,x1=x1,x0-q*x1
            y0,y1=y1,y0-q*y1
        assert(a==1)
        x0%=p
        return x0
    c=0.0
    for k in range(N):
        mod=2*M*N+2*k+1
        A=1
        B=1
        C=1
        R=1
        m=mod
        P=[]
        for j in range(3,k+1,2):
            if m%j==0:
                P.append(j)
                while m%j==0:
                    m//=j
        for j in range(1,k+1):
            aa=N-j+1
            bb=j
            for p in P:
                while aa%p==0:
                    aa//=p
                    R*=p
                while bb%p==0:
                    bb//=p
                    R//=p
            A*=aa
            A%=mod
            B*=bb
            B%=mod
            C*=bb
            C%=mod
            C+=A*R
            C%=mod
        x=C
        x*=modinv(B,mod)
        x%=mod
        if n-N+2<0:
            y=pow(5,n,mod)
            y*=pow(modinv(2,mod),-(n-N+2),mod)
        else:
            y=pow(5,n,mod)
            y*=pow(2,n-N+2,mod)
        y%=mod
        y*=x
        y%=mod
        if k%2:
            c-=y/mod
        else:
            c+=y/mod
    return (b-c)-math.floor(b-c)

NMAX=int(input())
print("3.")
print("14", end="")
for n in range(2,NMAX):
    if n%10==0:
        print("")
    print(int((compute(n)*10)), end="")
print("")
