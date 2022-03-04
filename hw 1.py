import random
class Human:
    def __init__(self,id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def get_in_Queue(self):
        print(f'Hello, who last in queue?. I will follow you, my {self.id}')

    def registration(self):
        print(f'My id {self.id},im {self.name} {self.surname}')

    def talk_on_the_phone(self):
        print('Im talking on the phone')

    def __repr__(self):
        return (f'{self.name} {self.surname}')


class Queue:
    """Класс очреди"""
    def __init__(self):
        self.queue = []

    def len_queue(self): #длина очереди
        return len (self.queue)

    def count_human(self): #количество людей в очереди
        return self.queue == []

    def add_in_queue(self, human): #добавить людей в очередь
        self.queue.insert(1,human)

    def show(self):
        print(f'очердь: {self.queue}')

    def where(self):
        print('Люди стоят в очереди в МФЦ')

    def get_in_queue(self, human): # человек влезвет без очереди
        a = random.randrange(len(self.queue))
        print(self.queue[a], human)
        return self.queue.insert(a+1, human)


human1 = Human('24', 'Kate','Smirnova')
human2 = Human('13', 'Viktoria', 'Romanova')
human3 = Human('2365', 'Makar', 'Petrov')
human4 = Human('9375', 'Sacha', 'Syvorov')
human5 = Human('6368', 'Tatyana','Larina')

queue = Queue()
print(queue.count_human())

queue.add_in_queue(human4)
queue.add_in_queue(human2)
queue.add_in_queue(human3)
queue.add_in_queue(human5)
queue.add_in_queue(human1)
queue.show()
print(queue.len_queue())
queue.show()
queue.get_in_queue(human2)
queue.show()


