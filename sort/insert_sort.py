# Developer: ccz
# Time: 2023/8/18 16:58
def insert_sort(alist):
    n=len(alist)
    #从右边第几个位置取出元素执行这样的过程
    for j in range(1,n):
        i=j
        #从右边的无序序列中取一个数目，即i位置的数目，然后将其插入到前面正确的位置中
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i -= 1
            else:
                break

if __name__=='__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    insert_sort(li)
    print(li)

