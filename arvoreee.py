class NodoArvore:
    def __init__(self, chave=None, esquerda=None,
                 direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and
                                   self.esquerda.chave,
                                   self.chave,
                                   self.direita and
                                   self.direita.chave)


raiz = NodoArvore(3)
raiz.esquerda = NodoArvore(5)
raiz.direita = NodoArvore(1)
print("Árvore: ", raiz)


raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)


def em_ordem(raiz):
    if not raiz:
        return

    em_ordem(raiz.esquerda)

    print(raiz.chave),

    em_ordem(raiz.direita)


def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo

    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)


for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
em_ordem(raiz)


def busca(raiz, chave):

    if raiz is None:
        return None

    if raiz.chave == chave:
        return raiz

    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    return busca(raiz.esquerda, chave)

for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!"
              .format(chave))
    else:
        print("Busca pela chave {}: Falha!"
              .format(chave))
