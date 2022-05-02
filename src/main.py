import numpy as np
from sympy.combinatorics import Permutation

#This function computes the permutation associated with the bottom tree of a positive Thompson element
#n is odd number
#This function returns a premutation on {0,1,...,n}
#https://docs.sympy.org/latest/modules/combinatorics/permutations.html
#conta l'ordine dei cicli (non disgiunti) nel numero finale di orbite?
#in realtà n è un parametro superfluo della funzione top permutation

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


#this function works for F_{3,+}, in order to use it for F_+ the components of the vector v with odd
#indices must be zero
def top_permutation(n, v):
    if n%2==0:
        print('The number is even')
        exit(0)
    if n==1:
        p=[1,0]
    elif n==3:
        p=[2,3,0,1]
    else:
        z = np.nonzero(v)[0]#vector containing the indices of the non-zero components of v
        k=len(z)
        a=z[k-1]#this is the index of the last non-zero entry in the vector v
        # v[a] is the value of the first non-zero entry in our vector v
        v[a]=v[a]-1

        v_prime=v
        w=top_permutation(n-2, v_prime)
        p=np.zeros(n+1)
        for i in range(n-1):
            if i <= a and w[i]<=a:
                p[i]=w[i]
            elif i <= a and w[i]==a+1:
                p[i]=w[i]+1
                print("i=",i,"p[i]=", p[i],"case 1")
            elif i <= a and w[i]>=a+2:
                p[i]=w[i]+2
                print("i=",i,"p[i]=", p[i],"case 2")
            elif i >= a+2 and w[i]>=a+2:
                p[i+2]=w[i]+2
                print("i=",i,"p[i+2]=", p[i],"case 3")
            elif i >= a+2 and w[i]<=a:
                p[i+2]=w[i]                
                print("i=",i,"p[i+2]=", p[i+2],"case 4")
            elif i >= a+2 and w[i]==a+1:
                p[i+2]=a+2
                print("i=",i,"p[i]=", p[i+2],"case 5")
            elif i == a+1 and w[i]>=a+2:
                p[i+1]=w[i]+2
                print("i=",i,"p[i]=", p[i],"case 6")
            elif i == a+1 and w[i]<=a:
                p[i+1]=w[i]
                print("i=",i,"p[i+1]=", p[i],"case 7") 
        p[a+1]=a+3
        p[a+3]=a+1
    return p


if __name__ == '__main__':
    p=top_permutation(7, [1,0,1,0])
    p=Permutation(p)
    p=top_permutation(5, [0,1,0])
    p=Permutation(p)
    print('permutation = ', p)
    p: Permutation =top_permutation(1, np.zeros(3))
    print('permutation = ', p)

    # p_prime=Permutation(1, 3)
    # z=p_prime.array_form 
    # print("z=",p_prime)
    # r=Permutation(1, z[0])
    # z=list(z*r)
    # print("r=",r, "zr=", Permutation(z))
