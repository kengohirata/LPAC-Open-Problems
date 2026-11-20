"""Finite GF(2) sanity checks for the source-splitting criterion.
This is not a proof of the infinite-dimensional theorem.
"""
import numpy as np

rng=np.random.default_rng(48291)

def rank(a):
    a=np.array(a,dtype=np.uint8).copy()%2
    nr,nc=a.shape
    r=0
    for j in range(nc):
        piv=next((i for i in range(r,nr) if a[i,j]),None)
        if piv is None: continue
        a[[r,piv]]=a[[piv,r]]
        for i in range(nr):
            if i!=r and a[i,j]: a[i]^=a[r]
        r+=1
        if r==nr: break
    return r

def null(a):
    a=np.array(a,dtype=np.uint8).copy()%2
    nr,nc=a.shape
    r=0; piv=[]
    for j in range(nc):
        p=next((i for i in range(r,nr) if a[i,j]),None)
        if p is None: continue
        a[[r,p]]=a[[p,r]]
        for i in range(nr):
            if i!=r and a[i,j]: a[i]^=a[r]
        piv.append(j);r+=1
        if r==nr: break
    free=[j for j in range(nc) if j not in piv]
    out=np.zeros((nc,len(free)),dtype=np.uint8)
    for k,j in enumerate(free):
        out[j,k]=1
        for i,p in enumerate(piv): out[p,k]=a[i,j]
    return out

def make_complex(N=4):
    # Split normal form: C_n=B_n + H_n + B_{n-1}.
    hs=rng.integers(0,3,size=N)
    bs=np.r_[rng.integers(0,3,size=N-1),0]
    ds=[int(bs[n]+hs[n]+(bs[n-1] if n else 0)) for n in range(N)]
    dif=[np.zeros((0,ds[0]),dtype=np.uint8)]
    for n in range(1,N):
        d=np.zeros((ds[n-1],ds[n]),dtype=np.uint8)
        b=int(bs[n-1]);start=int(bs[n]+hs[n])
        d[:b,start:start+b]=np.eye(b,dtype=np.uint8)
        dif.append(d)
    return ds,dif

def hom_basis(C,D):
    cd,cb=C; dd,db=D;N=len(cd)
    offs=np.cumsum([0]+[cd[n]*dd[n] for n in range(N)])
    nv=int(offs[-1]); rows=[]
    # d_D[n] a_n - a_{n-1} d_C[n] = 0.
    for n in range(1,N):
        for i in range(dd[n-1]):
            for j in range(cd[n]):
                row=np.zeros(nv,dtype=np.uint8)
                for k in range(dd[n]):
                    row[offs[n]+k*cd[n]+j]^=db[n][i,k]
                for k in range(cd[n-1]):
                    row[offs[n-1]+i*cd[n-1]+k]^=cb[n][k,j]
                rows.append(row)
    mat=np.array(rows,dtype=np.uint8).reshape((len(rows),nv))
    return null(mat),offs

def mats(v,C,D,offs):
    return [v[offs[n]:offs[n+1]].reshape(D[0][n],C[0][n]) for n in range(len(C[0]))]

def sample_map(C,D):
    bas,offs=hom_basis(C,D)
    v=bas@rng.integers(0,2,size=bas.shape[1],dtype=np.uint8)%2
    return mats(v,C,D,offs)

def check(C,U,V,f):
    bu,ou=hom_basis(C,U);bv,ov=hom_basis(C,V)
    images=[]
    for j in range(bu.shape[1]):
        aa=mats(bu[:,j],C,U,ou)
        images.append(np.concatenate([(f[n]@aa[n]%2).ravel() for n in range(len(f))]))
    mat=np.array(images,dtype=np.uint8).T if images else np.zeros((int(ov[-1]),0),dtype=np.uint8)
    actual=(rank(mat)==bu.shape[1]==bv.shape[1])
    expected=True
    for n in range(len(f)):
        zu=null(U[1][n]);zv=null(V[1][n])
        z_iso=(rank(f[n]@zu%2)==zu.shape[1]==zv.shape[1])
        hn=C[0][n]-rank(C[1][n])-(rank(C[1][n+1]) if n+1<len(f) else 0)
        if hn and not z_iso: expected=False
        if n and rank(C[1][n]) and not(rank(f[n])==U[0][n]==V[0][n]):
            expected=False
    return actual==expected

for j in range(300):
    C=make_complex();U=make_complex();V=make_complex();f=sample_map(U,V)
    assert check(C,U,V,f),f'failure in test {j}'
print('300 exact GF(2) checks passed (four degrees; random split complexes and chain maps).')
