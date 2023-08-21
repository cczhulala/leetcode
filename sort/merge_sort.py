# Developer: ccz
# Time: 2023/8/21 14:25

def merge_sort(alist):
    n=len(alist)
    mid = n//2
    if n<=1:
        return alist
    #left 采用归并排序后返回的有序的新列表
    left_li=merge_sort(alist[:mid])
    #right相同
    right_li=merge_sort(alist[mid:])
    #merge(left,right)
    left_pointer, right_pointer = 0 ,0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        #小于等于是为了保证稳定性
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)

    print(merge_sort(li))