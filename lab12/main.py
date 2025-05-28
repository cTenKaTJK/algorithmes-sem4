def ruksack(curr_weight, items, index, matr=dict()):
    # закончился вес или нечего добавить
    if index < 0 or curr_weight == 0:
        return 0
    
    # рассматриваемое значение уже встречалось при другом проходе рекурсии
    elif (index, curr_weight) in matr.keys():
        return matr[(index, curr_weight)]
    
    weight, cost = items[index]

    if weight > curr_weight:
        # что выгоднее положить очередной предмет или нет
        matr[((index, curr_weight))] = ruksack(curr_weight, items, index - 1, matr)
        return matr[((index, curr_weight))]
    
    matr[(index, curr_weight)] = max(ruksack(curr_weight, items, index - 1, matr), cost + ruksack(curr_weight - weight, items, index - 1, matr))

    return matr[(index, curr_weight)]
    



if __name__ == '__main__':
    max_weight = 10
    # (масса, ценность)
    items = [
        (3, 20), (4, 30), (1, 15), (2, 30), (5, 60)
    ]
    print(ruksack(max_weight, items, len(items) - 1))