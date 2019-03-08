#!/usr/bin/python
#-*- coding:UTF-8 -*-
import imaplib
import sys
import funciones
import time


# Verificamos que se ingresen los parametros requeridos
try:
    # numero de orden
    orden = sys.argv[1]

    # email cliente
    email = sys.argv[2]

    # nombre cliente
    nombre = sys.argv[3]

except Exception:
    print 'Ingresa los parametros'


# Agregamos un tiempo de espera de 10 segundos, para darle tiempo al correo
# de confirmación de webpay que llegue a nuestro correo
tiempo = 2

# Contador para ejecutar la verificación solo 10 veces
contador = 0

# Iniciamos el tiempo de espera al inicio
time.sleep(tiempo)

# Por lo general, el correo de confirmacion de compra no demora más
# de 20 segundos en llegar, por eso el script se ejecuta 10 veces,
# esperando 10 segundos entre cada verificación
while True:
    # Mensaje de verificación
    print 'Verificación -> %s' % contador

    # verificamos las veces que se ha ejecutado la funcion
    # si son 10, terminamos la ejecución, ya que lo más probable
    # es que hubo un error en la entrega del correo
    if contador == 10:
        # Enviamos una alerta al cliente, haciendo saber
        # que hubo un error en la llegada del correo, por tanto 
        # no se pudo verificar la compra
        funciones.error(nombre,email)

        # Mensaje de verificación
        print 'Pago no verificado'

        # Terminamos la ejecución
        exit(0)

    # Iniciamos sesión en el correo donde webpay nos notifica de una
    # nueva compra
    mail = imaplib.IMAP4_SSL('imap.dominio.com')
    mail.login('nombre@correo.cl', 'contraseña123') 

    # Selección de bandeja de entrada por defecto
    mail.select()

    # Buscamos dentro de los correos sin leer, si ha llegado alguno
    # con el número de orden que se está verificando
    typ, data = mail.search(None, '(NEW BODY "' + orden + '")')

    # Verificamos si se ha encontrado una coincidencia en la búsqueda
    if data[0] != '':
        # Si se ha encontrado el pago, enviamos un mail de confirmación al cliente
        funciones.confirmar(nombre,email)

        # marcar el mensaje como leido en la badeja de entrada
        mail.store(data[0], '+FLAGS', '\SEEN')


        #
        # Aqui tu código
        # 


        # Mensaje de verificación
        print 'Pago verificado'

        # Terminamos la ejecución del programa
        exit(0)

    # cerrar sesion
    mail.close()
    mail.logout()

    # aumentar contador
    contador = contador+1
    
    # Si llega hasta aquí, es porque aún no se encuentra el correo
    # de confirmación, por lo tanto, agregamos un deelay para volver 
    # a verificar el correo electronico
    time.sleep(tiempo)

