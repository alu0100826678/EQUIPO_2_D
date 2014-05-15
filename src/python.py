from sympy import *
import sys
import time


def fac(grado):
  if grado == 0:
    return 1
  else:
    return grado * fac(grado-1)

def taylor(grado, punto, centro):
  Ti=time.time()
  c = Symbol('c')
  funcion = ln(c)
  suma = funcion.evalf(subs={c:centro})
  for i in range(1,grado+1):
    deriv = diff(funcion, c)
    termino = (deriv.evalf(subs={c:centro})/fac(i))*((punto-centro)**i)
    funcion = deriv
    suma += termino
  return suma
  error = funcion- suma
  Tf=time.time() 
  tiempo= Tf-Ti
grado = int(raw_input('Introduzca el grado en el que desea que se aplique el desarrollo de Taylor: '))
punto = float(raw_input('Introduzca el punto en el que desea que se aplique el desarrollo de Taylor: '))
centro = float(raw_input('Introduzca el centro en el que desea que se aplique el desarrollo de Taylor: '))
suma = taylor(grado, punto, centro)
print 'El polinomio de Taylor es: ', suma
Ti=time.time()
Tf=time.time() 
tiempo= Tf-Ti
print 'Tiempo: ', tiempo
