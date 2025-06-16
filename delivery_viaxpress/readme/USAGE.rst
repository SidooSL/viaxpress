Estas son las distintas operaciones posibles con este módulo:

Grabar servicios
~~~~~~~~~~~~~~~~

  #. Al confirmar el albarán, el servicio se grabará en ViaXpress.
  #. Con la respuesta, se registrará en el chatter la referencia de envío y
     las etiquetas correspondientes.
  #. Para gestionar los bultos del envío, se puede utilizar el campo de número
     de bultos que añade `delivery_package_number` (ver el README para mayor
     información) o bien el flujo nativo de Odoo con paquetes de envío. El
     módulo mandará a la API de ViaXpress el número correspondiente y podremos
     descargar las etiquetas en PDF con su correspondiente numeración.

Obtener etiquetas
~~~~~~~~~~~~~~~~~~

  #. Una vez validado el envío, en el chatter aparecerá adjunto el PDF con las
     etiquetas de los bultos del envío.



