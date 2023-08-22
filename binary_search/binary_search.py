# Developer: ccz
# Time: 2023/8/21 17:50
'''#递归版本
def binary_search(alist,item):
    n = len(alist)
    if n>0:
        mid = n//2
        if alist[mid]==item:
            return True
        elif item < alist[mid]:
             return binary_search(alist[:mid],item)
        else:
             return binary_search(alist[mid+1:],item)
    return False
    '''
#非递归版本
def binary_search(alist,item):
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(binary_search(li,26))
    print(binary_search(li,100))

