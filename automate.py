#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)

def inicializaBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def definePinoComoSaida(numeroPino):
    GPIO.setup(numeroPino, GPIO.OUT)

def escreveParaPorta(numeroPino, estadoPorta):
    GPIO.output(numeroPino, estadoPorta)
