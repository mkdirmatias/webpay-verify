# Descripción

Los botones de pago de Webpay son una solución rápida y efectiva para vender en internet, la unica desventaja es que los pagos se deben verificar de forma manual, por ello hice este script que permite al momento de que se realiza el pago en la plataforma de webpay, verificar mediante el correo donde nos llegan las notificaciones de una nueva compra (definido en el panel de notificacion de webpay)

# Uso

El script debe ser llamado desde el backend en segundo plano, en el momento que webpay redirecciona al cliente a nuestra web y mostramos los datos de pago, por ejemplo:

![Verificacion del pago](https://i.imgur.com/kWE0nPv.png)

El script hace uso del numero de orden de compra, funciona de la siguiente forma:

- Realizado el pago, se llama al script desde el backend 
- El script inicia sesión en el correo de notificaciones
- Busca en los mensajes sin leer, si  existe alguno con la orden de compra 
- De existir, envía un correo de confirmacion al cliente
- De no existir, el script hace una comprobación del mail 10 veces, con 10 segundos entre cada comprobación. Lo normal es que el correo de confirmación no llegue en más de 20 segundos. Pasadas las 10 comprobaciones, si no se encuentra el mail, se envía una notificacion al cliente de que no se pudo verificar el pago, por ende que contacte al soporte de la web.

# Ejemplo

El script debe ser llamado desde el backend en segundo plano de la siguiente forma:

```bash
python verificar.py 'numero_orden' 'email_cliente' 'nombre_cliente'
```

![Ejemplo](https://i.imgur.com/oYU9n4Q.png)

Para obtener el email del cliente, lo forzamos a ingresarlo en el boton de webpay

![Email cliente](https://i.imgur.com/LilvSJQ.png)

