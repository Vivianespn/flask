def media(notas):
    return sum(notas) / len(notas)

def ultimos_n(itens, n):
    return itens[len(itens) - n - 1:]

def adicionar_tag(tag, tags=[]):
    tags.append(tag)
    return tags

def aprovado(status):
    return status is "aprovado"
