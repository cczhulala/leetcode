# Developer: ccz
# Time: 2023/8/18 10:05
class Stack():
    def __init__(self):
        self.__list=[]
    def push(self,item):
        self.__list.append(item)
    def pop(self):
        return self.__list.pop()
    def peek(self):
        if self.is_empty(self):
            return None
        else:
            return self.__list[-1]
    def is_empty(self):
        return self.__list==[]
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s._Stack__list)
    print(s.pop())
    print(s._Stack__list)
    print(s.is_empty())
    print(s.size())

