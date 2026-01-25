def g(s, h, end):
    # выигрыш: достигли s ≤ 15 ровно на нужном ходе
    if s <= 15:
        return h in end

    # если ходы закончились, а выигрыш не достигнут
    if h == max(end):
        return False

    # возможные ходы
    moves = [g(s - 3, h + 1, end), g(s - 5, h + 1, end)]

    # ход игрока, который стремится к выигрышу
    if (h + 1) % 2 == end[0] % 2:
        return any(moves)
    else:
        return all(moves)


# проверка начальных значений
for x in range(16, 47):
    if g(x, 0, [2]):
        print(x)
