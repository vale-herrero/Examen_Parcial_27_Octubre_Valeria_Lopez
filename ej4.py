
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
    def __str__(self): return 'lo que quiero mostrar'



alumno1 = Alumno('Valeria', 8)
print(alumno1)
print(alumno1.__dict__)