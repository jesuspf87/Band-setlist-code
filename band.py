import random

print("Bienvenido, ingresa tu usuario")
banda = input("Ingresa nombre: ")

print("Hola", banda, "¿dónde tocarán?")
local = input("Ingresa nombre del local: ")

print(banda, "tocará en", local)

set_espanol = ["Donde estan los ladrones", "Yo pa ti no estoy", "La mordidita", "11 y 6", "Mi enfermedad", "Tu recuerdo", "Sin documentos", "Flaca", "Deseos de cosas imposibles", "la otra de fito", "La bestia pop", "Corazon espinado", "Mil horas", "Tu sin mi", "Cae el sol", "Contigo a la distancia", "Genio en la botella"]
set_ingles = ["Rehab", "You know im not good", "Rolling in the deep", "She will be love", "Sunday morning", "Toxic", "This love", "Take on me", "I want it that way", "New rules", "Dont speak", "Zombie", "White flag"]
set_mixto = set_espanol + set_ingles

print("Selección del set:")
print("1) Español")
print("2) Inglés")
print("3) Mixto")

select = int(input("Seleccione el set: "))

if select == 1:
    while True:
        set_esp = random.sample(set_espanol, k=9)
        for i, esp in enumerate(set_esp):
            print(f"{i+1}. {esp}")
        print(banda, "este es tu set en español")
        ok_set = int(input("1) Ok 2) Repetir: "))
        if ok_set == 1:
            print("Buen set", banda, "¡Vamos arriba!")
            break
        elif ok_set == 2:
            continue
        else:
            print("Opción inválida")
elif select == 2:
    while True:
        set_eng = random.sample(set_ingles, k=9)
        for i, eng in enumerate(set_eng):
            print(f"{i+1}. {eng}")
        print(banda, "este es tu set en inglés")
        ok_set = int(input("1) Ok 2) Repetir: "))
        if ok_set == 1:
            print("Buen set", banda, "¡Vamos arriba!")
            break
        elif ok_set == 2:
            continue
        else:
            print("Opción inválida")
elif select == 3:
    while True:
        set_mix = random.sample(set_mixto, k=9)
        for i, mix in enumerate(set_mix):
            print(f"{i+1}. {mix}")
        print(banda, "este es tu set mixto")
        ok_set = int(input("1) Ok 2) Repetir: "))
        if ok_set == 1:
            print("Buen set", banda, "¡Vamos arriba!")
            break
        elif ok_set == 2:
            continue
        else:
            print("Opción inválida")
else:
    print("Opción inválida")

#Cobro del toque y reparto al grupo

print("Calculemos cobro")

pago_banda = int(input("Ingrese cobro del toque: "))

print("El local paga: ", pago_banda)

miembros = 0

print("Calculemos pago individual: ")

miembros = int(input("Cuantos conforman la banda: "))

pago_miembros = pago_banda / miembros

print("El total a cada uno es:", pago_miembros)




