def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('X' if cell else 'O')
        s.append('\n')
    return ''.join(s)


cell_state_map = {}


def build_state_map():
    for i in range(512):
        all_but_center_bit = 0b111101111 & i
        active_bit_count = bin(all_but_center_bit).count('1')

        if active_bit_count < 2 or active_bit_count > 3:
            cell_state_map[i] = False
        elif active_bit_count == 3:
            cell_state_map[i] = True
        else:
            cell_state_map[i] = 0b00001000 & i


def get_generation(cells, generations):
    universe = []
    for y, row in enumerate(cells):
        universe.append([])
        for x, cell in enumerate(row):
            cell_state = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        cell_state |= cells[y + i][x + j]
                        cell_state << 1
                    except:
                        cell_state << 1
            next_state = cell_state_map[cell_state]
            universe[y].append(next_state)
    return universe
