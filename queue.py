class Queue:

    def __init__(self):

        self.items = []



    def isEmpty(self):

        return self.items == []



    def enqueue(self,item):

        self.items.insert(0,item)



    def getList(self):

        return self.items





q=Queue()

q.enqueue("Ahmad")

q.enqueue("Riza")

q.enqueue("Tata")

print(q.getList())
