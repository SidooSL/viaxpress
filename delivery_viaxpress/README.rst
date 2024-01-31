================
Delivery ViaXpress
================

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1|

Este módulo integra la API de VIAXPRESS LOGISTICS con Odoo.

**Tabla de contenido**

.. contents::
   :local:

Instalación
============

Este módulo necesita la librería python `suds` y depende igualmente de los
módulos de OCA/delivery-carrier `delivery_package_number` y `delivery_state`.

La API de ViaXpress no provee métodos de cálculo de precio.

Configuración
=============

Para configurar el transportista:

#. Diríjase a *Inventario > Configuración > Entrega > Método de envío* y cree uno nuevo.
#. Seleccione *ViaXpress* como proveedor.
#. Configure los datos del servicio que ha contratado.

Para configurar el servicio:

#. Acceda a *Ajustes > Usuarios y Compañías > Compañías* y elija la compañía que utilizará el servicio.
#. En la pestaña *ViaXpress*, complete los datos de acceso al servicio:
    - ID Cliente
    - Usuario
    - Contraseña
    - Host
    - Puerto

    Una vez completados todos los datos, guarde los cambios y pulse el botón *Sincronizar con ViaXpress* para comprobar que la configuración es correcta.
    Este botón también obtendrá los datos que necesite de la API. En caso de fallar, saldrá un mensaje de error.

Uso
=====

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

Seguimiento de errores
===========

Los errores se registran en `GitHub Issues <https://github.com/SidooSL/viaxpress/issues>`_.
En caso de problemas, por favor revisa
allí si tu problema ya ha sido reportado. Si lo descubriste primero, ayúdanos a solucionarlo proporcionando una
descripción detallada y bienvenida.
`feedback <https://github.com/SidooSL/viaxpress/issues/new?body=module:%20delivery_viaxpress%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Creditos
=======

Autores
~~~~~~~

* Sidoo

Colaboradores
~~~~~~~~~~~~

* `Sidoo <https://sidoo.es/>`_:

  * Iván De La Poza

Responsables
~~~~~~~~~~~

Este módulo está siendo mantenido por Sidoo.

.. image:: https://sidoo.es/wp-content/uploads/2023/07/Sidoo_Horizontal.png
   :alt: Sidoo
   :target: https://sidoo.es

