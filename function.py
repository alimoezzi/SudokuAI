from utils import display

rows = 'ABCDEFGHI'
cols = '123456789'
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


def cross(rows, cols):
    return [s + t for s in rows for t in cols]


def grid_values(s):
    return {i: s[j] for j, i in enumerate(cross(rows, cols))}


def grid_values_with_eliminate(s):
    d = {i: s[j] for j, i in enumerate(cross(rows, cols))}
    for i in d:
        available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if d[i] == '.':
            r = row_units[ord(i[0]) - 65]
            c = column_units[int(i[1]) - 1]
            s = [j for j in square_units if i in j][0]
            for k in r + c + s:
                if d[k].isnumeric() and len(d[k]) == 1:
                    available[int(d[k]) - 1] = -1
            d[i] = ''.join([str(z) for z in available if z != -1])
    return d


def grid_values_with_eliminate_only_choice(s):
    d = {i: s[j] for j, i in enumerate(cross(rows, cols))}
    for i in d:
        available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if d[i] == '.':
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


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, rc) for rs in ('ABC', 'DEF', 'GHI') for rc in ('123', '456', '789')]

if __name__ == '__main__':
    boxes = cross(rows, cols)
    display(grid_values_with_eliminate_only_choice(grid), rows, cols, boxes)
    print(boxes)
