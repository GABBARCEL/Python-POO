class Livro:
    def __init__(self, titulo, autor, n_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.n_paginas = n_paginas
        self.genero = genero

    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        

Lv_crepusculo = Livro("o Crepsculo", "Gabriel", 2500, "românce")

print(Lv_crepusculo.get_titulo())

Lv_crepusculo.set_titulo("Game of Trones")

print(Lv_crepusculo.get_titulo())
