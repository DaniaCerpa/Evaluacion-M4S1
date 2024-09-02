class Personalequipo:
    """
    Se establece una clase Padre que represente al personal que compone a la seleccion de futbol.
    Sus atributos seran id, nombre, apellidos y edad.
    Sus metodos seran concentrase y viajar.
    Atributos y metodos se heredan a subclases (clases hijas).
    """
    def __init__(self, id: int, nombre: str, apellidos: str, edad: int, ) -> None:
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def concentrarse(self):
        return f"{self.nombre} {self.apellidos} ha entrado en modo concentración"
    
    def viajar(self):
        return f"{self.nombre} {self.apellidos} tiene un viaje programado"

    
 
#Establecimiento de clases hijas con rescpeto a la clase padre Personalequipo     

    
class Futbolista(Personalequipo):
    """
    Representa a un Futbolista, miembro del personal del equipo de la selección de futból
    Hereda atributos y metodos de la clase Personalequipo. 
    Añade los atributos dorsal y demarcacion. 
    Añade los metodos jugar_partido y entrenar.
    """
    def __init__(self, id: int, nombre: str, apellidos: str, edad: int, dorsal:int, demarcacion:str):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
        
    def jugar_partido(self):
        return f"A {self.nombre} {self.apellidos} le correponde jugar un partido"
    
    def entrenar(self):
        return f"A {self.nombre} {self.apellidos} le correponde entrenamiento"
    
    
   
class Entrenador(Personalequipo):
    """
    Representa a un Entrenador, miembro del personal del equipo de la selección de futból
    Hereda atributos y metodos de la clase Personalequipo. 
    Añade el atributo idfederacion. 
    Añade los metodos dirigir_partido y dirigir_entrenamiento.
    """
    def __init__(self, id: int, nombre: str, apellidos: str, edad: int, idfederacion: str):
        super().__init__(id, nombre, apellidos, edad)
        self.idfederacion = idfederacion
        
        
    def dirigir_partido (self):
        return f"A {self.nombre} {self.apellidos} de la Federación {self.idfederacion} le correponde dirigir el partido"
        
    def dirigir_entrenamiento (self):
        return f"A {self.nombre} {self.apellidos} de la Federación {self.idfederacion} le correponde dirigir el entrenamiento"
        
        
class Masajista(Personalequipo):
    """
    Representa a un Masajista, miembro del personal del equipo de la selección de futból
    Hereda atributos y metodos de la clase Personalequipo. 
    Añade el atributo titulacion y annosexperiencia.
    Añade el metodo dar_masajes 
    """
    def __init__(self, id: int, nombre: str, apellidos: str, edad: int, titulacion: str, annosexperiencia: int):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosexperiencia = annosexperiencia
        
    def dar_masajes (self):
        return f"A {self.nombre} {self.apellidos}, {self.titulacion}, le correponde realizar masajes para el equipo"
    
    
    
 #Ejemplo de uso de metodos de clase (padre e hijas)
jorge = Futbolista(123, "Jorge", "Gonzales Soto", 21, 10, "central")
print(jorge.jugarpartido())
print(jorge.viajar())

ana = Entrenador (345, "Ana", "Perez Medina", 40, "FedeSur")
print(ana.dirigirentrenamiento())
print(ana.concentrarse())

pedro = Masajista(678, "Pedro", "Oliva Fernandez", 25, "Masajista profesional", 5)
print(pedro.darmasajes())