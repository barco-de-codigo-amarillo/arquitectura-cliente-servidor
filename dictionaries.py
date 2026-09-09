# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Barco',
    'last_name': 'Amarillo',
    'age': 2500,
    'country': 'Saturn',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '07753'
    }
}
"""
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Saturn, print the information in the following format:
    {first_name} {last_name} lives in {country} and is married.
"""

if 'skills' in person:
    lista_skills = person['skills']
    
    # 1. Calculamos el índice del medio usando la división entera //
    indice_medio = len(lista_skills) // 2
    
    print("La habilidad central es:", lista_skills[indice_medio])

    # 2. Buscamos la habilidad ' Python' en la lista
    if 'Python' in lista_skills:
        print('La habilidad Python existe en la lista')
    else:
        print('La habilidad Python NO existe en la lista')

    # 3. Filtramos el perfil usando condiciones anidadas
    if 'JavaScript' in lista_skills and 'React' in lista_skills:
        # Si entra aquí, ya sabemos que tiene la base de Frontend.
        # Ahora miramos si ADEMÁS tiene las tecnologías de Backend:
        if 'Node' in lista_skills and 'MongoDB' in lista_skills:
            print(f'{person["first_name"]} is a fullstack developer')
        
        # Si NO tiene Node/MongoDB y solo tiene esas dos (o no cumple el backend):
        elif len(lista_skills) == 2:
            print(f'{person["first_name"]} is a front end developer')
            
        else:
            print('unknown title')

    elif 'Node' in lista_skills and 'MongoDB' in lista_skills and 'Python' in lista_skills:
        # Este bloque solo se ejecuta si NO tenía JavaScript + React al mismo tiempo,
        # pero sí tiene el combo puro de Backend.
        print(f'{person["first_name"]} is a backend developer')

    else:
        print('unknown title')


# 4. Si la persona está casada y vive en Saturno, imprime la información
if person['is_married'] is True and person['country'] == 'Saturn':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']} and is married.')

