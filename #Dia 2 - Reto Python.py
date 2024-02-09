#Dia 2 - Reto Python

registros    = int (input('Cuantos Registros deseas hacer?: '))

for i in range(registros):

   
    nombre    = input('Ingresa tu Nombre: ')
    condition = False
    while ( condition == False):
        num_char  = 0
        for caracter in nombre:
            num_char += 1
        if num_char > 5 and num_char < 50:
            print('Hecho')
            condition = True
        else:
            print('Error, Longitud minima de 5 caracteres, maxima de 50 caracteres')
            nombre = input('Vuelve a Ingresar tu Nombre: ')

    apellidos = input('Ingresa tus Apellidos: ')
    condition = False
    while ( condition == False):
        num_char  = 0
        for caracter in apellidos:
            num_char +=1
        if num_char > 5 and num_char < 50:
            print('Hecho')
            condition = True
        else:
            print('Error, Longitud minima de 5 caracteres, maxima de 50 caracteres')
            apellidos = input('Vuelve a Ingresar tus Apellidos: ')


    numero    = str(input('Ingresa tu Numero Telefonico: '))
    condition = False
    while ( condition == False):
        num_char  = 0
        for caracter in numero:
            num_char +=1
        if num_char == 10:
            print('Hecho')
            condition = True
        else:
            print('Error, El numero debe tener 10 caracteres')
            numero = input('VUelve a ingresar tu Numero: ')
  

    correo    = input('Ingresa tu Correo Electronico: ')
    condition = False
    while ( condition == False):
        num_char  = 0
        for caracter in correo:
            num_char +=1
        if num_char > 5 and num_char < 50:
            print('Hecho')
            condition = True
        else:
            print('Error, El correo debe tener de 5 a 50 caracteres')
            correo = input('VUelve a ingresar tu correo: ')


    print('Hola ' + nombre + ' ' + apellidos  + ' ' + 'en breve recibiras un correo a ' + correo)

else:
    print('Todos los Registros han sido exitosos')