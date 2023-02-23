class Queue:
    def __init__(self):
        self.__num = []

    def put(self, elem):
        self.__num.append(elem)

    def get(self):
        val = self.__num[0]
        del self.__num[0]
        return val


class QueueError(IndexError):  # Choose base class for the new exception.
    pass

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except IndexError:
    print("Queue error")
