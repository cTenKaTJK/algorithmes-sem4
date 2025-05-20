from functools import lru_cache


def voyage(matrix):
    rows, cols = len(matrix), len(matrix[0])
    voyage_end = (1 << rows) - 1  # все города посещены => конец алгоритма

    @lru_cache(None)
    def town_visited(town, visit : bool):
        if visit == voyage_end:
            return matrix[town][0]
        min_distance = float('inf')

        for next_town in range(rows):
            if not (visit & (1 << next_town)):  # если город еще не посещен
                next_distance = matrix[town][next_town] + town_visited(next_town, visit | (1 << next_town)) # рекурсивный обход еще не посещенных
                min_distance = min(min_distance, next_distance)

        return min_distance
    
    return town_visited(0, 1 << 0)


if __name__ == '__main__':
    graph_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    ans = voyage(graph_matrix)
    print(f'Кратчайшее расстояние через все города:\t{ans}')