if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max1 = max(arr)
    max2 = -100
    for i in range(0,len(arr)):
        if(arr[i]>max2 and arr[i]<max1):
            max2 = arr[i]
    print(max2)