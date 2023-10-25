class Person:

    #Atributo de clase
    species = 'Humano'
    
    def __init__(self, name='', age=0):
        #Atributos de instancia
        self.name = name
        self.age = age
        self.__private_at = name[0]+str(age)
        self._protected_at = None

    #Getter para atributo privado
    @property  #Decorador
    def private_at(self):
        return self.__private_at
    
    #Setter para atributo privado
    @private_at.setter #Decorador - propiedad setter
    def private_at(self, new_at):
        self.__private_at = new_at

    #Deleter para atributo privado
    @private_at.deleter #Decorador - propiedad deleter
    def private_at(self):
        del self.__private_at

    #Método de la clase
    def saludar(self):
        print(f'Hola, mi nombre es {self.name}')
