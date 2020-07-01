def analise(como):
    posicao = len(como) - 1
    palavras = []
    while posicao != 0:
        palavra = como[posicao]
        posicao -= len(palavra)
        palavras.append(palavra)
    return " ".join(list(reversed(palavras)))


def passwordCracker(passwords, loginAttempt):
    total = len(loginAttempt)
    eh_possivel = [False] * (total + 1)
    eh_possivel[0] = True
    como = [""] * (total + 1)
    for posicao in range(total):
        if not eh_possivel[posicao]:
            continue
        for palavra in passwords:
            if loginAttempt[posicao:].startswith(palavra):
                nova_posicao = posicao + len(palavra)
                eh_possivel[nova_posicao] = True
                como[nova_posicao] = palavra
                if nova_posicao == len(como)-1:
                    return analise(como)
    return "WRONG PASSWORD"


print(passwordCracker(["because", "can", "do", "must", "we", "what"], "wedowhatwemustbecausewecan"))
print(passwordCracker(["a", "b", "c", "d", "e", "f"], "bacbcabcabacbcacabcabcabbacbcaabccbaacbbacbcabcabcabcabcabcabcabacbcab"))
print(passwordCracker(["a", "b", "c", "d", "e", "f"], "bacbcabcabjacbcacabcabcabbacbcaabccbaacbbacbcabcabcabcabcabcabcabacbcab"))
print(passwordCracker(["a", "b", "ab", "ba", "aba", "abb"], "babababaabababababababababababababababababa"))

print(passwordCracker(["because", "can", "do", "must", "we", "what"], "wedowhatwe234mustbecausewecan"))
                                                                       # 10100100000000000000000000