class Pessoa:
    olhos=3
    maos=2
    manaus='am'

    def __init__(self,*filhos, nome = None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos =list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    carlos = Pessoa(nome='Carlos')
    luciana = Pessoa(carlos, nome='Luciana')
    print(Pessoa.cumprimentar(luciana))
    print (id(luciana))
    print(luciana.cumprimentar())
    print(luciana.nome)
    print(luciana.idade)
    for filho in luciana.filhos:
        print(filho.nome)
    luciana.sobrenome = 'Guarnieri'
    luciana.olhos= 1
    del luciana.filhos
    print(luciana.__dict__)
    print(carlos.__dict__)
    print(Pessoa.olhos)
    print(luciana.olhos)
    print(carlos.olhos)
    print(id(Pessoa.olhos))
    print(luciana.maos)
    print(luciana.manaus)
