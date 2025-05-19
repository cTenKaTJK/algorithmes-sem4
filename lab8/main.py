def moneyback(cash, nominals):
    line = [0] * (cash + 1)
    print('m |', *range(cash + 1))
    for coin in nominals:
        prev_line = line
        line = [1] + [0] * cash
        for subcash in range(1, cash + 1):

            if subcash >= coin:
                line[subcash] = prev_line[subcash] + line[subcash - coin]
            else:
                line[subcash] = prev_line[subcash]
            
        print(f'{coin} |', *line)
    return line[-1]


if __name__ == '__main__':
    cash = int(input('сумма:\t'))
    nominals = list(map(int, input('доступные монеты:\t').split()))
    nominals.sort()
    answer = moneyback(cash, nominals)
    print(f'ОТВЕТ: {answer}')
