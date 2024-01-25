import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from repositorio.livro_repositorio import livro_repositorio ## from repositorio import * -> importa tudo desse arquivo

codigo_atual = 1

# Cadastro de livro - function
def registrarLivro(titulo: str, autor: str) -> None: # uma função que não retorna valor
    livro = criarLivro(titulo, autor)
    livro_repositorio.append(livro)
    print("Livro adicionado com sucesso!")

def criarLivro(titulo: str, autor: str) -> dict:
    global codigo_atual # nâo pode alterar uma variável que está fora da função, então usa o comando 'global'
    codigo_atual += 1
    livro = {
        "codigo": codigo_atual,
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }
    return livro

if __name__ == "__main__": # __name__ é uma representacao generica desse arquivo, e o __main__ é onde o projeto esta sendo executado
    registrarLivro("1984", "George Orwel")
    print(livro_repositorio)
    
