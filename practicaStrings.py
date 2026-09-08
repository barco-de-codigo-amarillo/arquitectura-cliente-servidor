# Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'
print('Thirty', 'Days', 'Of', 'Python')

# Une las cadenas 'Coding', 'For', 'All' en 'Coding For All'
print('Coding', 'For', 'All')

# Declara la variable company y asígnale el valor inicial "Coding For All"
company = 'Coding For All'

# Imprime la variable company usando print()
print(company)

# Usa len() y print() para mostrar la longitud de la cadena company
print(len(company))

# Usa el método upper() para convertir todos los caracteres a mayúsculas
print(company.upper())

# Usa el método lower() para convertir todos los caracteres a minúsculas
print(company.lower())

# Aplica capitalize(), title() y swapcase() sobre la cadena 'Coding For All'
print(company.capitalize())
print(company.title(), 'title')
print(company.swapcase())

# Extrae mediante slicing la primera palabra de 'Coding For All'
print(company[0:6])
# SLICING de cadenas:
language = 'Python'
first_three = language[0:3] # empieza en índice 0, hasta 3 pero sin incluir 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Otra forma
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
# Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'.
cadena1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(cadena1, f"tiene {len(cadena1)} caracteres")

# Usa index, find u otros métodos para comprobar si la cadena 'Coding For All' contiene la palabra 'Coding'
print(company.index('Coding')) # Saca el índice inicial de la palabra 'Coding'
print(company.find('Coding')) # Busca la palabra y devuelve el índice inicial de la palabra 'Coding'


# Reemplaza la palabra 'Coding' por 'Python' en 'Coding For All'
company = company.replace('Coding', 'Python')
print(company)
    

# Reemplaza 'Python for Everyone' por 'Python for All' (usa replace() u otro método)
company = company.replace('All', 'Everyone')
print(company)


# Separa la cadena 'Coding For All' usando espacios como separador
company = company.split(' ')
print(company)

 # Divide la cadena 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' por las comas
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies)
companies = companies.split(', ')
print(companies)

# ¿Qué carácter está en el índice 0 de 'Coding For All'?
print(company[0]) # Anteriormente hemos reasignado la variable company para poder trabajar con el método replace() por lo que se espera 'Python'


# ¿Cuál es el índice del último carácter de 'Coding For All'?
print(len(company) - 1) # 2, porque la variable company ahora es una lista ['Python', 'For', 'Everyone'] y el último índice es 2

# ¿Qué carácter está en el índice 10 de 'Coding For All'?
company = 'Coding For All'
print(company[10])


# Crea una sigla (acrónimo) a partir de 'Python For Everyone'
company = company.replace('Coding', 'Python')
company = company.replace('All', 'Everyone')
acronym = ''.join(word[0].upper() for word in company.split())
print(acronym)


# Crea una sigla a partir de 'Coding For All'
acronym = ''.join(word[0].upper() for word in 'Coding For All'.split())
print(acronym)


# Usando index, determina la primera aparición de la letra 'C' en 'Coding For All'
company = 'Coding For All'
print(company.index('C')) # 0


# Usando index, determina la primera aparición de la letra 'F' en 'Coding For All'
print(company.index('F')) # 7


# Usa rfind para determinar la última aparición de 'l' en 'Coding For All People'
company = 'Coding For All People'
print(company.rfind('l')) # 19


# Usa index o find para encontrar la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'
info = 'You cannot end a sentence with because because because is a conjunction'
print(info.index('because', 20)) # empieza a buscar desde la posición 20


# Usa rindex para encontrar la última aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'
print(info.rindex('because'))


# Elimina la frase 'because because because' de: 'You cannot end a sentence with because because because is a conjunction'
info = info.replace('because because because', 'because')
print(info)


# ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?
company = 'Coding For All'
print(company.startswith('Coding')) # True


# ¿La cadena 'Coding For All' termina con la subcadena 'coding'?
print(company.endswith('coding')) # False


# Elimina los espacios en blanco a la izquierda y derecha de la cadena '   Coding For All      '
print('   Coding For All      '.strip()) # 'Coding For All'


# Usando isidentifier(), ¿cuál de las siguientes devuelve True?
a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(a.isidentifier()) # False
print(b.isidentifier()) # True


# Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios
frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(frameworks)) # 'Django Flask Bottle Pyramid Falcon'


# Usa la secuencia de escape de nueva línea para separar las siguientes oraciones:
"""
I am enjoying this challenge.
I just wonder what is next.
"""
frase1 = 'I am enjoying this challenge.'
frase2 = 'I just wonder what is the next.'
print(frase1 + '\n' + frase2)


# Usa la secuencia de tabulación para mostrar
"""
Name      Age     Country   City
Barco    2500     Saturno   Saturnaria
"""
word1 = 'Name'
word2 = 'Age'
word3 = 'Country'
word4 = 'City'
name = 'Barco'
age = '2500'
country = 'Saturno'
city = 'Saturnaria'

print(f'{word1}\t{word2}\t{word3}\t{word4}\n{name}\t{age}\t{country}\t{city}')


# Usa un método de formateo de cadenas para imprimir
"""
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
"""
print('radius = 10\narea = 3.14 * radius ** 2 \n# The area of a circle with radius 10 is 314 meters square.')


