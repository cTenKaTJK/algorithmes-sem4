from functools import lru_cache


def packing(items, box_size):

    @lru_cache(None)
    def sub_pack(mask):
        if mask == 0:
            return 0
        # изначально на 1 коробку 1 предмет
        min_bins = n
        subset = mask
        while subset:
            # объем переданного набора вещей аещей
            weight = sum(items[i] for i in range(n) if subset & (1 << i))
            if weight <= box_size:
                # рекурсивно вызываем функцию с добавленным предметом
                min_bins = min(min_bins, 1 + sub_pack(mask ^ subset))
            subset = (subset - 1) & mask
        return min_bins

    n = len(items)
    # все предметы разложены по коробкам 
    all_items = (1 << n) - 1
    return sub_pack(all_items)       


if __name__ == '__main__':
    items = [8, 3, 5, 4, 1, 7, 1]
    box_size = 10
    print(packing(items, box_size))