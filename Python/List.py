if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        fun=input("")
        templ=fun.split()
        if templ[0]=='insert':
            list.insert(int(templ[1]),int(templ[2]))
        elif templ[0]=='print':
            print(list)
        elif templ[0]=='remove':
            list.remove(int(templ[1]))
        elif templ[0]=='append':
            list.append(int(templ[1]))
        elif templ[0]=='sort':
            list.sort()
        elif templ[0]=='pop':
            list.pop()
        elif templ[0]=='reverse':
            list.reverse()
        else:
            pass
