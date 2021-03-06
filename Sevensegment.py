#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      tecnico@fryntiz.es
# @web        www.fryntiz.es
# @github     https://github.com/fryntiz
# @gitlab     https://gitlab.com/fryntiz
# @twitter    https://twitter.com/fryntiz

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################
# Esta clase crea un nuevo objeto al que se puede acceder para controlar la
# pantalla de 7 segmentos, 8 dígitos con el chip MAX7219 mediante los métodos
# aquí definidos simplificando el trabajo y haciéndolo más accesible.

#######################################
# #       Importar Librerías        # #
#######################################

# Librerías del sistema
import time  # Importamos la libreria time --> time.sleep
from datetime import datetime

# Librerías específicas
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

#######################################
# #             Variables           # #
#######################################
sleep = time.sleep

#######################################
# #               CLASE             # #
#######################################


class Sevensegment:

    def __init__(self, c=1, p=0, d=0):
        """
        Constructor de la clase para crear un nuevo objeto display de 7
        segmentos con métodos fácilmente accesibles y opcionales.
        :param c: Cantidad de dispositivos en cascada.
        :param p: Puerto del dispositivo.
        :param d: Dispositivo.
        """
        self.cascaded = c  # Cantidad de dispositivos en cascada

        self.serial = spi(port=p, device=d, gpio=noop())
        self.device = max7219(self.serial, cascaded=c)
        self.seg = sevensegment(self.device)

    def fecha(self):
        """
        Muestra la fecha actual en el dispositivo
        """
        fecha_ahora = datetime.now().strftime('%d-%m-%y')
        self.seg.text = fecha_ahora

    def hora(self):
        """
        Muestra la hora actual
        """
        hora_actual = datetime.now().strftime('%H-%M-%S')
        self.seg.text = hora_actual

    def mostrarMensajeFlotante(self, txt, delay=1):
        """
        Muestra un mensaje como animación recorriendo la pantalla de forma que
        entra por la derecha y sale por la izquierda, útil cuando no cabe al
        completo el texto por ser un mensaje largo conviertiéndolo previamente
        a mayúsculas.
        :param txt: Texto a mostrar por la pantalla
        :param delay: Tiempo entre carácteres para desplazar el mensaje
        """
        width = self.device.width
        padding = " " * width
        txt = padding + txt.upper() + padding
        n = len(txt)

        print("Mostrando mensaje:\n"+txt)

        virtual = viewport(self.device, width=n, height=8)
        sevensegment(virtual).text = txt
        for i in reversed(list(range(n - width))):
            virtual.set_position((i, 0))
            sleep(delay)

    def mostrarMensajeFlotante2(self, txt, delay=1):
        """
        Muestra el mensaje flotante pero cortando la cadena por si misma,
        similar al anterior
        :param txt: El texto a mostrar por la pantalla
        :param delay: Tiempo entre iteraciones
        """
        width = self.seg.device.width
        padding = " " * width
        txt = padding + txt.upper() + padding

        for i in range(len(txt)):
            self.seg.text = txt[i:i + width]
            sleep(delay)

    def mostrar(self, txt):
        """
        Muestra un texto fijo en la pantalla sin ninguna animación. En caso de
        ser superior a la cantidad de dígitos entre todas las pantallas en
        cascada, no se mostrará el mensaje.
        :param txt: Mensaje a mostrar por la pantalla
        """
        if len(txt) <= (8 * self.cascaded):
            self.seg.text = txt.upper()
        else:
            print('Supera la longitud')

    def brillo(self, n):
        """
        Ajusta el brillo de la pantalla al valor indicado. Este se convertirá a
        hexadecimal por lo que el rango válido será desde 0-15.
        :param n: Valor del brillo en rango de 0-15.
        """
        if n in range(16):
            print('Ajustando Brillo a ' + str(n))
            self.seg.device.contrast(n * 16)
        else:
            print('Valor de Brillo indicado no correcto, solo del 0-15')
