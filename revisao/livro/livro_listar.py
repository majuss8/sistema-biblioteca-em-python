import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from repositorio.livro_repositorio import livro_repositorio

def listarLivros() -> None:
    print("--- TODOS OS LIVROS ---")
    for livro in livro_repositorio:
        print(f'Codigo: {livro["codigo"]}')
        print(f'Titulo: {livro["titulo"]}')
        print(f'Autor: {livro["autor"]}')
        print(f'Emprestado?: {livro["emprestado"]}')
        print("-" * 30)
        
if __name__ == "__main__":
    listarLivros()