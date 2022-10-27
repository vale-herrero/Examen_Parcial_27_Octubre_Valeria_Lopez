
class Alumno():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print('se ha creado el alumno con exito')
    
    def calificacion(self, nota):
        if nota>4 and nota<10:
            print('El alumno ha aprobado')
        elif nota<=4:
            print('El alumno ha suspenso')
        else:
            print('El alumno no tiene una nota valida')

alumno1= Alumno('Valeria', 8)
alumno1.calificacion(8)
alumno2=Alumno('Rodrigo', 9)
alumno2.calificacion(9)
