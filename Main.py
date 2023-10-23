from Person import Person

my_person = Person('Cinthia',31)

#Accedemos a los atributos del objeto
print(f'Nombre: {my_person.name}, edad: {my_person.age}')

print('---')
#Acceso a atributo de clase
print('Acceso al atributo de clase.')
print(f'Desde el objeto: {my_person.species}')
print(f'Desde la clase: {Person.species}')

print('---')
#Intento de acceder al atributo privado
'''print(my_person.__private_at)''' #Nos dará error
print('Atributo privado original: ')
print(my_person.private_at) #Con getter

#Modificación de atributo privato con setter
my_person.private_at = 'Atributo modificado'
#Verificación
print('\nAtributo privado modificado: ')
print(my_person.private_at) #Con getter

#Borrado del atributo privado
'''del my_person.private_at''' #Con deleter
#Verificamos
'''print(my_person.private_at)''' #Con getter

print('---')
#Intento de acceder al atributo protegido
print(my_person._protected_at)

print('---')
#Creación dinámica de un atributo
my_person.surname = 'Rigoni'
print(f'Atributo creado dinámicamente: {my_person.surname}')

print('---')
#Llamada a un método de la clase, desde el objeto creado
print('Llamada al método "saludar": ')
my_person.saludar()