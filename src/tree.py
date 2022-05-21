from turtle import shape
import numpy as np
from sklearn.metrics import v_measure_score
from sympy.combinatorics import Permutation

#Go to https://docs.sympy.org/latest/modules/combinatorics/permutations.html
#for more information on Permutation
"""
v = (v_1, v_2, ..., v_n)
0 <= v_i < m, v_i in N, for every i
"""



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
def top_permutation(n: int, v: np.ndarray) -> np.ndarray:
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
        v_prime=v.copy()
        v_prime[a]=v_prime[a]-1
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

 
def whole_permutation(n: int, v: np.ndarray) -> np.ndarray:
    p = top_permutation(n, v)
    q = bottom_permutation(n) 
    
    tot = []
    
    for i in range(n):
        l: list = []
        if i not in [item for sublist in tot for item in sublist]:
            while True:
                if p[i] not in l:       
                    l.append(p[i])
                    i=p[i]
                    if q[i] not in l:
                        l.append(q[i])
                        i=q[i]
                    else:
                        break
                else:
                    break
            tot.append(l)
    return tot


#this function find the number of leaves in the reduced binary tree representing an element in F_+
def number_leaves_binary(v: np.ndarray)->int:
    n=(number_leaves_ternary(v)+1)/2
    return n

#this function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}
def number_leaves_ternary(v: np.ndarray)->int:
    z = np.nonzero(v)[0]#vector containing the indices of the non-zero components of v
    k=len(z)   
    m=1000#maximal length
    # for i in range(k):
    #     m = m + i+3*v[z[i]]
    w=np.array(list(range(m)))
    u=w.copy()
    for i in range(k-1,-1,-1):
        for j in range(v[z[i]]):
            w=np.delete(w,z[i]+1)
            w=np.delete(w,z[i]+1)
    n=0
    for i in range(len(w)-1):
#        print('w[',i,']=',w[i],'u[',i,']=',u[i], 'w[',i,']-u[',i,']=',w[i]-u[i])
        if w[i+1]-w[i]>=2:
            n=w[i+1]
#    print('cont=',cont,'n=', n)
    if n%2==1:
        n=n+2
    else:
         n=n+1
    return n

def generate_vectors(vector_width: int, vector_height: int) -> np.ndarray:
    v = list(range(vector_height))
    l = [v for i in range(vector_width)]

    w = np.array(np.meshgrid(*l)).T.reshape(-1, vector_width)
    w = w[(w[:, 0] != 0) | (w[:, 1] != 0)]

    return w

def random_generate_vectors(vector_number: int, vector_height: int, vector_width: int) -> np.ndarray:
    vector_matrix: np.ndarray = np.random.randint(vector_height, size=(vector_number, vector_width))
    vector_matrix = vector_matrix[(vector_matrix[:, 0] != 0) | (vector_matrix[:, 1] != 0)]
    return vector_matrix

if __name__ == '__main__':
    # print(generate_vectors(5,2).shape)
    A = random_generate_vectors(1000000, 10, 10)
    # A = np.array([[1, 1], [2, 2], [3, 3]])
    # A = A[(A[:, 1] == 1) | (A[:, 0] == 2)]
    print(A)
#     a = np.array([[1, 1], [2, 2], [3, 3]])
#     print(a.shape)
#     b=np.array([[5], [6],[7]])
#     print(b.shape)
#     c=np.hstack((a,b))
#     print(b)

# #    a=np.array([[[5], [6],[7]], a])
#     print(c)
    # n=3
    # l = []
    # for i in range(n): 
    #     for j in range(n):
    #         l.insert(1,i)
    #         l.insert(1,j)
    # print(l)
    # n1, n2 = (2, 4)
    # a = np.linspace(0, 2, n1).astype(int)
    # print('a',a)
    # b = np.linspace(0, 3, n2).astype(int)
    # print('b',b)
    # aa, bb = np.meshgrid(*a)
    # print(aa.astype(int))
    # print(bb.astype(int))


    # k=3
    # v=np.array([1,1, 0, 0, 0, 0])
    # n=number_leaves_ternary(v)
    # print('v=',v,'n=',n)
    # v=np.array([0,1, 0, 0, 0, 0])
    # n=number_leaves_ternary(v)
    # print('v=',v,'n=',n)
    # v=np.array([1, 0, 0, 0, 0])
    # n=number_leaves_ternary(v)
    # print('v=',v,'n=',n)
    # v=np.array([0,0,0,0,1, 0, 0, 0, 0])
    # n=number_leaves_ternary(v)
    # v=np.array([0,0,1, 0, 0, 1, 0])
    # n=number_leaves_ternary(v)
    # print('v=',v,'n=',n)

    # v=np.array([0, 0,0, 0,0, 0,1, 0, 0, 0, 0])
    # n=number_leaves_ternary(v)
    # print('v=',v,'n=',n)
    # # v=np.array([1, 0, 0, 0, 0])
    # # print('v=',v)
    # # n=number_leaves_ternary(v)
    # # print('v',v,'n',n)


    # # w = np.array([0, 0, 1])
    # # print(f"W={w}")
    # # r=whole_permutation(5, w)
    # # print(f"W={w}")
    # # print(f"PERMUTATION = {r}")
    # # r=whole_permutation_2(5, w)
    # # print(f"W={w}")
    # # print(f"PERMUTATION 2 = {r}")
    # # v=np.array([0, 1, 0, 0, 0, 0, 0, 1])
    # # n=number_leaves_ternary(v)
    # # print('n',n)
    # # v=np.array([1, 1, 0, 0, 0, 0, 0])
    # # n=number_leaves_ternary(v)
    # # print('v',v,'n',n)
    # # v=np.array([2, 1, 0, 0, 0, 0, 0])
    # # n=number_leaves_ternary(v)
    # # print('v',v,'n',n)
    # # v=np.array([0, 0, 0, 0, 1, 0, 0])
    # # n=number_leaves_ternary(v)
    # # print('v',v,'n',n)
    # # v=np.array([0, 1, 0, 0, 1, 0, 0])
    # # n=number_leaves_ternary(v)
    # # print('v',v,'n',n)