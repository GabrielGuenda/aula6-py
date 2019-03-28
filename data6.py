class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.meses = {1:31, 2: 28, 3: 31, 4: 30,
                      5: 31, 6: 30, 7: 31, 8: 31,
                      9: 30, 10: 31, 11: 30, 12: 31}

    def imprime_data(self):
        saida = f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"
        print (saida)

    
    def amanha(self):
        if self.dia < self.meses[self.mes]: 
            self.dia += 1
        else:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1

        saida = f"{self.dia+1:02d}/{self.mes:02d}/{self.ano:04d}"
        print (saida)


    def semana(self):
        saida = f"{self.dia+7:02d}/{self.mes:02d}/{self.ano:04d}"
        print (saida)

        
    def proximo_ano(self):
        self.ano += 1

if __name__ == '__main__':
    dia = Data(25, 12, 2019)
    dia.imprime_data()
    dia2 = Data(2, 12, 2019)
    dia2.imprime_data()
    dia2.amanha()
    dia2.semana()
    dia2.proximo_ano()