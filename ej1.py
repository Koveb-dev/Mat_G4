# PROBLEMA 1:


# EJ 1.1
l_terminos = []


for x in range(1, 6):
    f = 3 * x**2 + 7
    l_terminos.append(f)


print(
    f'\nLos primeros 5 terminos de la sucesion 3 * n elevado a 2 + 7 son: {l_terminos}')

# EJ 1.2

l_terminos2 = []
for t in range(16, 21):
    j = 3 * t**2 + 7
    l_terminos2.append(j)


print(
    f'\nLos 5 terminos  que vienen despues del decimo quinto temrino de la sucesion 3 * n elevado a 2 + 7 son: {l_terminos2}')


# PROBLEMA 2:

# EJ 2.1 Y EJ 2.2

l1_terminos_p2 = []
l2_terminos_p2 = []
for d in range(1, 13):
    g = 5*d**3
    if (d <= 4):
        l1_terminos_p2.append(g)
    elif (d >= 9):
        l2_terminos_p2.append(g)


print(
    f"\nLos primeros 4 terminos de la sucesión de 5*n**3 son: {l1_terminos_p2}")

print(
    f"\nLos 4 terminos que vienen inmediatamente despues del octavo termino son: {l2_terminos_p2}")

# EJ 2.3

# valor = 40000

# for b in range(30):
#     gn = 5*b**3

#     if (gn == valor):
#         pos = b
#         print(
#             f'\nEl termino 40.000 si pertenece a la sucesión, y se encuentra en la posicion: {pos}')
#         break
#     else:
#         print('\nEl termino 40.000 no pertenece a la sucesión!')

# EJ 2.3 VERS.MEJOR
x = 0
while True:
    if (5*x**3 == 40000):
        print(
            f'\nEl termino 40.000 si pertenece a la sucesión, y se encuentra en la posicion: {x}')
        break
    elif (5*x**3 > 40000):
        print('\nEl termino 40.000 no pertenece a la sucesión!')
        break

    x = x+1


# PROBLEMA 3:

# EJ 3.1
l_fibonacci = []
n1 = 0
n2 = 1

while True:
    if (len(l_fibonacci) == 30):
        break
    else:

        if (len(l_fibonacci) == 0):
            l_fibonacci.append(n1)
            l_fibonacci.append(n2)
            l_fibonacci.append(1)

        for x in range(len(l_fibonacci)):
            if (l_fibonacci[-1] + l_fibonacci[-2] == 2):
                l_fibonacci.append(2)
                break
            elif (l_fibonacci[-1] + l_fibonacci[-2] > l_fibonacci[-1]):
                l_fibonacci.append(l_fibonacci[-1] + l_fibonacci[-2])
                break

l_fibonacci_20_ter = []

for l in range(len(l_fibonacci)):
    if l < 20:
        l_fibonacci_20_ter.append(l_fibonacci[l])
    else:
        print(
            f"\nLos primeros 20 números de la sucesión son: {l_fibonacci_20_ter} ")
        break

# EJ 3.2
suma = 0
for i in range(len(l_fibonacci)):
    suma = suma + l_fibonacci[i]

print(
    f'\nLa suma de los primeros 30 terminos de la sucesion de Fibonacci es: {suma}')


# PROBLEMA 4:

# EJ 4.1

l_pares = []

num = 0
while True:

    if (len(l_pares) == 10):
        break
    else:
        num = num + 1
        if (num % 2 == 0):
            l_pares.append(num)

print(f'\nel valor del décimo término es: {l_pares[-1]}')


# EJ 4.2
nro = 0
suma = 0
l_nropares = []
while True:
    if (len(l_nropares) == 100):
        break
    else:
        nro = nro + 1
        if (nro % 2 == 0):
            l_nropares.append(nro)
            suma = suma + nro

print(f"La suma de los 100 numeros pares {l_nropares}\n\t es: {suma}")

# EJ 4.3

for e_nro in l_nropares:
    if (e_nro == 58):
        posicion = l_nropares.index(e_nro)
        print(
            f"La posición donde se encuentra el numero 58 en la lista es: {posicion+1}")


# PROBLEMA 5:


