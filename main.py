def fruits(fruit_list):
    res = dict()
    for fruit in fruit_list:
        if fruit.get('shape') == 'sphere':
            if 300 <= fruit.get('mass', 0) <= 600:
                if 100 <= fruit.get('volume', 0) <= 500:
                    name = fruit.get('name')
                    if name is not None:
                        if name not in res:
                            res[name] = 1
                        else:
                            res[name] += 1
    return res


fruits((
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))
