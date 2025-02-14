from random import choice, random

first = 'Мама мыла раму'
second = 'Рамена мало было'
eqv = lambda x, y: x == y
print(list(map(eqv, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='UTF-8')
        for s in data_set:
            file.write(str(s))
            file.write('\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

