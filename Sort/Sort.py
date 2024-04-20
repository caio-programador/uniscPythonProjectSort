def bubble_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            comparacoes += 1
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
                num_troca += 1
        n -= 1
    return vetor, comparacoes, num_troca


def insertion_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    for index in range(1, n):
        currentValue = vetor[index]
        position = index
        comparacoes += 1
        while position > 0 and vetor[position - 1] > currentValue:
            vetor[position] = vetor[position - 1]
            position -= 1  # Ajuste aqui
            num_troca += 1
        vetor[position] = currentValue
    return vetor, comparacoes, num_troca


def quick_sort(vetor):
    global comparacoes, num_troca
    comparacoes, num_troca = 0, 0
    quick_sort_helper(vetor, 0, len(vetor) - 1)

    return vetor, comparacoes, num_troca


def quick_sort_helper(vetor, first, last):
    global num_comparacoes, num_troca
    if first < last:
        splitpoint = partition(vetor, first, last)

        quick_sort_helper(vetor, first, splitpoint - 1)
        quick_sort_helper(vetor, splitpoint + 1, last)


def partition(vetor, first, last):
    global comparacoes, num_troca
    pivo = vetor[first]

    esquerda = first + 1
    direita = last

    done = False
    while not done:

        comparacoes += 1
        while esquerda <= direita and vetor[esquerda] <= pivo:
            esquerda = esquerda + 1
            comparacoes += 1
        comparacoes += 1
        while vetor[direita] >= pivo and direita >= esquerda:
            direita = direita - 1
            comparacoes += 1

        if direita < esquerda:
            done = True
        else:
            temp = vetor[esquerda]
            vetor[esquerda] = vetor[direita]
            vetor[direita] = temp
            num_troca += 1

    temp = vetor[first]
    vetor[first] = vetor[direita]
    vetor[direita] = temp

    return direita


def merge_sort(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    vetor = merge_sort_helper(vetor)
    return vetor, comparacoes, num_troca


def merge_sort_helper(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2

    esquerda = merge_sort_helper(vetor[:meio])
    direita = merge_sort_helper(vetor[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    global comparacoes, num_troca
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        if esquerda[i] < direita[j]:
            num_troca += 1
            resultado.append(esquerda[i])
            i += 1
        else:
            num_troca += 1
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def shell_sort(vetor):
    global comparacoes, num_troca
    h = len(vetor) // 2
    comparacoes = 0
    num_troca = 0
    while h > 0:

        for startposition in range(h):
            gapInsertionSort(vetor, startposition, h)

        h = h // 2

    return vetor, comparacoes, num_troca


def gapInsertionSort(alist, start, gap):
    global comparacoes, num_troca
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        comparacoes += 1

        while position >= gap and alist[position - gap] > currentvalue:
            num_troca += 1
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


#  ele pega os menores valores e vai pondo nas menores posicoes
#  faz pesquisa sequencial para achar os menores valores
def selection_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min]:
                min = j

        if min != i:
            vetor[i], vetor[min] = vetor[min], vetor[i]
            num_troca += 1

    return vetor, comparacoes, num_troca


def radix_sort(vetor):
    comparacoes, trocas = 0, 0
    return vetor, comparacoes, trocas


def bucket_sort(vetor):
    comparacoes, trocas = 0, 0
    return vetor, comparacoes, trocas