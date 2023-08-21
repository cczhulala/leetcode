# Developer: ccz
# Time: 2023/8/21 10:49
#核心是递归和嵌套

def quick_sort(alist,first,last):
    if first >= last:
        return

    #n=len(alist)
    mid_value = alist[first]
    #low=0
    #high=n-1
    low=first
    high=last
    while low<high:
        # 从右往左一直走
        #把中间值放到一边判断
        while low<high and alist[high]>=mid_value:
                high -= 1
        alist[low]=alist[high]
        #防止错过
        #low += 1
        # 从左往右一直走
        while low<high and alist[low]<mid_value:
                low += 1
        alist[high]=alist[low]
        #防止错过
        #high -= 1
    #从循环退出时 low = high
    alist[low] = mid_value

    #对low左边的进行排序
    #不能用切片，因为切片相当于copy
    quick_sort(alist,first,low-1)
    #对low右边的进行排序
    quick_sort(alist,low+1,last)

if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)