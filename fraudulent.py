from math import ceil


def proximo(counter, j):
    for i in range(j + 1, len(counter) + 1):
        if counter[i] != 0:
            return i
    raise Exception("Nunca")


def get_mediana(counter):
    tot = sum(counter)  # da pra cachear
    eh_impar = (tot % 2 == 1)
    meio = tot / 2
    # print(f"tot {tot} {eh_impar} {meio}")
    # da pra ser mais inteligente pq diminuiu ou subiu
    tot_ate_agora = 0
    for i, qtd in enumerate(counter):
        tot_ate_agora += qtd
        if eh_impar and tot_ate_agora >= ceil(meio):
            return i
        if not eh_impar and tot_ate_agora > meio:
            return i
        if not eh_impar and tot_ate_agora == meio:
            return (i + proximo(counter, i)) / 2

    # nunca deveria acontecer
    raise Exception(f"Nunca deveria acontecer {counter}")


def activityNotifications(expenditure, d):
    total = 0
    counter = [0] * 201
    for day in range(len(expenditure)):
        gasto = expenditure[day]

        if day >= d:
            # verifica
            mediana = get_mediana(counter)
            # print(f"verificando {gasto} {mediana} {counter}")
            if gasto >= 2 * mediana:
                total += 1
            # remove
            gasto_antigo = expenditure[day - d]
            counter[gasto_antigo] -= 1
        counter[gasto] += 1

    return total


print(activityNotifications([10, 20, 30, 40, 50], 3))
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
# print(activityNotifications([1, 2, 3, 4, 5, 6], 5))
print(activityNotifications([1, 2, 3, 4, 4], 4))
