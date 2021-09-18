class Persona:
    
    nombre =''
    telefono:str
    correo: str
    
    def __init__(self,nombre=''):
        self.nombre = nombre
        
    def metodo1(self):
        pass
    
    def meotodo2(self):
        pass
    
class Estudiante:
    
    identificacion: int
    promedio: float
    
    def __init__(self,nombre):
        Persona.__init__(self.nombre)
        super().__init__(nombre)
        pass
    
    def metodom1(self):
        pass
    
    def metodom2(self):
        pass
    
    

        