from utils import display

rows = 'ABCDEFGHI'
cols = '123456789'
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


def cross(rows, cols):
    return [s + t for s in rows for t in cols]


def grid_values(s):
    return {i: s[j] for j, i in enumerate(cross(rows, cols))}


def grid_values_with_eliminate(*args):
    if len(args) == 1:
        if isinstance(args[0], str):
            d = {i: args[0][j] for j, i in enumerate(cross(rows, cols))}
        elif isinstance(args[0], dict):
            d = args[0]
        else:
            raise Exception(f'Invalid type of input {type(args[0])}')
    else:
        raise Exception(f'Invalid number of args {len(args)}')
    for i in d:
        available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if d[i] == '.':
            available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        elif d[i].isnumeric() and len(d[i]) == 1:
            continue
        else:
            available = [-1 if str(z) not in d[i] else z for z in range(1, 10)]
        r = row_units[ord(i[0]) - 65]
        c = column_units[int(i[1]) - 1]
        s = [j for j in square_units if i in j][0]
        for k in r + c + s:
            if d[k].isnumeric() and len(d[k]) == 1:
                available[int(d[k]) - 1] = -1
        d[i] = ''.join([str(z) for z in available if z != -1])
    return d


def grid_values_with_eliminate_only_choice(*args):
    if len(args) == 1:
        if isinstance(args[0], str):
            d = {i: args[0][j] for j, i in enumerate(cross(rows, cols))}
        elif isinstance(args[0], dict):
            d = args[0]
        else:
            raise Exception(f'Invalid type of input {type(args[0])}')
    else:
        raise Exception(f'Invalid number of args {len(args)}')
    for i in d:
        if d[i] == '.':
            available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        elif d[i].isnumeric() and len(d[i]) == 1:
            continue
        else:
            available = [-1 if str(z) not in d[i] else z for z in range(1, 10)]
        r = row_units[ord(i[0]) - 65]
        c = column_units[int(i[1]) - 1]
        s = [j for j in square_units if i in j][0]
        for k in r + c + s:
            if d[k].isnumeric() and len(d[k]) == 1:
                available[int(d[k]) - 1] = -1
        d[i] = ''.join([str(z) for z in available if z != -1])
    for i in d:
        cnt = {i: 0 for i in range(1, 10)}
        if len(d[i]) > 1:
            r = row_units[ord(i[0]) - 65]
            c = column_units[int(i[1]) - 1]
            s = [j for j in square_units if i in j][0]
            for k in r + c + s:
                if d[i] != d[k]:
                    for z in d[k]:
                        cnt[int(z)] += 1
            for z in cnt:
                if cnt[z] == 0:
                    d[i] = str(z)
    return d


def reduce_puzzle(values):
    one_in_two = False
    l = 0
    i = grid_values_with_eliminate(values)
    j = grid_values_with_eliminate_only_choice(i)
    while l != len(j.values()):
        i = grid_values_with_eliminate(j)
        j = grid_values_with_eliminate_only_choice(i)
        if one_in_two is True:
            l = len(j.values())
            one_in_two = False
        else:
            one_in_two = True
    return j


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, rc) for rs in ('ABC', 'DEF', 'GHI') for rc in ('123', '456', '789')]

if __name__ == '__main__':
    boxes = cross(rows, cols)
    display(grid_values_with_eliminate_only_choice(grid), rows, cols, boxes)
    print('**')
    display(reduce_puzzle(grid), rows, cols, boxes)
    print(boxes)
