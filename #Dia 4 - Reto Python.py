#Dia 4 - Reto Python
bandera=0
opcion = 0
contador_id = 0
usuarios = []
while (opcion != 5):
    print ( '1. Registrar Nuevo Usuario \n'
            '2. Lista de Usuarios \n'
            '3. Ver Usuario por ID \n'
            '4. Editar Usuario por ID \n'
            '5. Salir \n')
    opcion = int (input('Elija la Opcion a Realizar: '))
    
    if (opcion == 1):
        registros = int (input('Cuantos Usuarios Desea Registrar?: '))\
        
        for i in range(registros):

            # NOMBRE
            nombre = input('Ingresa tu Nombre: ')
            condicion = False
            while (condicion == False):
                num_char = 0
                for caracter in nombre:
                    num_char += 1
                if num_char > 5 and num_char < 50:
                    print('Hecho')
                    condicion = True
                else:
                    print('Error, Longitud minima de 5 caracteres, maxima de 50 caracteres')
                    nombre = input('Vuelva a Ingresar su Nombre: ')
        
            #APELLIDOS
            apellidos = input('Ingrese sus Apellidos: ')
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
                    apellidos = input('Vuelva a Ingresar sus Apellidos: ')

            #NUMERO
            numero    = str(input('Ingrese Su Numero Telefonico: '))
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
                    numero = input('VUelvA a ingresar Su Numero: ')
  
            #CORREO 
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

            print('Hola ' + nombre + ' ' + apellidos  + ' ' + 'en breve recibiras un correo a ' + correo, '\n')
        
            usuario = {
                   'Nombre'     : nombre,
                   'Apellidos'  : apellidos,
                   'Telefono'   : numero,
                   'Correo'     : correo,
            }
            print (usuario)
            contador_id += 1
            print ('Tu Nuevo ID es: ', contador_id, '\n')
            usuarios.append (usuario)
            
        else:
            print('Todos los Registros han sido exitosos \n')
            bandera=1

    if (opcion == 2):
        if (bandera==1):
            for indice,_usuario in enumerate(usuarios):
                print('ID: ', indice+1)
                for key, value in _usuario.items():
                    print ("  " , key, ' = ' ,value)
            print(' ')    
        else:
            print('Aun No Existen Usuarios \n')
    
    if (opcion == 3):
        if(bandera == 1):
            ver = int(input('Que ID desea VER?: ')) - 1
            if(ver >= 0 and ver < len(usuarios)):
                print(usuarios[ver], '\n')                
            else:
                print('El indice No se Encuentra \n')
        else:
            print('Aun No Existen Usuarios \n')

    if (opcion == 4):
        if (bandera == 1):
            editar = int(input('Que ID desea EDITAR?: ')) - 1
            if(editar >= 0 and editar < len(usuarios)):

                #NOMBRE EDITAR
                nombre = input('Ingresa El Nuevo Nombre: ')
                condicion = False
                while (condicion == False):
                    num_char = 0
                    for caracter in nombre:
                        num_char += 1
                    if num_char > 5 and num_char < 50:
                        print('Editado')
                        condicion = True
                    else:
                        print('Error, Longitud minima de 5 caracteres, maxima de 50 caracteres')
                        nombre = input('Vuelva a Ingresar el Nuevo Nombre: ')

                #APELLIDOS EDITAR
                apellidos = input('Ingrese los Nuevos Apellidos: ')
                ondition = False
                while ( condition == False):
                    num_char  = 0
                    for caracter in apellidos:
                        num_char +=1
                    if num_char > 5 and num_char < 50:
                        print('Hecho')
                        condition = True
                    else:
                        print('Error, Longitud minima de 5 caracteres, maxima de 50 caracteres')
                        apellidos = input('Vuelva a Ingresar Nuevos Apellidos: ')   

                #NUMERO       
                numero    = str(input('Ingrese el Nuevo Numero Telefonico: '))
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
                        numero = input('VUelvA a ingresar Nuevo Numero: ')      

                #CORREO EDITAR
                correo    = input('Ingresa el Nuevo Correo Electronico: ')
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
                        correo = input('VUelve a ingresar Nuevo correo: ')   

                print('Usuario Editado Exitosamente! \n')
            
                usuarios[editar] = {
                   'Nombre'     : nombre,
                   'Apellidos'  : apellidos,
                   'Telefono'   : numero,
                   'Correo'     : correo,
                }     
            else:
                print('El indice No se Encuentra \n')
        else:
            print('Aun No Existen Usuarios \n')
print('Hasta pronto!')