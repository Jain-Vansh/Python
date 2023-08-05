if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    w = []
    for i in range(0,1):
        for j in range(0,x+1):
            for k in range(0,y+1):
                for l in range(0,z+1):
                    sum = j+k+l
                    if(sum == n):
                        continue
                    else:
                        w.extend([[j,k,l]])
    print(w)
        

