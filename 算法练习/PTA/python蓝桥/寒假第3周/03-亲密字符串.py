def F(A,B):
    if len(A)!=len(B):
        return False
    idx = [i for i in range(len(A)) if A[i]!=B[i]]
    if len(idx) == 2 and A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]:
        return True
    if len(idx) == 0 and len(A)-len(set(A)) > 0:
        return True
    return  False

if __name__=="__main__":
    A = input()
    B = input()
    print(F(A,B))