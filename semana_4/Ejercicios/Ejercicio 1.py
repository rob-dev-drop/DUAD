my_string = str("stringvalue")
my_int = int(69)
my_list = [0,1,2,3,4,5]
my_float = 3.14
my_bool = True

my_string2 = str("secondstringvalue")
my_int2 = int(55)
my_list2 = [6,7,8,9,10,11]
my_float2 = 2.57
my_bool2 = False

r1 = my_string + my_string2 # Se concatenan los str
# r2 = my_string + my_int2  #Esta intentado verlo como concatenacion y no se puede concatenar un string con un integer
# r3 = my_int + my_string2 #Esta tratando de sumar y como el string no son numeros, no lo permite
r4 = my_list + my_list2 #se hace una lista mas grande con todos los valores
#r5 = my_string + my_list2 #de igual manera, esta intenando concatenar el str con la lista
r6 = my_float + my_int #se suman los valores y el resultado es un float
r7 = my_bool + my_bool2 #True equivale a 1 y False a 0, entonces cuando se suman queda 1 como el resultado

print(f'{r1}')
#print(f'{r2}') 
#print(f'{r3}') 
print(f'{r4}')
#print(f'{r5}') 
print(f'{r6}')
print(f'{r7}')