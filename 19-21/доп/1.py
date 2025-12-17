def game(rocks,stage,end):
    # 1. Если камней >= 129, проверяем, на нужном ли мы ходу (stage должно быть в end)
    if rocks >= 129: return stage in end

    # 2. Если превысили лимит ходов, но камней все еще мало — это проигрыш ветки
    if stage >= max(end): return False

    moves = [game(rocks + 1, stage + 1, end), game(rocks * 2, stage + 1, end)]

    # 3. Логика ходов (any/all)
    # Если четность следующего хода совпадает с четностью победного — это НАШ ход (ищем хотя бы одну победу)
    if (stage + 1) % 2 == end[0] % 2:
        return any(moves)
    # Иначе это ход ПРОТИВНИКА (мы должны выигрывать при любом его ходе)
    else:
        return all(moves)


for i in range(1,129):
    if game(i,0,[4])==True:print(i)