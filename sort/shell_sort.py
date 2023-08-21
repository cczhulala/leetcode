# Developer: ccz
# Time: 2023/8/18 17:24
def shell_sort(alist):
    '''希尔排序'''
    n=len(alist)
    gap=n // 2
    while gap>0:
        #控制全部子序列
        for j in range(gap,n):
            i=j
        #子序列中的插入排序
            while i>0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__=='__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    shell_sort(li)
    print(li)