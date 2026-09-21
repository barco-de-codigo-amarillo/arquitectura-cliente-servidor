"""
Definir la clase Empleado que herede de Persona. Atributo propio: salario
y cuenta
Definir la clase Cuenta que tiene como atributos: saldo, IBAN
Desde el punto de un empleado implementar estas clases, crear un par de empleados y hacerles cobrar un par de sueldos.
Ideas adicionales: la Cuenta puede tener además un atributo de operaciones
.
Cada operación puede ser de la clase Operación:
cantidad (negativa o positiva), concepto, momento (datetime)
Por tanto (sugerencia) complementar la Cuenta con el atributos de operaciones[Operacion]. El saldo sería siempre un atributo calculado por la suma de las cantidades de las operaciones.
"""
from dataclasses import dataclass, field

print("Ejercicio propuesto en 30-días-Python: En la clase PersonAccount diseña atributos firstname, lastname, incomes y expenses y añade métodos para calcular el ingreso neto de la persona.")
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
class PersonAccount:
    # MÉTODO CONSTRUCTOR
    def __init__(self, f=None, l=None, i=0, e=0):
        self.nombre = f
        self.apellido = l
        self.ingresos = i
        self.gastos = e
     # MÉTODOS
    def personAccount_info(self):
        return f'{self.nombre} {self.apellido} tiene {self.ingresos} de ingreso. Y tiene tiene {self.gastos} de gasto.'
    def calcular_ingreso_neto(self):
        return f"Y tiene un ingreso neto de : {self.ingresos - self.gastos}"


cuentaPersona1 = PersonAccount("Jaime", "Ruíz", 6000, 5000)
print(cuentaPersona1.personAccount_info())
print(cuentaPersona1.calcular_ingreso_neto())
# ********

@dataclass
class Cuenta:
    IBAN: str     # se declara el tipo
    saldo: float
    titular: str | None # Para este problema no se requiere titular. Pero en futuras utilizaciones de Cuenta puede convenir un titular
    movimientos: list[str] = field(default_factory=list)
    def cuenta_info(self):
        return f"La cuenta de IBAN: {self.IBAN} tiene {self.saldo} € de saldo. Y su histórico de momviemntos es {self.movimientos}"
    def añadir_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

# ********
class Empleado(Person):
    def __init__(self, firstname=None, lastname=None, age=0, country='España', city='Zaragoza', account=None):
        self.cuenta = account
        super().__init__(firstname, lastname, age, country, city)

    def empleado_info(self):
        return f"{super().person_info()} tiene cuenta con IBAN: {self.cuenta.IBAN}."

# Prueba de concepto sobre un caso de uso planteado: se asigna cuenta bancaria a un empleado:
unaCuenta = Cuenta("ES44 1111 2222 3333 4444 8888", 1000, ["ingreso", "gasto", "ingreso"])
unEmpleado = Empleado("Luis","Villarán", 30, "España", "Zaragoza", unaCuenta)
print(unEmpleado.empleado_info())
