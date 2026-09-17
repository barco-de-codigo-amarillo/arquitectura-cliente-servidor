# combine lists when looping through them

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v}) # posible alternativa tuplas y listas

print(fruits_and_veges)

# Alternativas: cuando no hay elemento (dessemparejados) en una de las dos listas
from itertools import zip_longest

resultado = list(zip_longest(fruits, vegetables, fillvalue="Sin fruta"))

print(resultado)

# 
# Lista 1: Nombres de tecnologías de desarrollo (Strings)
tecnologias = ["Python", "JavaScript", "Docker", "Git", "Linux", "SQL", "HTML"]

# Lista 2: Números enteros de control (Integers)
codigos = [101, 204, 308, 404, 500, 200, 403]

# Lista 3: Estados de activación (Booleans)
estados = [True, False, True, True, False, True, False]
tech = []
for t, c, e in zip(tecnologias, codigos, estados):
    tech.append({'tec':t, 'code':c, 'active': e})

print(tech)