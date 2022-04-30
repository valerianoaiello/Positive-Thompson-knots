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
        a=len(w)-1# we find the index of the last non-zero entry in our vector v
        # v[a] is the value of the last non-zero entry in our vector v
        # print('w=', w, 'a=', a, 'b=', b, 'v[a]=', v[a])
        v[a]=v[a]-1
          #  print('v[a]=', v[a])
        m=n-2
        v_prime=v
          #  q=Permutation(a,a+2)
        p_prime=top_permutation(n-2, v_prime)
        print(p_prime.array_form)
        z=p_prime.array_form 
        print('z = ', type(z))
#        exit(0)
        m=len(z)
#        print(z)
        for i in range(m):
            if z[i]>=i and z[i] >= a+2:
                r=Permutation(i, z[i])
                s=Permutation(i,z[i]+2)
#                z[i]=z[i]+2
                z=Permutation(z*r*s)
                print(z)
            elif z[i]==a+1:
                r=Permutation(i, z[i])
                s=Permutation(i,z[i]+1)
#                z[i]=z[i]+2
                z=Permutation(z*r*s)
#                z[i]=i+1
                print(z)
#                r= Permutation(i,i+1)
 #               print(p_prime, r, '=')
  #              p_prime=Permutation(p_prime*r)
   #             print(p_prime)
        q=Permutation(a+1,a+3) 
        print(q, z, '=')
        p_prime=Permutation(q*z)
        print(p_prime)
        p=p_prime
    return p
 
 






if __name__ == '__main__':
    print('inizio')
    p: Permutation =top_permutation(5, np.array([1, 0]))
    print('permutation = ', p)

