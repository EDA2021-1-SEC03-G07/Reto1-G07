"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con más views en un país determinado")
    print("3- Video trending por más días en un país determinado")
    print("4- Video trending por más días para una categoría específica")
    print("5- Videos diferentes con más likes en un país con un tag específico")
    print("0- Salir")

catalog = None

def initCatalog(type_representation):

    return controller.initCatalog(type_representation)

def loadData(catalog):

    controller.loadData(catalog)

def printResults(sortedVideos, sample=10):
    size = lt.size(sortedVideos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son: ")
        i = 1
        while i <= sample:
            video = lt.getElement(sortedVideos, i)
            print('Vistas: ' + video['views'] + ' Título: ' + video['title'] + ' Fecha de tendencia: ' + video['trending_date'] + ' Nombre del canal: ' + 
            video['channel_title'] + ' Hora de publicación: ' + video['publish_time'] + ' Likes: ' + video['likes'] + ' Dislikes ' + video['dislikes'])
            i +=1

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        type_representation = str(input("Seleccione el tipo de representación de la lista: "))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(type_representation)
        loadData(catalog)
        primer_video = controller.firstVideo(catalog)
        print('Videos cargados: ' + str(lt.size(catalog["videos"])))
        print('El primer video es: ')
        print(primer_video)
        print('Categorias cargadas: ' + str(lt.size(catalog["categories"])))
        print(catalog["categories"])

    elif int(inputs[0]) == 2:
        size = input("Indique tamaño de la muestra: ")
        if int(size) > lt.size(catalog['videos']):
            print("El tamaño de la muestra excede el tamaño de los datos cargados en memoria")
        else:
            iterative = input("Indique el tipo de algoritmo de ordenamiento iterativo: ")
            result = controller.sortVideosByViews(catalog, int(size), iterative)
            print("Para la muestra de " , size, " elementos, el tiempo (mseg) es: ", str(result[0]))
            printResults(result[1])
    else:
        sys.exit(0)
sys.exit(0)
