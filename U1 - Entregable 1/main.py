# pip install requests
import requests

# Torrente, el brazo tonto de la ley
r = requests.get('https://www.filmaffinity.com/es/film334167.html')

t = r.text

espacio = '&nbsp;'
dd = '<dd>'
dd_c = '</dd>'
span = '<span>'
span_c = '</span>'
div_c = '</div>'

def tituloOriginal(t):
    label = t[t.find('<dt>Título original</dt>'):t.find(dd_c)]
    tituloOriginal = label[label.find(dd):].splitlines()[1]
    tituloOriginal = tituloOriginal.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = tituloOriginal.find('<span')
    if (find_aka != -1):
        tituloOriginal = tituloOriginal[:find_aka]

    return tituloOriginal

def year(t):
    cadena = '<dd itemprop="datePublished">';
    longitud = len(cadena);
    year = t[t.find('<dd itemprop="datePublished">')+longitud:t.find('<dd itemprop="datePublished">')+longitud+4]

    return year

def duracion(t):
    cadena = '<dd itemprop="duration">';
    longitud = len(cadena);
    duracion = t[t.find(cadena)+longitud:t.find(cadena)+longitud+6]

    return duracion

def pais(t):
    longitud = len(espacio);
    label = t[t.find('<span id="country-img">'):]
    pais = label[label.find(espacio)+longitud:label.find('</dd>')]

    return pais

def direccion(t):
    cadena = '<span itemprop="name">';
    longitud = len(cadena);
    label = t[t.find('<dd class="directors">'):]
    direccion = label[label.find('<span itemprop="name">')+longitud:label.find('</span>')]
    
    return direccion

def guion(t):
    cadena = '<span>';
    longitud = len(cadena);
    label = t[t.find('<dt>Guion</dt>'):]
    guion = label[label.find(cadena)+longitud:label.find('</span>')]

    return guion

def musica(t):
    cadena = '<span>';
    longitud = len(cadena);
    label = t[t.find('<dt>Música</dt>'):]
    musica = label[label.find(cadena)+longitud:label.find('</span>')]

    return musica

def fotografia(t):
    cadena = '<span>';
    longitud = len(cadena);
    label = t[t.find('<dt>Fotografía</dt>'):]
    fotografia = label[label.find(cadena)+longitud:label.find('</span>')]

    return fotografia

def reparto(t):
    cadena = '<span itemprop="name">';
    label = t[t.find('<dt>Reparto</dt>'):]
    label = label[label.find(cadena):label.find('</style>')]

    array = label.split('name')
    array.pop(0)

    reparto = ""

    for i in array:
        reparto += i[2:i.find('</span>')]+", "

    return reparto

def productora(t):
    cadena = '<span>';
    longitud = len(cadena);
    label = t[t.find('<dt>Compañías</dt>'):]
    productora = label[label.find(cadena)+longitud:label.find('</span>')]

    return productora

def genero(t):
    cadena = '<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc">';
    longitud = len(cadena)
    label = t[t.find('<dt>Género</dt>'):]
    label = label[label.find(cadena)+longitud:label.find('</dd>')]

    array = label.split('<a')

    generos = ""

    generos += label[:label.find('</a>')]+", "

    array.pop(0)

    for i in array:
        cadena = 'count&nodoc">'
        longitud = len(cadena)
        generos += i[i.find(cadena)+longitud:i.find('</a>')]+", "

    return generos

def sinopsis(t):
    cadena = '<dd class="" itemprop="description">';
    longitud = len(cadena);
    label = t[t.find('<dt>Sinopsis</dt>'):]
    sinopsis = label[label.find(cadena)+longitud:label.find('</dd>')]

    return sinopsis

diccionario = {
    "titulo_original":tituloOriginal(t),
    "año":year(t),
    "duracion":duracion(t),
    "pais":pais(t),
    "direccion":direccion(t),
    "guion":guion(t),
    "musica":musica(t),
    "fotografía":fotografia(t),
    "reparto":reparto(t),
    "productora":productora(t),
    "genero":genero(t),
    "sinopsis":sinopsis(t)
}

print(diccionario);