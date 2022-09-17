# Given a list of values how will you find the kth biggest element in the list

# sample input
# 5
# 12,34,56,22,57
# 3

# sample output:
# 34

def kthSmallest(arr, N, K):
    arr=set(arr)
    arr=list(arr)
    arr.sort()
    return arr[K-1]
if __name__ == '__main__':
    e=input()
    ar=input().split(",")
    arr=list(map(int,ar))
    N = len(arr)
    K = int(input())
    print(kthSmallest(arr, N, K))