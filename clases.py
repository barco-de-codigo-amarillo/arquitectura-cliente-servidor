class Human:
    pass # similar a continue
print(Human)

class Person:
    def __init__(self, name = None, lastname  = None, age  = None, gender = None, country  = None, work  = None): # precisa None para mantener el flujo
        # self es puntero hacia la clase y permite extraer los parámetros
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = 'male'
        self.country = country
        self.work = work
        self.skills = []
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.name} {self.lastname} is {self.age}. {self.gender} lives {self.country} and work as {self.work}.'
    def add_skill(self, skill):
        self.skills.append(skill)
    #region Operaciones Matemáticas
    def secction_a(self):
        pass
    def secction_b(self):
        pass
    #endregion
class Former(Person):
    def __init__(self, name = None, lastname  = None, age  = None, country  = None, work  = None, gender = 'female'):
        self.gender = gender
        super().__init__(name, lastname, age, country, work)
    def person_info(self):
        genero = 'female' if self.gender =='male' else 'She'
        return f'{self.name} {self.lastname} is {self.age}. {genero.capitalize()} lives {self.country} and work as {self.work}.'
    def print_work_data(*args,**kwargs):
        for product in args:
            print(product)
        for key in kwargs:
            print(f'{key}: {kwargs[key]}')

urbana = Person('Jhon', 'Smith', 32, 'Boston', 'Programmer')
print(urbana.name)
print(urbana.lastname)
print(urbana.age)
print(urbana.country)
print(urbana.work)
print(urbana.person_info())
rural = Person('John', 'Doe', 30, 'Nomadland', 'Helpdesk')
print(urbana.person_info())
mister = Former('Barbara', 'Liskov', 86, 'California', 'IT')
print(mister.person_info())
mister.add_skill('CLU')
mister.add_skill('Thor')
mister.add_skill('Argus')
mister.add_skill('IA')
print(mister.skills)


if len(urbana.skills)>0:
    print(f"la primera habilidad adquirida de {urbana.firstname} es: {urbana.skills[0]}")
else:
    print(f"{urbana.name} No tiene habilidades")



# MODO "MODERNO" DE DEFINIR CLASES:
from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str     # se declara el tipo
    precio: float
    activo: bool = True
    # Métodos de la clase
    def producto_info(self):
        return f"{self.nombre} {self.precio} está activo: {self.activo}"
    secciones: list[str] = field(default_factory=list) # atributo de clase mutable con un valor inicial vacío (lista de strings); = field(default_factory=list): Es la forma correcta en las dataclass de asignar objetos mutables (como listas o diccionarios) por defecto
    def añadir_seccion(self, seccion):
        self.secciones.append(seccion)

bicicleta = Producto("MB78", 788.95, True)
bicicleta.añadir_seccion("Deportes")
bicicleta.añadir_seccion("Montaña")
print(bicicleta.activo)
print(bicicleta.producto_info())
print(bicicleta.secciones) # ['Deportes', 'Montaña']


# HERENCIA
class Student(Person):
    def __init__(self, name='Barco', lastname='Amarillo', age=2500, country='Saturn', work='Saturnaria', gender='unkonwn'):
        self.gender = gender
        super().__init__(name, lastname, age, country, work)
    def person_info(self):
        genero = 'él' if self.gender == 'male' else 'ella'
        return f'{self.name} {self.lastname} tiene {self.age} años. {genero.capitalize()} trabaja en {self.work}, {self.country}.'


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Engeneering', "male")
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Programming', "female")
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
print('*****************************')



# POLIMORFISMO Y ENCAPSULACIÓN

from abc import ABC, abstractmethod
from dataclasses import dataclass

# 1. CLASE BASE CON DOS PARÁMETROS COMPARTIDOS
@dataclass
class Poligono(ABC):
    """
    Clase abstracta que define las dos dimensiones obligatorias
    y la interfaz común para el cliente.
    """
    base: float
    altura: float

    @abstractmethod
    def calcular_area(self) -> float:
        pass
# 2. IMPLEMENTACIONES ESPECÍFICAS (Encapsulación de la fórmula)
@dataclass
class Rectangulo(Poligono):
    # Hereda automáticamente 'base' y 'altura' de Poligono
    
    def calcular_area(self) -> float:
        # Lógica interna del Rectángulo
        return self.base * self.altura


@dataclass
class Triangulo(Poligono):
    # Hereda automáticamente 'base' y 'altura' de Poligono

    def calcular_area(self) -> float:
        # Lógica interna del Triángulo
        return (self.base * self.altura) / 2


# 3. EL CLIENTE (Polimorfismo puro)

def mostrar_informacion_poligono(poligono: Poligono): # el argumento poligono que debe recibir tiene que ser de tipo Poligono
    """
    El cliente opera de forma idéntica con cualquier polígono.
    Solo interactúa con el método expuesto 'calcular_area'.
    """
    print(f"--- {type(poligono).__name__} ---") # Línea de cortesía para indicar si se instancia un triángulo o un rectángulo. Obtiene el nombre exacto de la clase que se usó para crear el objeto.
    print(f"Dimensiones: Base = {poligono.base}, Altura = {poligono.altura}")
    print(f"Área calculada: {poligono.calcular_area():.2f}\n") # El modificador :.2f asegura que el resultado decimal se muestre redondeado a exactamente 2 posiciones decimales.


# --- Demostración de uso ---
if __name__ == "__main__":
    # Ambos se instancian pasando exactamente dos parámetros
    mi_rectangulo = Rectangulo(base=10.0, altura=5.0)
    mi_triangulo = Triangulo(base=6.0, altura=4.0)

# El cliente los procesa sin distinguir su tipo internamente
    mostrar_informacion_poligono(mi_rectangulo)
    mostrar_informacion_poligono(mi_triangulo)