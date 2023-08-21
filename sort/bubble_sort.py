# Developer: ccz
# Time: 2023/8/18 15:09
def bubble_sort(alist):
    '''冒泡排序'''
    for j in range(0,len(alist)):
        for i in range(0, len(alist)-j-1):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

if __name__=='__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    bubble_sort(li)
    print(li)


