def principal(renglon, columna):
        for i in range(8):
            if tablero[renglon][i] == 'R' or tablero[i][columna] == 'R':
                return False

        if renglon <= columna:
            c = columna - renglon
            r = 0
        else:
            r = renglon - columna
            c = 0
        while c < 8 and r < 8:
            if tablero[r][c] == 'R':
                return False
            r += 1
            c += 1

        if renglon <= columna:
            r = 0
            c = columna + renglon
            if c > 7:
                r = c - 7
                c = 7
        else:
            c = 7
            r = renglon - (7 - columna)

        while c >= 0 and r < 8:
            if tablero[r][c] == 'R':
                return False
            r += 1
            c -= 1

        return True

def colocar_reina(n):
        if n < 1:
            return True

        for idx_renglon in range(8):
            for idx_columna in range(8):
                if principal(idx_renglon, idx_columna):
                    tablero[idx_renglon][idx_columna] = 'R'
                    if colocar_reina(n-1):
                        return True
                    else:
                        tablero[idx_renglon][idx_columna] = 'x'

        return False


tablero = []
for i in range(8):
    tablero.append(['x'] * 8)
colocar_reina(8)
for renglon in tablero:
    print(*renglon)