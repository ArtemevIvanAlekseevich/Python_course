class Buffer:

    def __init__(self):
        # конструктор без аргументов
        self.lst = []

    def add(self, *a):
        # добавить следующую часть последовательности
        for i in a:
            self.lst.append(i)
        while len(self.lst) >= 5:
            sum = 0
            for j in range(5):
                sum += self.lst[0]
                del self.lst[0]
            print(sum)       

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
        return self.lst

