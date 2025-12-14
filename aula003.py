class Televisão:
    
    #TELEVISÃO TEM VÁRIOS ATRIBUTOS E MÉTODOS, ESSE MÉTODOS SÃO DENPEDÊ NTES DOS ATRIBUTOS PARA FUNCIONAR CORRETAMENTE

    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False
#                                                  MÉTODOS

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        else:
            if self.canal < self.canal_max:
                self.canal += 1
            else:
                self.canal = self.canal_min
            
    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        else:
            if self.canal > self.canal_min:
                self.canal -= 1
            else:
                self.canal = self.canal_max

    def aumentar_volume(self):
        if not self.ligada:
            return
        else:
            if self.volume < self.volume_max:
                self.volume += 1

    def diminuir_volume(self):
        if not self.ligada:
                return
        else:
            if self.volume > self.volume_min:
                self.volume -= 1

    def __str__(self) -> str:
        return f"Televisão está ligada: {self.ligada}\nCanal atual: {self.canal}\nVolume: {self.volume}"
    

#todos sabemos que a TV da LG é a melhor
tv_LG = Televisão()

tv_LG.ligar()
print(f"A TV está ligada? {tv_LG.ligada}")

print(f"Canal atual: {tv_LG.canal}")
tv_LG.mudar_canal_para_cima()
print(f"canal atual: {tv_LG.canal}")


tv_LG.mudar_canal_para_baixo()
print(f"canal atual: {tv_LG.canal}")



print(f"Volume atual: {tv_LG.volume}")
tv_LG.aumentar_volume()

print(f"Volume atual: {tv_LG.volume}")

tv_LG.diminuir_volume()
print(f"Volume atual: {tv_LG.volume}")