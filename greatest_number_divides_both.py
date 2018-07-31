# greatest_number_divides_both
def main():
    pass
    n=list(map(int,input().split()))
    list_1=[]
    list_2=[]
    list_3=[]
    for num in range(1,n[0]+1):
            if(n[0]%num==0):
                list_1.append(num)
    for num2 in range(1,n[1]+1):
            if(n[1]%num2==0):
                list_2.append(num2)
    for i in list_1:
        for j in list_2:
            if(i==j):
                list_3.append(i)
    print(max(list_3))
if __name__ == '__main__':
    main()
