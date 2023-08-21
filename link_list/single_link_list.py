# Developer: ccz
# Time: 2023/8/15 13:51
class Node:
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None
    pass
#node = Node(100)
class SingleLinkList:
    '''单链表'''
    def __init__(self,node = None):
        self.__head=node

    def is_empty(self):
        return self.__head == None
    def length(self):
        #cur游标，用来移动遍历节点
        cur = self.__head
        length=0
        while True:
            if cur!=None:
                length=length+1
                cur=cur.next
            else:
                break
        return length

    def travel(self):
        cur = self.__head
        list=[]
        while cur !=None:
            list.append(cur.elem)
            cur=cur.next
        return print(list)

    def add(self,item):
        '''头插法'''
        node=Node(item)
        node.next=self.__head
        self.__head=node
    def append(self,item):
        '''尾插法'''
        node=Node(item)
        cur=self.__head
        if self.is_empty():
            self.__head = node
            return
        while cur.next != None:
            cur=cur.next
        cur.next=node

    def insert(self, pos, item):
        #parm pos 从0开始
        node=Node(item)
        cur=self.__head
        count=0
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
        #当循环退出后，cur指向pos-1位置
            while count!=pos-1:
                cur=cur.next
                count=count+1
            node.next=cur.next
            cur.next=node
    def remove(self,item):
        cur=self.__head
        pre=None
        while cur != None:
            if cur.elem!=item:
                    pre=cur
                    cur=cur.next
            else:
                #判断是否为头结点
                if pre==None:
                    self.__head=cur.next
                    return
                else:
                    pre.next=cur.next
                    return



    def search(self,item):
        cur = self.__head
        count=0
        while cur != None:
            if cur.elem==item:
                return print('yes,pos is {}'.format(count))
            cur=cur.next
            count += 1
        return print('Can\'t find')


if __name__=="__main__":
    ll=SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.add(8)
    ll.travel()
    ll.insert(0,1)
    ll.insert(1,2)
    ll.insert(-1,-1)
    ll.insert(10,10)
    ll.travel()
    ll.search(11)
    ll.remove(-1)
    ll.travel()
    ll.remove(2)
    ll.travel()
    ll.remove(10)
    ll.travel()