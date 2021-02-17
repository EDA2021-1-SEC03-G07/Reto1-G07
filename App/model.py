"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"videos" : None, "categories" : None}
    catalog["videos"] = lt.newList('ARRAY_LIST', cmpfunction=comparevideos)
    catalog["categories"] = lt.newList('ARRAY_LIST', cmpfunction=comparecategories)

    return catalog 

# Funciones para agregar informacion al catalogo

def addVideo(catalog, videoname):

    lt.addLast(catalog["videos"], videoname)
    
def addCategory(catalog, category):

    c = newCategory(category["name"], category["id"])
    lt.addLast(catalog["categories"], c)


# Funciones para creacion de datos
    

def newCategory(name, id):

    category = {"category_name": "", "category_id": ""}
    category["category_name"] = name
    category["category_id"] = id
    return category



# Funciones de consulta

def firstVideo (catalog):

    lista = catalog["videos"]
    primer_video = lt.firstElement(lista)
    title = primer_video["title"]
    channel = primer_video["channel_title"]
    trending_date = primer_video["trending_date"]
    country = primer_video["country"]
    views = primer_video["views"]
    likes = primer_video["likes"]
    dislikes = primer_video["dislikes"]

    video = {"title": title, "channel_title": channel, "trending_date": trending_date, "country": country, "views": views, "likes": likes, "dislikes": dislikes}

    return video

# Funciones utilizadas para comparar elementos dentro de una lista

def comparevideos(videotitle1, video):

    if (videotitle1.lower() in video["title"].lower()):
        return -1

def comparecategories(name, category):

    return (name==category["category_name"])


# Funciones de ordenamiento