if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrnew=[]
    for i in arr:
        arrnew.append(i)
    
    arrnew.sort()
    for i in range(len(arrnew)-1,0,-1):
        if arrnew[i]>arrnew[i-1]:
            print(arrnew[i-1])
            break
