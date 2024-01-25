import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from repositorio.livro_repositorio import livro_repositorio
from livro.livro_buscar import buscarPorCodigo

def editarLivro(codigo: int, titulo: str, autor: str) -> None:
    livro = buscarPorCodigo(codigo)
    if livro:
        livro['titulo'] = titulo
        livro['autor'] = autor
        print('Dados alterados com sucesso!')
    else:
        print('Livro não encontrado!')
        
if __name__ == "__main__":
    editarLivro(1, "Clean Code", "Arthur")
    print(buscarPorCodigo(1))
    editarLivro(2, "As Cronicas de Narnia", "Wells")
        
    