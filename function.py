rows = 'ABCDEFGHI'
cols = '123456789'


def cross(rows, cols):
    return [s + t for s in rows for t in cols]


def grid_values(s):
    return {i: s[j] for j, i in enumerate(cross(rows, cols))}


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, rc) for rs in ('ABC', 'DEF', 'GHI') for rc in ('123', '456', '789')]

if __name__ == '__main__':
    boxes = cross(rows, cols)
    print(boxes)