# EJ 5.1
def cant_usuarios(cant_meses):
    usuarios_ini = 500
    return int(usuarios_ini*(1+0.15)**cant_meses)


print(
    f"\nLa cantidad de usuarios que tendra el software dentro de 6 meses sera de: {cant_usuarios(3)}")

print(
    f"\nLa cantidad de usuarios que tendra el software dentro de 6 meses sera de: {cant_usuarios(6)}")


# EJ 5.2
def cant_usuarios_meses(cant_mes):
    usuarios = 500
    for d in range(1, cant_mes+1):
        print(
            f"El {d} mes el software tendra {int(usuarios*(1+0.15)**d)} usuarios")


cant_usuarios_meses(12)


# EJ 5.3
def cant_usuarios_anio():
    suma = 0
    usuarios = 500
    for x in range(1, 13):
        suma = suma + (int(usuarios*(1+0.15)**x))

    return suma


print(
    f"\nLa cantidad de usuarios que tendra el software luego de un año sera de {cant_usuarios_anio()}\n")


# PROBLEMA 6:

# EJ 6.1
def deposito_mensuales():
    deposito_ini = 12000
    incremento = 2000
    for v in range(1, 13):
        if v == 1:
            print(f"El 1 mes deposito ${deposito_ini}\n")
        else:
            deposito_ini = deposito_ini + incremento
            print(f"El {v} mes deposito ${deposito_ini}\n")


deposito_mensuales()


# EJ 6.2

def deposito_febrero():
    deposito = 12000
    incremento = 2000
    for x in range(1, 15):
        if x != 1:
            deposito = deposito + incremento

        if x == 14:
            print(f"\nEn febrero del segundo año deposito ${deposito}")


deposito_febrero()


# EJ 6.3


def total_2_years():
    deposito = 12000
    incremento = 2000
    total = 0
    for x in range(1, 25):
        if x == 1:
            total = total + deposito
        if x != 1:
            deposito = deposito + incremento
            total = total + deposito
    print(f"\nEl total ahorrado al finalizar los 2 años sera de ${total}")


total_2_years()


# PROBLEMA 7


# EJ 7.1 VERS.MEJOR
l_fases = []
fase = 0
for x in range(0, 16, 3):
    if x != 0:
        if x == 3:
            fase = 3
            l_fases.append(fase)
        else:
            fase = round(fase - (fase*0.10), 1)
            l_fases.append(fase)

print(f"\nLa quinta fase dura: {l_fases[4]}")

# EJ 7.2 VERS.MEJOR


def duracion_total():
    acumu = 0
    fase = 3
    for x in range(1, 11):
        if x == 1:
            acumu = acumu + fase
        else:
            fase = round(fase - (fase*0.10), 1)
            acumu = round(acumu + fase, 1)

    print(
        f"\nLa duracion total del proyecto despues de 10 fases es: {acumu}")


duracion_total()

# l_10_fases = []
# fase_t = 0
# suma = 0
# for x in range(1, 12):
#     if x == 1:
#         fase_t = 3
#     else:
#         fase_t = round(fase - (fase*0.10), 2)
#         l_10_fases.append(fase_t)

# for n in range(len(l_10_fases)):
#     if (n == 0):
#         suma = suma + l_10_fases[n]
#     else:
#         suma = suma + l_10_fases[n]

# print(
#     f"\nLa duración total del proyecto despues de 10 fases es: {suma}")

# for x in range(1, 6):
#     if x == 1:
#         fase1_duracion = 3
#         print(
#             f"La fase nro {x} tiene una duracion de: {fase1_duracion}")
#     if x != 1:
#         fase1_duracion = fase1_duracion - (fase1_duracion * 0.10)
#         print(
#             f"La fase nro {x} tiene una duracion de: {fase1_duracion}")


# quinta_fase(5)

# fase1 = 90
# reduc = 10
# for x in range(1, nro_fases+1):
#     if (x == 2):
#         fase1 = fase1 - (fase1 / reduc)
#         nuevaf = fase1


# PROBLEMA 8:

