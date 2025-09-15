#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Guarda colores en una lista

print(my_lista) #Imprime la lista
print(type(my_lista)) #Imprime el tipo de variable de la lista
print(my_lista[2]) #Imprime el tercer valor de la lista o el valor que este en la posición 2

print("my_lista size: ", len(my_lista)) #Muestra el tamaño de la lista
print(my_lista[0:2]) #Imprime dos valores de la lista desde la posición 0 
print(my_lista[:2]) #Imprime dos valores de la lista desde el inicio

my_lista.append('Blanco') #Agrega elemento al final de la lista
print(my_lista) #Imprime la lista con el valor nuevo al final

my_lista.insert(3, 'Negro') #Agrega un elemento a la lista en la posición 3
print(my_lista) #Imprime la lista con los nuevos valores


my_lista.extend(['Marron', 'Gris']) #Concatena a otra lista
print(my_lista) #Imprime la lista concatenada completa

print(my_lista.index('Azul')) #Imprime la posición del valor ingresado

my_lista.remove('Marron') #Quita un valor de la lista
print(my_lista) #Imprime la lista sin el valor

my_lista.insert(8, 'Marron') #Pone un valor en la lista en una posición específica 
print(my_lista) #Imprime la lista nueva

print(my_lista.pop()) # Quita el ultimo elemento de la lista y lo imprime
size = len(my_lista) # Guarda en una variable el tamaño de la lista
print("size = ", size) # Imprime la variable con el tamaño de la lista

my_lista_3 = my_lista*3 # Multiplica los valores de la lista y los repite 3 veces
print("my_lista_3: ", my_lista_3) #Imprime la lista multiplicada

print("Sort:") #Imprime el string "Sort:"  
print() # Imprime un espacio en blanco
my_listaSort = my_lista.sort() # Ordena la lista pero por el tipo de datos no tiene orden
print(my_listaSort) #Imprime que no tiene orden la lista

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Es una lista con numeros
print("Ordering my_NumList: ") #Imprime el string "Ordering my_Numlist:"
my_NumList.sort() #Ordena los valores de la lista
print(my_NumList) #Imprime la lista ordenada

my_NumList.sort(reverse = True) #Ordena la lista al revés 
print("De menor a mayor: ", my_NumList) #Imprime la lista de menor a mayor


#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################") #Imprime una serie de numerales
print("###########################") #Imprime una serie de numerales
print("###########################") #Imprime una serie de numerales
print("############TUPLAS#########") #Imprime una serie de numerales y la palabra tuplas
my_tupla = tuple(my_lista) #Convierte la lista en una tupla
print() #Imprime un espacio
print() #Imprime un espacio
print() #Imprime un espacio
print("my_tuple: ", my_tupla) #Imprime la tupla

print(my_tupla[0]) #Imprime el primer valor de la tupla
print(my_tupla[2]) #Imprime el tercer valor de la tupla


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla) #Imprime si el valor se encuentra en la tupla
print(my_tupla.count('Rojo')) #Imprime y cuenta el numero de veces que se encuentra el valor en la tupla

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco') #Guarda una tupla de un solo elemento
print(my_tupla_unitaria) #Imprime el valor de la tupla

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999 #Guarda valores en una tupla de varios tipos
print(my_tupla) #Imrpime los valores de la tupla

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla #Le asigna un nombre a la posición de cada valor
print(nombre) #Imprime el valor de la tupla que va en nombre
print(dia) #Imprime el valor de la tupla que va en dia
print(mes) #Imprime el valor de la tupla que va en mes
print(año) #Imprime el valor de la tupla que va en año

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año) #Imprime la tupla de manera ordenada entre strings

#Convertir una tupla en una lista
my_lista2=list(my_tupla) #Convierte la tupla en lista
print(my_lista2)#Imprime la lista
