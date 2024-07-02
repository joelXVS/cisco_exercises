class ErrorDeDíaDeSemana(Exception):
    pass

class Semanario:
    __dias = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, dia):
        try:
            self.__current = Semanario.__dias.index(dia)
        except ValueError:
            raise ErrorDeDíaDeSemana

    def __str__(self):
        return Semanario.__dias[self.__current]

    def agregar_dia(self, num):
        self.__current = (self.__current + num) % 7

    def quitar_dias(self, num):
        self.__current = (self.__current - num) % 7

try:
    diaDeSemana = Weeker('Lun')
    print(diaDeSemana)
    diaDeSemana.add_days(15)
    print(diaDeSemana)
    diaDeSemana.subtract_days(23)
    print(diaDeSemana)
    diaDeSemana = Weeker('Lunes')
except ErrorDeDíaDeSemana:
    print("Lo siento, no puedo atender tu solicitud.")
    