# EJ 8.1
def p1_termino():
    lista_sucesion = [-20]
    num = -20
    while True:
        num = num - 4
        if (len(lista_sucesion) == 10):
            break
        else:
            lista_sucesion.append(num)

    print(f'\nEl primer término de la sucesión es: {lista_sucesion[9]}')


p1_termino()

# EJ 8.2: EXPRESION??

# EJ 8.3:


def termino_pos_100():
    lista_suces = [-56]
    p1Ter = -56
    while True:
        p1Ter = p1Ter + 4
        if (len(lista_suces) == 100):
            break
        else:
            lista_suces.append(p1Ter)

    print(f"\nEl término que ocupa el lugar 100 es: {lista_suces[99]}")


termino_pos_100()


def pos_num1680():
    lista = [-56]
    while True:
        sucesion = lista[-1] + 4
        if (lista[-1] == 1680):
            pos = lista.index(1680)
            break
        else:
            lista.append(sucesion)

    print(f"\nLa posicion del número 1680 en la secuencia es: {pos+1}")


pos_num1680()


# PROBLEMA 9:

# EJ 9.1


def razon_geometrica():
    t3 = 5
    t6 = 40
    r = (t6 / t3)**(1/3)
    print(f'\nRazon constante de la sucesion geometrica es: {r}')


razon_geometrica()

# EJ 9.2


def primer_octavoTerm_pos20480():

    # 9.2
    p3 = 5.0
    p6 = 40
    lista_terminos = [p3]
    while True:
        # primero encontrar que nro es r
        # por lo que al empezar en el tercer termino que es 5 debemos encontrar la sucesion que hace que el termino sexto sea 40:
        # el r(numero), encontre que 2 da la sucesion geometrica en este caso
        n = lista_terminos[-1] * 2

        if (len(lista_terminos) == 4):
            break
        else:
            if n <= p6:
                lista_terminos.append(n)

                # agrego los terminos  que se obtenga en una lista, despues del tercer termino hasta que este sea igual al sexto termino(40)
                # teniendo el 4to termino,5to termino y 6to termino en la lista. Ahora dividire el 4to con el tercer termino para si encontrar la razon y llegar a encontrar el 1er termino con el segundo termino
                # ya que voy a dividir 4to termino con su antecesor que es el tercer termino y lo agregare a la lista. ya por ultimo cuando lista tenga un maximo de 6 terminos entonces esta ya
                # habra encontrado el primer termino.

    while True:
        if (len(lista_terminos) == 6):
            break
        else:
            r = lista_terminos[0] / 2
            lista_terminos.insert(0, r)

    print(f'\nEl primer termino de  la sucesión es: {lista_terminos[0]}')

    # 9.3
    while True:
        if (len(lista_terminos) == 8):
            break
        else:
            x = lista_terminos[-1] * 2
            lista_terminos.append(x)

    print(f'\nEl termino que ocupa el lugar 8 es: {lista_terminos[-1]}')

    # 9.5
    while True:
        if (20480 in lista_terminos):
            pos = lista_terminos.index(20480)
            break
        else:
            i = lista_terminos[-1] * 2
            lista_terminos.append(i)

    print(f"\nEl lugar que ocupa la sucesión el termino 20480 es: {pos+1}")


primer_octavoTerm_pos20480()


#  PROBLEMA 10


def rendimiento_novenoMes():

    # EJ 10.1

    p1_termino = round(1.2 / 1.31, 2)
    l_rendimientoMes = [p1_termino, 1.2]

    while True:
        if (len(l_rendimientoMes) == 9):
            break
        else:

            sucesionMeses = round(l_rendimientoMes[-1] * 1.31, 3)
            l_rendimientoMes.append(sucesionMeses)

    print(
        f"\nEl rendimiento del noveno mes es: {round(l_rendimientoMes[-1], 2)}")

    # EJ 10.2
    while True:
        if (23.41 in l_rendimientoMes):
            pos = l_rendimientoMes.index(23.41)
            break
        else:
            sM = round(l_rendimientoMes[-1] * 1.31, 2)
            l_rendimientoMes.append(sM)
            print(l_rendimientoMes)

    print(f"\n El mes que el rendimiento fue de 23.4 tps es el {pos+1} mes")


rendimiento_novenoMes()