# Usa un método de formateo de cadenas para imprimir:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
print('8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')


# CONVERTIRLO EN UN TEXTO ALTERNATIVO EXTRALLENDO LAS APARICIONES DE "el" O "el," O "el;" "el." POR "un" O "un,
# " O "un;" O "un.".
"""
texto:
El sol de la mañana iluminaba un antiguo sendero que cruzaba un espeso bosque. Caminar por allí siempre 
me daba mucha paz, especialmente cuando el viento suave movía las copas de los árboles altos. A lo lejos, 
el cantar de un pájaro interrumpió un profundo silencio. Decidí sentarme en una gran roca a descansar y 
contemplar el paisaje en calma. La naturaleza tiene una magia única que logra desconectarnos por completo 
de la rutina diaria. Al final, regresé directo a casa con la mente despejada y el corazón lleno de una 
inmensa tranquilidad. 
"""

texto = 'El sol de la mañana iluminaba un antiguo sendero que cruzaba un espeso bosque. Caminar por allí siempre me daba mucha paz, especialmente cuando el viento suave movía las copas de los árboles altos. A lo lejos, el cantar de un pájaro interrumpió un profundo silencio. Decidí sentarme en una gran roca a descansar y contemplar el paisaje en calma. La naturaleza tiene una magia única que logra desconectarnos por completo de la rutina diaria. Al final, regresé directo a casa con la mente despejada y el corazón lleno de una inmensa tranquilidad. '

texto_alternativo = texto.replace('El', 'Un').replace('el ', 'un ')
print(texto_alternativo)


# Extrae de la variable contratolas cadenas de texto '………..........', '………….', '……....', '………', '……', '……………', '…....':

contrato = """De una parte, y como arrendador, persona física, D/Dña. …………., mayor de edad,
domiciliado/a en ………, y con NIF nº ……....Y con datos de contacto a efectos de notificaciones:
correo electrónico: ……….........., y número de teléfono:…….
De otra parte, y como arrendatario, D/Dña. ……………, mayor de edad, con NIF…...., con
domicilio a efectos de notificaciones en la vivienda objeto de arrendamiento. Y con datos de
contacto a efectos de notificaciones: correo electrónico: ………........., y número de teléfono:…..
Ambas partes se reconocen la capacidad legalmente necesaria para el otorgamiento del
presente contrato de arrendamiento. (En su caso indicar si se actúa por representación
debidamente justificada)
EXPONEN2
Que D/ Dña. …………, arrendador, es propietario/a de una vivienda localizada en la
calle…..nº…..piso……con Referencia Catastral………e inscrita en el Registro de la
Propiedad………..y de un trastero/plaza de garaje/anexo……….(incluir aquí o en un Anexo, la
descripción física de la finca, si está amueblada o no y, en su caso, un inventario de los mismos)
Se deja constancia de que la vivienda posee el preceptivo certificado de eficiencia energética,
de conformidad con lo establecido por el Real Decreto 235/2013, de 5 de abril, por el que se
aprueba el procedimiento básico para la certificación de la eficiencia energética de los
edificios.
Que D/Dña………………...está interesado/a en arrendar para uso permanente de vivienda suyo
y/o de su familia (incluir el número de personas y su identificación), el inmueble descrito…….
Ambas partes se comprometen a cumplir con lo pactado en el presente contrato de
arrendamiento.

1
Son el arrendador y el arrendatario, que pueden actuar en nombre propio o mediante representación
debidamente acreditada. El arrendador, conocido coloquialmente como “casero” es el propietario de una
vivienda que cede su uso a otra a cambio de dinero. El arrendatario, también conocido coloquialmente como
“inquilino” es la persona que tiene derecho a usar un bien que pertenece a otra pagando una remuneración por
ello. Tanto el arrendador como el arrendatario pueden ser personas naturales o jurídicas. Las dos partes,
arrendador y arrendatario, deberán estar perfectamente identificadas en el contrato y, de manera especial en el
caso del arrendatario, todos los miembros de la unidad familiar que convivirán en el inmueble arrendado. Esto
evitará problemas de interpretación de la existencia de posibles subarriendos de habitaciones no autorizados
expresamente y por escrito por el arrendador
2
: La vivienda que se alquila deberá estar identificada con claridad (dirección completa y superficie) y sus
características más específicas, como los anejos (garaje, trastero, etc.), así como dejar claro si éstos se incluyen
o no en el contrato. También debe hacerse constar la referencia catastral y la inscripción en el Registro de la
Propiedad."""


print(contrato.replace('………..........', '').replace('………….', '').replace('……....', '').replace('………', '').replace('……', '').replace('……………', '').replace('…....', ''))


# 1. Limpiamos la puntuación básica (comas y puntos) y pasamos todo a minúsculas
contratosinsuspensivos = contrato.lower().replace(',', '').replace('.', '')
# 2. Convertimos el texto en una lista de palabras usando los espacios
lista_palabras = contratosinsuspensivos.split()
# 3. Convertimos la lista en un set para eliminar duplicados
conjunto_palabras = set(lista_palabras)
print(conjunto_palabras)
# Inicio de de IA con análisis de texto.


