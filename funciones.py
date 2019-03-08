#!/usr/bin/python
#-*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText


#
# Datos de conexión desde donde enviaremos el mail de confirmación
#
email    = 'nombre@correo.cl'
password = 'contraseña123'
smtpzoho = 'smtp.dominio.com'


#
# funcion para enviar confirmacion de pago
#
def confirmar(nombre,receptor):
    # Conectamos al correo
    server = smtplib.SMTP_SSL(smtpzoho, 465)
    server.login(email, password)

    # Formamos el mensaje
    mensaje = 'Estimado <b>%s</b>,<br> El pago de tu compra ha sido confirmado' % nombre
    mensaje = MIMEText(mensaje,'html')
    mensaje['Subject'] = 'Pago confirmado'
    mensaje['From'] = email
    mensaje['To'] = receptor

    # Enviamos el correo
    server.sendmail(email, receptor, mensaje.as_string())

    # Cerramos la sesión
    server.quit()


#
# funcion para enviar confirmacion de error en el pago
#
def error(nombre,receptor):
    # Conectamos al correo
    server = smtplib.SMTP_SSL(smtpzoho, 465)
    server.login(email, password)

    # Formamos el mensaje
    mensaje = 'Estimado <b>%s</b>,<br> Hubo un error al verificar el pago, contacta al soporte para solucionar el problema.' % nombre
    mensaje = MIMEText(mensaje,'html')
    mensaje['Subject'] = 'Pago no confirmado'
    mensaje['From'] = email
    mensaje['To'] = receptor

    # Enviamos el correo
    server.sendmail(email, receptor, mensaje.as_string())

    # Cerramos la sesión
    server.quit()