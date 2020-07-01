def organizingContainers(containers):
    n = len(containers)
    capacidade_de_containers = []
    quantidade_de_bolas = [0] * n
    for container in containers:
        total_do_container = sum(container)
        capacidade_de_containers.append(total_do_container)
        for tipo, quantidade in enumerate(container):
            quantidade_de_bolas[tipo] += quantidade
    capacidade_de_containers.sort()
    quantidade_de_bolas.sort()
    if capacidade_de_containers== quantidade_de_bolas:
        return "Possible"
    return "Impossible"


print(organizingContainers([[1,3,1],[2,1,2],[3,3,3]]))
print(organizingContainers([[0,2,1],[1,1,1],[2,0,0]]))
print(organizingContainers([[2,0,0],[1,1,1],[0,2,1]]))