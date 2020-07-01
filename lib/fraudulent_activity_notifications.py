from math import ceil


def proximo_gasto(existentes, gasto):
    # print("igual", existentes, gasto + 1)
    for i in range(gasto + 1, 201):
        # print(existentes[i], i)
        if existentes[i] > 0:
            return i
    raise Exception("nao calculei direito")


def mediana(existentes, d):
    # 3
    if d % 2 == 1:
        posicao = ceil(d / 2)
    else:
        # 4, posicao = 2
        # [a, b, c, d]
        posicao = d / 2

    soma = 0
    for gasto in range(201):

        quantidade = existentes[gasto]
        if quantidade == 0:
            continue

        # print(gasto, quantidade, posicao)
        if soma + quantidade > posicao:
            return gasto
        if soma + quantidade == posicao:
            if d % 2 == 1:
                return gasto
            proximo = proximo_gasto(existentes, gasto)
            total = (gasto + proximo)
            return total / 2

        soma += quantidade

    raise Exception("Fiz algo errado")


def activityNotifications(expenditure, d):
    existentes = [0] * 201
    fraudes = 0
    for dia in range(len(expenditure)):
        gasto_no_dia = expenditure[dia]
        if dia < d:
            existentes[gasto_no_dia] += 1
            continue
        # sera que eh fraude?
        m = mediana(existentes, d)
        # print(gasto_no_dia, m * 2)
        if gasto_no_dia >= m * 2:
            fraudes += 1
        existentes[gasto_no_dia] += 1
        gasto_antigo = expenditure[dia - d]
        existentes[gasto_antigo] -= 1
    return fraudes


print(activityNotifications([10, 20, 30, 40, 50], 4))
print(activityNotifications([10, 20, 30, 40, 44], 4))
print(activityNotifications([10, 20, 25, 40, 44], 4))

print(activityNotifications([10, 20, 30, 40, 50], 3))
print(activityNotifications([30, 10, 20, 40, 50], 3))
