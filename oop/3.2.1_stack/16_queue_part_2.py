class Queue:
    def __init__(self):
        self.__num = []

    def put(self, elem):
        self.__num.append(elem)

    def get(self):
        val = self.__num[0]
        del self.__num[0]
        return val

    def get_length(self):
        return len(self.__num)

class SuperQueue(Queue):

    def isempty(self):
        if Queue.get_length(self) > 0:
            return False
        else:
            return True


class QueueError(IndexError):  # Choose base class for the new exception.
    pass


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
