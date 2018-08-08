# raspberry-MAX7219

Instalación y librerías personalizadas para display de 7 segmentos (8 dígitos) con el chip MAX7219 en Raspberry y Raspbian Estable

Esta herramienta facilita el acceso, instalación y manipulación de pantallas
con el chip max7219

## Instalar librerías en Raspbian desde PyPy
Para instalar la librería debemos tener instalado pip y python.

### Para python =2.7

```bash
    pip install Pillow
    sudo -H pip install --upgrade luma.led_matrix
```

### Para python >=3.4

```bash
    pip3 install Pillow
    sudo -H pip3 install --upgrade luma.led_matrix
```

Para otros modos de instalación o/y contemplar otros sistemas operativos
tendrás que consultar la fuente oficial del autor para la librería usada, esta
información la puedes encontrar un poco más abajo.


## Modo de uso

Para usar esta clase de apoyo solo necesitamos el archivo "Sevensegment.py" e
instanciarlo. Una vez realizado esto ya podemos acceder a los métodos
simplificados que he creado para hacer aún más accesible estas pantallas.

Para ello lo importamos:

```Python
    from Sevensegment import  Sevensegment
```

Y una vez importado ya podemos crear un objeto a partir de el, sería algo
similar a lo siguiente:

```Python
    ss = Sevensegment()
```

Ya sería posible acceder a sus métodos como por ejemplo pintando la fecha:
```Python
    ss.fecha()
```

### Métodos de Sevensegment.py

- fecha() → Muestra la fecha
- hora() → Muestra la hora
- mostrarMensajeFlotante(texto, delay) → Mensaje desde la derecha hacia
izquierda
- mostrarMensajeFlotante2(texto, delay) → Mensaje similar al anterior
- mostrar(texto) → Muestra un mensaje fijo
- brillo(n) → Cambia la intensidad del brillo, valores del 0-15


### Pines GPIO

Los pines para una Raspberry PI con este tipo de display sigue este esquema:

|   Board Pin  |     Name     |    Remarks   |    RPi Pin   | RPi Function |
| :----------: | :----------: | :----------: | :----------: | :----------: |
|      4       |     VCC      |   +5V Power  |      -       |     5V0      |
|      6       |     GND      |    Ground    |      -       |     GND      |
|      19      |     DIN      |    Data In   |      10      |    MOSI      |
|      24      |     CS       |  Chip Select |      8       |   SPI CE0    |
|      23      |     CLK      |     Clock    |      11      |   SPI CLK    |


## Librería usada

https://github.com/rm-hull/luma.led_matrix


## Documentación de la librería oficial

https://luma-led-matrix.readthedocs.io/en/latest/api-documentation.html#module-luma.led_matrix.device
