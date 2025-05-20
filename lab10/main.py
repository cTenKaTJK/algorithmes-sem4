'''
Задача о бросании яиц: Дано 100-этажное здание. Если яйцо сбросить с высоты N-го этажа
(или с большей высоты),оно разобьется. Если его бросить с любого меньшего этажа, оно не разобьется.
У вас есть два яйца. Найдите N за минимальное количество бросков.
'''
from functools import lru_cache

def aritmetical(eggs, floors):
    aritmetical_sum, drop = 0, 0
    while aritmetical_sum < floors:
        drop += 1
        aritmetical_sum += drop
    return drop


@lru_cache()
def recursive(eggs, floors):
    def throw(eggs, tryes):
        if eggs == 1:
            return tryes
        elif eggs >= tryes:
            return 2 ** eggs - 1
        else:
            return throw(eggs - 1, tryes - 1) + 1 + throw(eggs, tryes - 1)
    
    result, count = 0, 0
    while result < floors:
        count += 1
        result = throw(eggs, count)
    return count


if __name__ == '__main__':
    eggs, floors = 2, 100
    print(aritmetical(eggs, floors), recursive(eggs, floors))