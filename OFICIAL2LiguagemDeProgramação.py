class Acervo:

    def __init__(self, titulo, autor, editora, ano_de_publicacao, ano_de_aquisicao, lido, data ):

        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano_de_publicacao = ano_de_publicacao
        self.ano_de_aquisicao = ano_de_aquisicao
        self.lido = lido
        self.data = data

    def __repr__(self): #Função de conversão para string
      return repr((self.titulo))

    def nome_do_autor(self, autor): #Buscar livros pelo autor
        print()
        print('Busca por autor')
        for i in  Livros:
            if autor == i.autor:
                print(i)

    def nao_lido(self): #listar todos os livros não lidos
        print()
        print('Livros não lidos:')
        for i in Livros:
            if i.lido =='NÃO':
                print(i.titulo)

    def info(self):
        print('----------------------------------------------')
        print(' Título .............. ' + self.titulo)
        print(' Autor ............... ' + self.autor)
        print(' Editora ............. ' + self.editora)
        print(' Ano de publicação ... ' + str(self.ano_de_publicacao))
        print(' Ano de aquisição .... ' + str(self.ano_de_aquisicao))
        print(' Lido ................ ' + self.lido)
        print(' Data ................ ' + str(self.data))

    def ler(self, data): #função para livors que eu li e adicionei a data de quando foi lido
        self.lido = 'Sim'
        self.data = data

Livro1 = Acervo('Sociedade do Anel', 'J. R. R. Tolkien', 'HarperCollins Brasil', 2021 , 2021 , 'NÃO', 0000)
Livro2 = Acervo('Duas Torres' , 'J. R. R. Tolkien', 'HarperCollins Brasil', 2021 , 2021 , 'NÃO', 0000)
Livro3 = Acervo('Retorno do Rei' , 'J. R. R. Tolkien', 'HarperCollins Brasil', 2021 , 2021 , 'NÃO', 0000)
Livro4 = Acervo('Pedra Filosofal', 'J.K. Rowling', 'Arthur A. Levine Books', 1997 , 2010 , 'NÃO', 0000)
Livro5 = Acervo('Câmara Secreta', 'J.K. Rowling', 'Arthur A. Levine Books', 1998 , 2010 , 'NÃO', 0000)
HQ1 = Acervo('Peter Parker (34)', 'Stan Lee', 'Marvel', 1986, 2005, 'NÃO', 0000)
MANGA1 = Acervo('Dragon Ball (01)', 'Akira Toriyama','Panini Comics', 2017, 1995,'NÃO', 0000 )

Livros = [Livro1, Livro2, Livro3, Livro4, Livro5, HQ1, MANGA1 ] #lista
print()
print('Ordem Alfabética:', (sorted(Livros, key=lambda Acervo: Acervo.titulo)))

Livros[0].nome_do_autor('J.K. Rowling')

Livro1.ler(2021)
Livro4.ler(2010)
Livro5.ler(2011)
HQ1.ler(2005)
MANGA1.ler(2017)

Livros[0].nao_lido()

Livro1.info()
Livro2.info()
Livro3.info()
Livro4.info()
Livro5.info()
HQ1.info()
MANGA1.info()
