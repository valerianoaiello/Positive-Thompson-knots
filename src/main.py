import numpy as np
from sympy.combinatorics import Permutation

#This function computes the permutation associated with the bottom tree of a positive Thompson element
#n is odd number
#This function returns a premutation on {0,1,...,n}
#https://docs.sympy.org/latest/modules/combinatorics/permutations.html
#conta l'ordine dei cicli (non disgiunti) nel numero finale di orbite?

def bottom_permutation(n: int) -> Permutation:
    if n%2==0:
        print('The number is even')
        exit(0)
    if n==1:
        p=Permutation(0, 1)
    elif n==3:
        p=Permutation(0, 2)(1, 3)
    else:
        q=Permutation(0, 2)
        m=int((n-3)/2)
        for i in range(m):
            q=Permutation(q(2*i+1,2*i+4))
        p=Permutation(q(n-2, n))
       
    return p


def top_permutation(n: int, v: np.array) -> Permutation:
    p=Permutation(size=n+1)
#    print(p.size)
#    print('v=',v)
    if n==1:
        p=Permutation(0, 1)
    elif n==3:
        p=Permutation(0, 2)(1, 3)
    else:
        w = np.nonzero(v)[0]
        a=w[0]#this is the index of the first non-zero entry in the vector v
        # v[a] is the value of the first non-zero entry in our vector v
        # print('w=', w, 'a=', a, 'b=', b, 'v[a]=', v[a])
        v[a]=v[a]-1
          #  print('v[a]=', v[a])
        m=n-2
        v_prime=v
          #  q=Permutation(a,a+2)
        p_prime=top_permutation(n-2, v_prime)

        z=p_prime.array_form 


        m=len(z)

        for i in range(m):
            if z[i]>i and z[i] >= a+2:
                print("(i, z[i]) = ", i, z[i])

                r=Permutation(i, z[i])
                s=Permutation(i,z[i]+2)
                z=list(z*r*s)

                
            elif z[i]==a+1:
                r=Permutation(i, z[i])
                s=Permutation(i,z[i]+1)
                z=list(z*r*s)

        q=Permutation(a+1,a+3)
        
        p_prime=list(q*Permutation(z))
        print("prova")
        p=p_prime
    return p
 
 






if __name__ == '__main__':
    print('inizio')
    p: Permutation =top_permutation(5, np.array([1, 0]))
    print('permutation = ', p)

