def breakingRecords(scores):
    if len(scores) == 0:
        return [0, 0]
    recorde_superior = scores[0]
    recorde_inferior = scores[0]
    total_recorde_superior = 0
    total_recorde_inferior = 0
    for pontuacao in scores:
        if pontuacao > recorde_superior:
            recorde_superior = pontuacao
            total_recorde_superior += 1
        if pontuacao < recorde_inferior:
            recorde_inferior = pontuacao
            total_recorde_inferior += 1
    return [total_recorde_superior, total_recorde_inferior]


print(breakingRecords([12, 24, 10, 24]))
print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
print(breakingRecords([12, 12, 12, 12]))
print(breakingRecords([12]))
print(breakingRecords([]))
print(breakingRecords([0]))
print(breakingRecords([0,3,4]))
print(breakingRecords([4,3,0]))
