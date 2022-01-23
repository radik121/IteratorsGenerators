nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# Первое задание

class Nested_iter:

    def __init__(self, n_list):
        self.n_list = n_list

    def __iter__(self):
        self.attach = [item for sublist in nested_list for item in sublist]
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.attach):
            raise StopIteration
        return self.attach[self.cursor]


# Второе задание
def nested_list_items(lst):
    for sublist in lst:
        for item in sublist:
            yield item


if __name__ == '__main__':
    print('Итератор:')
    for elem in Nested_iter(nested_list):
        print(elem)
    flat_list = [item for item in Nested_iter(nested_list)]
    print(flat_list)

    print('-' * 30)

    print('Генератор:')
    for res in nested_list_items(nested_list):
        print(res)