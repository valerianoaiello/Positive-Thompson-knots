import numpy as np
from sympy.combinatorics import Permutation

#Go to https://docs.sympy.org/latest/modules/combinatorics/permutations.html
#for more information on Permutation
"""
v = (v_1, v_2, ..., v_n)
0 <= v_i < m, v_i in N, for every i
"""
def generate_vectors(n: int, m: int) -> np.ndarray:
    v = list(range(m))
    l = [v for i in range(n)]

    w = np.array(np.meshgrid(*l)).T.reshape(-1, n)
    return w


#this function find the number of leaves in the reduced binary tree representing an element in F_+
def number_leaves_binary(v: np.array)->int:
    n=(number_leaves_ternary(v)+1)/2
    return n

#this function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}
def number_leaves_ternary(v: np.array)->int:
    z = np.nonzero(v)[0]#vector containing the indices of the non-zero components of v
    k=len(z)
    a=z[k-1]#this is the index of the last non-zero entry in the vector v
    # v[a] is the value of the first non-zero entry in our vector v
 #   print("k=",k, "a=", a, "v[a]=", v[a])
    if k==0:
        n=1
    elif k==1 and v[a]==1 and a%2==0:
        n=a+5
    elif k==1 and v[a]==1 and a%2==1:
        n=a+4
    else:
        v[a]=v[a]-1
        n=number_leaves_ternary(v)+2
#        print("n=",n)
    return n

#This function computes the permutation associated with the bottom tree of a positive Thompson element
#n is odd number and the permutation acts on {0,1,...,n}
def bottom_permutation(n: int) -> np.ndarray:
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
       
    return np.array(p.array_form)


#This function computes the permutation associated with the top tree of a positive Thompson element
#n is odd number and the permutation acts on {0,1,...,n}
def top_permutation(n: int, v: np.array) -> np.ndarray:
    if n%2==0:
        print('The number is even')
        exit(0)
    if n==1:
        p=np.array([1,0])
    elif n==3:
        p=np.array([2,3,0,1])
    elif n>=5 and not np.any(v):
        p=bottom_permutation(n)
    else:
        z = np.nonzero(v)[0]#vector containing the indices of the non-zero components of v
        k=len(z)
#        print('k',k)
        a=z[k-1]#this is the index of the last non-zero entry in the vector v
        # v[a] is the value of the first non-zero entry in our vector v
        v[a]=v[a]-1

        v_prime=v
        w=top_permutation(n-2, v_prime)
        p=np.zeros(n+1).astype(int)
        for i in range(n-1):
            if i <= a and w[i]<=a:
                p[i]=w[i]
            elif i <= a and w[i]==a+1:
                p[i]=w[i]+1
   #             print("i=",i,"p[i]=", p[i],"case 1")
            elif i <= a and w[i]>=a+2:
                p[i]=w[i]+2
   #             print("i=",i,"p[i]=", p[i],"case 2")
            elif i >= a+2 and w[i]>=a+2:
                p[i+2]=w[i]+2
  #              print("i=",i,"p[i+2]=", p[i],"case 3")
            elif i >= a+2 and w[i]<=a:
                p[i+2]=w[i]                
 #               print("i=",i,"p[i+2]=", p[i+2],"case 4")
            elif i >= a+2 and w[i]==a+1:
                p[i+2]=a+2
#                print("i=",i,"p[i]=", p[i+2],"case 5")
            elif i == a+1 and w[i]>=a+2:
                p[i+1]=w[i]+2
 #               print("i=",i,"p[i]=", p[i],"case 6")
            elif i == a+1 and w[i]<=a:
                p[i+1]=w[i]
 #               print("i=",i,"p[i+1]=", p[i],"case 7") 
        p[a+1]=a+3
        p[a+3]=a+1
    return p

 #if __name__ == '__main__':


def whole_permutation(n: int, v: np.array) -> np.ndarray:
    p = top_permutation(n, v)
    q = bottom_permutation(n)
    print("P: ", p)
    print("Q: ", q)
    
    v: list = []
    i=0
    while True:
        if p[i] not in v:       
            v.append(p[i])
            print('p[',i,']',p[i])
            i=p[i]
            if q[i] not in v:
                v.append(q[i])
                print('q[',i,']',q[i])
                i=q[i]
            else:
                break
        else:
            break

    # i=0
    # i=p[i]
    #     i=q[i]
    # while i != 0:
    #     if p[i] not in v:
    #         v.append(p[i])
    #         if q[p[i]] not in v:
    #             v.append(q[p[i]])
    #             i=q[p[i]]
    #             print('ciaone1')
    #         else:
    #             i=p[i]
    #             print('ciaone2')
    #     print('ciao')

    # secret_word = "python"
    # counter = 0

    # while True:
    #     word = input("Enter the secret word: ").lower()
    #     counter = counter + 1
    #     if word == secret_word:
    #         break
    return v



if __name__ == '__main__':
    r=whole_permutation(5, np.array([1, 0, 0]))
    print(r)
    
