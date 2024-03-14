def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print('Achei a chave!')

class Caixa:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def e_uma_caixa(self):
        return isinstance(self.conteudo, list)

    def e_uma_chave(self):
        return isinstance(self.conteudo, str) and self.conteudo.lower() == 'chave'


def procure_pela_chave(caixa):
    for item in caixa:
        if isinstance(item, Caixa):
            if item.e_uma_caixa():
                procure_pela_chave(item.conteudo)
            elif item.e_uma_chave():
                print('Achei a chave!')


# Exemplo de uso do código
caixa_principal = [
    "Livros",
    Caixa(["Roupas", "Chave"]),
    "Eletrônicos",
    Caixa(["Documentos", Caixa(["Chave"]), "Ferramentas"]),
]

# Chamada da função para procurar pela chave na caixa principal
procure_pela_chave(caixa_principal)

