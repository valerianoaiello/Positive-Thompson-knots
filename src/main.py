from sympy.combinatorics import Permutation

#This function computes the permutation associated with the bottom tree of a positive Thompson element
#n is odd number
#This function returns a premutation on {0,1,...,n}

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

if __name__ == '__main__':
    print(bottom_permutation(5))
    print(bottom_permutation(7))