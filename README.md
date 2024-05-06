
# 🪴 - Practico 5
###  Manejo de errores

En este proyecto vamos a ver el manejo de errores con el metodo try-except, con sus diferentes usos y casos en los cuales puede aplicarse.

#### 🌱- Ejercicio 1
 Utilizamos el método try-except para la división un número por 0, donde en el try ponemos la operación matemática y en el except usamos el error ZeroDivisionError para hacer un print si el usuario ingresa como 2do número un 0.

#### 🌱- Ejercicio 2
 Utilizamos el método try-except para detectar si el valor ingresado no es el esperad, donde en el try pedimos que el usuario ingrese un número y en el except usamos el error ValueError para hacer un print si el usuario ingresa un valor distinto al pedido..

#### 🌱- Ejercicio 3
 Utilizamos el método try-except por si se accede a un elemento de la lista que no existe, donde declaramos una lista vacía y pedimos que la consola ingrese el número de posición que se desea acceder, donde el en try se declara la lista en posición de ese indice y en el except se usa el error IndexError, por si el número es un indice no existente en la lista.

#### 🌱- Ejercicio 4
 Utilizamos el método try-except por si el tipo de variable no corresponde a cierta función, donde declaramos una función de operaciones aritméticas, con dos parametros. En el try llamamos a la función con los parametros correspondientes, con un except que corresponde al error TypeError, por si los parametros no son de valor Int.