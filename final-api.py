import mysql.connector
from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def encodeAndString(foto):
   foto = str(base64.b64encode(foto))
   foto = foto[2:-1]
   return foto

Foto = convertToBinaryData("/Users/apps2m/Desktop/EscritorioCarpeta/ImagenesApi/default-non-user-no-photo-1.jpeg")


mydb = mysql.connector.connect(
  user="", 
  password="", 
  host="", 
  port="", 
  database=""
)

mycursor = mydb.cursor()
mycursorPeli = mydb.cursor()
nombreAparicion = []
listaProvisional = []
listaUsuario = []
usuarioElegido = []
musicaElegidaLista = []
musicaMostrarLista = []


idFav = 0
favStr = ""

mycursor.execute("SHOW TABLES FROM railway")
myresult = mycursor.fetchall()
mydb.commit()

"""
mycursor.execute("CREATE TABLE IF NOT EXISTS Serie (IDSerie INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Director VARCHAR(255), Protagonista VARCHAR(255), DescripcionCorta VARCHAR(750), Temporadas INT(4), Episodios INT(5), FotoDeSerie LONGBLOB,AnoDePublicacion INT(5), Duracion VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Pelicula (IDPelicula INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Director VARCHAR(255), Protagonista VARCHAR(255), DescripcionCorta VARCHAR(750), FotoDePelicula LONGBLOB, AnoDePublicacion INT(5), Duracion VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Musica (IDMusica INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Cantante VARCHAR(255), FotoDeMusica LONGBLOB, MultimediaDeAparición VARCHAR(255), Grupo VARCHAR(255), AnoDePublicacion INT(5), Duracion VARCHAR(10), EnlaceYoutube VARCHAR(255),EnlaceAmazon VARCHAR(255),EnlaceItunes VARCHAR(255),EnlaceSpotify VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Usuario (IDUsuario INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), FotoDePerfil LONGBLOB, Contrasena VARCHAR(255), DNI VARCHAR(255), TipoDeCuenta VARCHAR(255), FechaDeNacimiento VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Cantante (IDCantante INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Grupo VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Grupo (IDGrupo INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Cantante VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Reparto (IDReprto INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Rol VARCHAR(255))")
mydb.commit()
"""

@app.route("/")
def home():
    return "Bienvenido a la API REST en Flask"

@app.route("/api/serie", methods=["GET"])
def obtener_serie():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Serie")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "director": myresult[i][3],
                "protagonista": myresult[i][4],
                "descripcionCorta": myresult[i][5],
                "temporadas": myresult[i][6],
                "episodios": myresult[i][7],
                "foto": encodeAndString(myresult[i][8]),
                "anoDePublicacion": myresult[i][9],
                "duracion": myresult[i][10],
                "enLista": myresult[i][11],
                "imagenPaisaje": encodeAndString(myresult[i][12])
             })
    return jsonify(listaProvisional)


@app.route("/api/pelicula", methods=["GET"])
def obtener_pelicula():
    listaProvisional.clear()
    mycursorPeli.execute("SELECT * FROM Pelicula")
    myresult = mycursorPeli.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "director": myresult[i][3],
                "protagonista": myresult[i][4],
                "descripcionCorta": myresult[i][5],
                "foto": encodeAndString(myresult[i][6]),
                "anoDePublicacion": myresult[i][7],
                "duracion": myresult[i][8],
                "enLista": myresult[i][9],
                "imagenPaisaje": encodeAndString(myresult[i][10])
                
             })
    return jsonify(listaProvisional)

@app.route("/api/musica", methods=["GET"])
def obtener_musica():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Musica WHERE Nombre = '" + musicaElegidaLista[0] + "'")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "cantante": myresult[i][3],
                "foto": encodeAndString(myresult[i][4]),
                "aparicion": myresult[i][5],
                "momentoAparicion": myresult[i][6],
                "grupo": myresult[i][7],
                "anoDePublicacion": myresult[i][8],
                "duracion": myresult[i][9],
                "enlaceYoutube": myresult[i][10],
                "enlaceAmazon": myresult[i][11],
                "enlaceItunes": myresult[i][12],
                "enlaceSpotify": myresult[i][13],
                "favorito": myresult[i][14]
             })
    return jsonify(listaProvisional)

@app.route("/api/usuario", methods=["GET", "POST"])
def obtener_usuario():
    if request.method == "GET":
        listaUsuario.clear()
        mycursor.execute("SELECT * FROM Usuario")
        myresult = mycursor.fetchall()
        for i in range (0, len(myresult)):
            listaUsuario.append(
                {
                    "id": myresult[i][0],
                    "nombre": myresult[i][1],
                    "genero": myresult[i][2],
                    "foto": encodeAndString(myresult[i][3]),
                    "contrasena": myresult[i][4],
                    "DNI": myresult[i][5],
                    "tipoDeCuenta": myresult[i][6],
                    "fechaDeNacimiento": myresult[i][7]
                 })
        return jsonify(listaUsuario)
    

    if request.method == "POST":
        usuario = { 
        "nombre" : request.json["nombre"],
        "foto" : encodeAndString(Foto),
        "contrasena" : request.json["contrasena"],
        "fechaDeNacimiento" : request.json["fechaDeNacimiento"]}
        sql = "INSERT INTO Usuario (Nombre, Genero, FotoDePerfil, Contrasena, DNI, TipoDeCuenta, FechaDeNacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = [(request.json["nombre"], "no binario", Foto, request.json["contrasena"], "12345678X", "Premium", request.json["fechaDeNacimiento"])]
        mycursor.executemany(sql, val)
        mydb.commit()

        return jsonify(listaUsuario)
    
    else:
        return jsonify(listaUsuario)

@app.route("/api/cantante", methods=["GET"])
def obtener_cantante():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Cantante")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "grupo": myresult[i][2]
             })
    return jsonify(listaProvisional)

@app.route("/api/grupo", methods=["GET"])
def obtener_grupo():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Grupo")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "cantante": myresult[i][2]
             })
    return jsonify(listaProvisional)
    

@app.route("/api/reparto", methods=["GET"])
def obtener_reparto():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Reparto")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "rol": myresult[i][2]
             })
    return jsonify(listaProvisional)


@app.route("/api/usuarioElegido", methods=["GET", "POST"])
def obtener_usuarioElegido():
    if request.method == "POST":
        usuarioElegido.clear()
        usuario = { 
        "id" : request.json["id"],
        "nombre" : request.json["nombre"]
        }
        usuarioElegido.append(usuario)
        print(usuarioElegido)
        return jsonify(usuarioElegido)


    if request.method == "GET":
        usuario = { 
        "id" : usuarioElegido[0],
        "nombre" : usuarioElegido[0]
        }
        print(usuarioElegido)
        return jsonify(usuarioElegido)


@app.route("/api/serieRapida", methods=["GET"])
def obtener_serieRapida():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Serie")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "director": myresult[i][3],
                "protagonista": myresult[i][4],
                "descripcionCorta": myresult[i][5],
                "temporadas": myresult[i][6],
                "episodios": myresult[i][7],
                "foto": encodeAndString(myresult[i][8]),
                "anoDePublicacion": myresult[i][9],
                "duracion": myresult[i][10],
                "enLista": myresult[i][11],
                "imagenPaisaje": encodeAndString(myresult[i][12])
             })
    return jsonify(listaProvisional)


@app.route("/api/peliculaRapida", methods=["GET"])
def obtener_peliculaRapida():
    listaProvisional.clear()
    mycursor.execute("SELECT IDPelicula, Nombre, Genero, Director, Protagonista, Duracion, Lista, FotoPaisaje  FROM Pelicula")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "director": myresult[i][3],
                "protagonista": myresult[i][4],
                "duracion": myresult[i][5],
                "enLista": myresult[i][6],
                "imagenPaisaje": encodeAndString(myresult[i][7])
                
             })
    return jsonify(listaProvisional)

@app.route("/api/musicaRapida", methods=["GET"])
def obtener_musicaRapida():
    listaProvisional.clear()
    mycursor.execute("SELECT * FROM Musica WHERE MultimediaDeAparicion = '" + nombreAparicion[0] + "'")
    print("SELECT * FROM Musica WHERE MultimediaDeAparicion = '" + nombreAparicion[0] + "'")
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "cantante": myresult[i][3],
                "foto": encodeAndString(myresult[i][4]),
                "aparicion": myresult[i][5],
                "momentoAparicion": myresult[i][6],
                "grupo": myresult[i][7],
                "anoDePublicacion": myresult[i][8],
                "duracion": myresult[i][9],
                "enlaceYoutube": myresult[i][10],
                "enlaceAmazon": myresult[i][11],
                "enlaceItunes": myresult[i][12],
                "enlaceSpotify": myresult[i][13],
                "favorito": myresult[i][14]
             })
    nombreAparicion.clear()
    return jsonify(listaProvisional)

@app.route("/api/aparicion", methods=["POST"])
def obtener_aparicion():
    if request.method == "POST":
        aparicion = { 
        "aparicion" : request.json["aparicion"]
        }
        nombreAparicion.append(aparicion["aparicion"])
        return nombreAparicion

@app.route("/api/musicaElegida", methods=["POST"])
def obtener_musicaElegida():
    if request.method == "POST":
        musicaElegidaLista.clear()
        musicaElegida = { 
        "nombre" : request.json["nombre"]
        }
        musicaElegidaLista.append(musicaElegida["nombre"])
        return musicaElegidaLista

@app.route("/api/peliculaYSerie", methods=["GET"])
def obtener_peliculaYSerie():
    listaProvisional.clear()
    mycursor.execute("SELECT IDPelicula, Nombre FROM Pelicula")
    print(mycursor)
    mycursor.execute("SELECT * FROM Serie")
    print(mycursor)
    myresult = mycursor.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "enLista": myresult[i][2],
                "imagenPaisaje": encodeAndString(myresult[i][3]),
                "id": myresult[i][4]
                
             })
    return jsonify(listaProvisional)

@app.route("/api/musicaAMostrar", methods=["POST"])
def obtener_musicaAMostrar():
    if request.method == "POST":
        musicaMostrarLista.clear()
        musicaElegida = { 
        "id" : request.json["id"]
        }
        musicaMostrarLista.append(musicaElegida["id"])
        return musicaMostrarLista

@app.route("/api/recogerMusicaConcreta", methods=["GET"])
def recogerMusicaConcreta():
    listaProvisional.clear()
    mycursorPeli.execute("SELECT IDMusica, Nombre, Genero, Cantante, MultimediaDeAparicion, MomentoDeAparicion, Grupo, AnoDePublicacion, Duracion,EnlaceYoutube, EnlaceAmazon, EnlaceItunes, EnlaceSpotify, Favorito FROM Musica WHERE IDMusica = " + str(musicaMostrarLista[0]))
    myresult = mycursorPeli.fetchall()
    for i in range (0, len(myresult)):
     listaProvisional.append(
            {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "cantante": myresult[i][3],
                "aparicion": myresult[i][4],
                "momentoAparicion": myresult[i][5],
                "grupo": myresult[i][6],
                "anoDePublicacion": myresult[i][7],
                "duracion": myresult[i][8],
                "enlaceYoutube": myresult[i][9],
                "enlaceAmazon": myresult[i][10],
                "enlaceItunes": myresult[i][11],
                "enlaceSpotify": myresult[i][12],
                "favorito": myresult[i][13]
             })
    return jsonify(listaProvisional)

@app.route("/api/favorito", methods=["POST", "GET"])
def favorito():
    if request.method == "POST":
        favoritoObj = { 
        "id" : request.json["id"],
        "favorito": request.json["favorito"]
        }
        mycursorPeli.execute(f"UPDATE Musica SET Favorito = '{favoritoObj['favorito']}' WHERE IDMusica = {favoritoObj['id']}")
        return ("", 200)
    
    if request.method == "GET":
        listaProvisional.clear()
        mycursorPeli.execute("SELECT * FROM Musica WHERE Favorito = 'true'")
        myresult = mycursorPeli.fetchall()
        for i in range (0, len(myresult)):
            listaProvisional.append(
                   {
                    "id": myresult[i][0],
                    "nombre": myresult[i][1],
                    "genero": myresult[i][2],
                    "cantante": myresult[i][3],
                    "foto": encodeAndString(myresult[i][4]),
                    "aparicion": myresult[i][5],
                    "momentoAparicion": myresult[i][6],
                    "grupo": myresult[i][7],
                    "anoDePublicacion": myresult[i][8],
                    "duracion": myresult[i][9],
                    "enlaceYoutube": myresult[i][10],
                    "enlaceAmazon": myresult[i][11],
                    "enlaceItunes": myresult[i][12],
                    "enlaceSpotify": myresult[i][13],
                    "favorito": myresult[i][14]
                })
        return jsonify(listaProvisional)


@app.route("/api/lista", methods=["POST", "GET"])
def lista():
    if request.method == "POST":
        enListaObj = { 
        "nombre" : request.json["nombre"],
        "enLista": request.json["enLista"]
        }
        mycursorPeli.execute("SELECT Nombre FROM Serie")
        myresult = mycursorPeli.fetchall()
        print(myresult)
        tupla = (enListaObj["nombre"],) 
        resultado = myresult.count(tupla)
        if resultado > 0:
            print("Serie")
            mycursorPeli.execute(f"UPDATE Serie SET Lista = '{enListaObj['enLista']}' WHERE Nombre = '{enListaObj['nombre']}'")
        else:
            print("Peli")
            mycursorPeli.execute(f"UPDATE Pelicula SET Lista = '{enListaObj['enLista']}' WHERE Nombre = '{enListaObj['nombre']}'")
        mydb.commit()
        return ("", 200)
    if request.method == "GET":
        listaProvisional.clear()
        mycursorPeli.execute("SELECT * FROM Serie WHERE Lista = 'true'")
        myresult = mycursorPeli.fetchall()
        for i in range (0, len(myresult)):
         listaProvisional.append(
                {
                    "id": myresult[i][0],
                    "nombre": myresult[i][1],
                    "genero": myresult[i][2],
                    "director": myresult[i][3],
                    "protagonista": myresult[i][4],
                    "descripcionCorta": myresult[i][5],
                    "temporadas": myresult[i][6],
                    "episodios": myresult[i][7],
                    "foto": encodeAndString(myresult[i][8]),
                    "anoDePublicacion": myresult[i][9],
                    "duracion": myresult[i][10],
                    "enLista": myresult[i][11],
                    "imagenPaisaje": encodeAndString(myresult[i][12])
                 })
        return jsonify(listaProvisional)

@app.route("/api/listaPelicula", methods=["GET"])
def listaPeli():
    if request.method == "GET":
        listaProvisional.clear()
        mycursorPeli.execute("SELECT * FROM Pelicula WHERE Lista = 'true'")
        myresult = mycursorPeli.fetchall()
        for i in range (0, len(myresult)):
         listaProvisional.append(
                {
                "id": myresult[i][0],
                "nombre": myresult[i][1],
                "genero": myresult[i][2],
                "director": myresult[i][3],
                "protagonista": myresult[i][4],
                "descripcionCorta": myresult[i][5],
                "foto": encodeAndString(myresult[i][6]),
                "anoDePublicacion": myresult[i][7],
                "duracion": myresult[i][8],
                "enLista": myresult[i][9],
                "imagenPaisaje": encodeAndString(myresult[i][10])
                 })

        return jsonify(listaProvisional)

if __name__ == '__main__':
    app.run(debug=True)


##DROP TABLES Serie, Pelicula, Musica, Usuario, Cantante, Grupo, Reparto

#sql = "INSERT INTO Serie (Nombre, Genero, Director, Protagonista, DescripcionCorta, Temporadas, Episodios, FotoDeSerie, AnoDePublicacion, Duracion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val = [("Breaking Bad", "Drama", "Vince Giligan", "Bryan Cranston", "Descripción corta", "5" ,"59", Foto, "2008", "40:00:00"),
#("Cyberpunk: Edgerunners", "Ciberpunk", "Hiroyuki Imashi", "David Martinez", "Descripción corta","5" ,"59", Foto, "2008", "40:00:00"),
#("Rick y Morty", "Humor", "Justin Roiland", "Rick Sanchez", "Descripción corta","5" ,"59", Foto, "2008", "40:00:00")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#sql = "INSERT INTO Pelicula (Nombre, Genero, Director, Protagonista, DescripcionCorta, FotoDePelicula, AnoDePublicacion, Duracion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#val = [("Breaking Bad", "Drama", "Vince Giligan", "Bryan Cranston", "Descripción corta", Foto, "2008", "40:00:00"),
#("Cyberpunk: Edgerunners", "Ciberpunk", "Hiroyuki Imashi", "David Martinez", "Descripción corta", Foto, "2008", "40:00:00"),
#("Rick y Morty", "Humor", "Justin Roiland", "Rick Sanchez", "Descripción corta", Foto, "2008", "40:00:00")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#
#
#sql = "INSERT INTO Musica (Nombre, Genero, Cantante, FotoDeMusica, MultimediaDeAparición, Grupo, AnoDePublicacion, Duracion, EnlaceYoutube, EnlaceAmazon, EnlaceItunes, EnlaceSpotify) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val = [("For the damaged Coda", "Rock Indie", "Simone Pace", Foto, "Breaking Bad", "Blonde Redhead", "2000", "3:34", "Enlace", "Enlace", "Enlace", "Enlace"),
#("Dont look back", "Pop", "Kotomi", Foto, "Breaking Bad", "-", "2000", "2:42", "Enlace", "Enlace", "Enlace", "Enlace"),
#("I really want to stay at your house", "Synth-Pop", "Rosa Walton", Foto, "Breaking Bad", "-", "2000", "8:00", "Enlace", "Enlace", "Enlace", "Enlace")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#
#sql = "INSERT INTO Usuario (Nombre, Genero, FotoDePerfil, Contrasena, DNI, TipoDeCuenta, FechaDeNacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#val = [("Carlos Puigdemont", "Hombre", Foto, "VivaEspanya", "51699087Y", "Premium", "30-03-96"),
#("Carlas Tamayo", "Mujer", Foto, "VivaLaSecta", "51695087Y", "Normal", "30-12-96"),
#("Ayuso Yasuo", "Mujer", Foto, "Sanidant", "51299087Y", "Premium", "30-03-69")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#sql = "INSERT INTO Cantante (Nombre, Grupo) VALUES (%s, %s)"
#val = [("Natos", "Natos y Waor"),
#("Waor", "Natos y Waor"),
#("Freddy Mercury", "Queen")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#
#sql = "INSERT INTO Grupo (Nombre, Cantante) VALUES (%s, %s)"
#val = [("Queen", "Freddy Mercury"),
#("Guns and Roses", "Axel Rose"),
#("Natos y Waor", "Natos y Waor")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#sql = "INSERT INTO Reparto (Nombre, Rol) VALUES (%s, %s)"
#val = [("Dwayne Johnson", "Actor"),
#("Ryan Reynolds", "Actor"),
#("Tom Cruise", "Actor")]
#mycursor.executemany(sql, val)
#mydb.commit()
#
#def borrarTabla():
#  print("¿Que tabla quieres eliminar?")
#  print("Serie, Actor, Director, Grupo, Musica, Plataforma, Usuario.")
#  tablaABorrar = str(input())
#  mycursor.execute("DROP TABLE " + tablaABorrar)
#
#def anadirTabla():
#  print("¿Que nombre tiene la tabla?")
#  tablaACrear = str(input())
#  mycursor.execute("CREATE TABLE " + tablaACrear + "(Id" + tablaACrear + " INT AUTO_INCREMENT PRIMARY KEY)")
#  print("¿Cuantos campos tiene tu tabla?")
#  numeroDeCampos = int(input())
#  for x in range (0, numeroDeCampos):
#    print("¿Que tipo de campo es, numero o caracter?")
#    tipoCampo = str(input())
#    if tipoCampo == "numero":
#      print("¿Como se llama el dato?")
#      nombreCampoN = str(input())
#      mycursor.execute("ALTER TABLE " + tablaACrear + " ADD (`"+nombreCampoN+"` INT(20))")
#    elif tipoCampo == "caracter":
#      print("¿Como se llama el dato?")
#      nombreCampoN = str(input())
#      mycursor.execute("ALTER TABLE " + tablaACrear + " ADD (`"+nombreCampoN+"` VARCHAR(20))")
#    else:
#      print(tipoCampo + "no es un tipo de dato")
#
#def modificarUnaTabla():
#  print("¿Que tabla quieres modificar?")
#  mycursor.execute("SHOW TABLES FROM railway")
#
#  myresult = mycursor.fetchall()
#
#  for x in myresult:
#    print(x)
#  
#  tablaAModificar = str(input())
#
#  print("¿Que ID vas a modificar?")
#  mycursor.execute("SELECT * FROM " + tablaAModificar)
#  myresult = mycursor.fetchall()
#  for x in myresult:
#    print(x)
#  IdAModificar = int(input())
#
#  print("¿Que dato qiuieres modificar de " + tablaAModificar + "?")
#  mycursor.execute("DESCRIBE " + tablaAModificar)
#  myresult = mycursor.fetchall()
#  for x in myresult:
#    print(x[0])
#  
#  datoAModificar = str(input())
#
#  print("¿En que quieres que se convierta?")
#
#  datoModificado = str(input())
#
#  sql = "UPDATE " + tablaAModificar + " SET " + datoAModificar + " = " + datoModificado + " WHERE Id"+ tablaAModificar + " = " + str(IdAModificar) 
#
#  mycursor.execute(sql)  
#
#  mydb.commit()
#
#def insertarDatosEnTabla():
#  print("¿Que tabla quieres modificar?")
#  mycursor.execute("SHOW TABLES FROM railway")
#
#  myresult = mycursor.fetchall()
#
#  for x in myresult:
#    print(x)
#  tablaAModificar = "RolUsuarioBBDD"
#  while tablaAModificar == "RolUsuarioBBDD" or tablaAModificar == "UsuarioBBDD":
#    tablaAModificar = str(input())
#    if tablaAModificar == "RolUsuarioBBDD" or tablaAModificar == "UsuarioBBDD":
#      print("No puedes modificar esa tabla, por favor elige otra.")
#  mycursor.execute("DESCRIBE " + tablaAModificar)
#  myresult = mycursor.fetchall()
#  arrayLongitud = len(myresult)
#  sql = "INSERT INTO "+tablaAModificar+ " ("
#  valuesS = ""
#  datosTotal = []
#  for x in range(1, arrayLongitud):
#    print(myresult[x][0])
#    datosTotal.append(str(input()))
#    sql = sql + str(myresult[x][0])
#    valuesS = valuesS+"%s"
#    if x < arrayLongitud -1:
#      sql = sql + ","
#      valuesS = valuesS+","
#
#  sql = sql + ") VALUES (" + valuesS + ")"
#  val = (datosTotal)
#  mycursor.execute(sql, val)  
#  mydb.commit()
#
#def verUnaTabla():
#  print("¿Que tabla quieres ver?")
#  mycursor.execute("SHOW TABLES FROM railway")
#
#  myresult = mycursor.fetchall()
#
#  for x in myresult:
#    print(x)
#  
#  tablaAVer = str(input())
#  mycursor.execute("SELECT * FROM " + tablaAVer)
#  myresult = mycursor.fetchall()
#  for x in myresult:
#    print(x)
#
#def borrarDatosDeUnaTabla():
#  print("¿Que tabla quieres modificar?")
#  mycursor.execute("SHOW TABLES FROM railway")
#
#  myresult = mycursor.fetchall()
#
#  for x in myresult:
#    print(x)
#  
#  tablaAModificar = str(input())
#
#  print("¿Que dato vas a borrar? Escriba su Id por favot")
#  mycursor.execute("SELECT * FROM " + tablaAModificar)
#  myresult = mycursor.fetchall()
#  for x in myresult:
#    print(x)
#  IdABorrar = int(input())
#  sql = "DELETE FROM " +tablaAModificar+ " WHERE Id"+ tablaAModificar + " = " + str(IdABorrar)
#
#  mycursor.execute(sql)  
#
#  mydb.commit()
#
#def crearUsuario():
#  print("Introduce el nombre del usuario")
#  nombreUsuario = str(input())
#  print("Introduce la contrasena del usuario")
#  contrasenaUsuario = str(input())
#  print("Introduce el rol del usuario, estos son los roles disponibles:")
#  mycursor.execute("SELECT Rol FROM RolUsuarioBBDD")
#  RolUsuarioAMostrar = mycursor.fetchall()
#  print(RolUsuarioAMostrar)
#  rolUsuarioAIntroducir = str(input())
#  sql = "INSERT INTO UsuarioBBDD (Nombre, Contrasena, Rol) VALUES (%s, %s, %s)"
#  val = [(nombreUsuario,contrasenaUsuario,rolUsuarioAIntroducir)]
#  mycursor.executemany(sql,val)
#  mydb.commit()
#  
#
#
#def borrarUsuario():
#  print("Introduce el nombre del usuario")
#  mycursor.execute("SELECT Nombre FROM UsuarioBBDD")
#  myresult = mycursor.fetchall()
#  print(myresult)
#  nombreUsuario = str(input())
#  print("¿Estas seguro de que quieres borrar a "+ nombreUsuario + " de la base de datos?")
#  respuestaBorar = str(input())
#  if respuestaBorar == "si":
#    mycursor.execute("DELETE FROM UsuarioBBDD WHERE Nombre = '" + nombreUsuario+"'")
#  mydb.commit()
#
#
#  
#
#def modificarUsuario():
#  mycursor.execute("SELECT Nombre FROM UsuarioBBDD")
#  myresult = mycursor.fetchall()
#  print(myresult)
#  print("Introduce el nombre del usuario")
#  nombreUsuario = str(input())
#  mycursor.execute("SELECT * FROM UsuarioBBDD WHERE Nombre = '" + nombreUsuario+"'")
#  myresult = mycursor.fetchall()
#  print("Que quieres modificar del usuario? ¿Nombre, Contrasena o Rol?")
#  print(myresult)
#  respuestaModificar = str(input())
#  if respuestaModificar == "Nombre" or respuestaModificar == "Contrasena" or respuestaModificar == "Rol":
#    if respuestaModificar == "Rol":
#      mycursor.execute("SELECT Rol FROM RolUsuarioBBDD")
#      myresult = mycursor.fetchall()
#      print("Introduzca el nuevo "+ respuestaModificar)
#      print("Ten en cuenta que solo podrás usar un rol que ya exista, estos son los roles disponibles:")
#      print(myresult)
#      NombreModificar = str(input())
#      for rol in myresult:
#        if str(rol[0]) == NombreModificar:
#          mycursor.execute("UPDATE UsuarioBBDD SET " + respuestaModificar + " = '" + NombreModificar + "' WHERE Nombre = '" + nombreUsuario+"'")
#          mydb.commit()
#    else:
#      print("Introduzca el nuevo "+ respuestaModificar)
#      NombreModificar = str(input())
#      mycursor.execute("UPDATE UsuarioBBDD SET " + respuestaModificar + " = '" + NombreModificar + "' WHERE Nombre = '" + nombreUsuario+"'")
#      mydb.commit()
#  else:
#    print("Esa no es una respuesta válida")
#  mydb.commit()
#
#def crearRol():
#  print("¿Como se llama el rol que quieres crear? Estos son los que ya existen: ")
#  mycursor.execute("SELECT Rol FROM RolUsuarioBBDD")
#  myresult = mycursor.fetchall()
#  print(myresult)
#  rolNuevo = str(input())
#  sql = "INSERT INTO RolUsuarioBBDD (Rol) VALUES (%s)"
#  val = [(rolNuevo,)]
#  mycursor.executemany(sql, val)
#  mydb.commit()
#
#
#def borrarRol():
#  print("¿Como se llama el rol que quieres borrar? Estos son los que ya existen: ")
#  mycursor.execute("SELECT Rol FROM RolUsuarioBBDD")
#  myresult = mycursor.fetchall()
#  print(myresult)
#  rolABorrar = str(input())
#  for i in myresult:
#        if str(i[0]) == rolABorrar:
#          mycursor.execute("DELETE FROM RolUsuarioBBDD WHERE Rol = '" + rolABorrar + "'")
#          mydb.commit()
#
#
#seguir = 1
#while seguir == 1:
#  print("Introduzca su usuario por favor:")
#  mycursor.execute("SELECT Nombre FROM UsuarioBBDD")
#  usuario = mycursor.fetchall()
#  usuarioEsta = False
#  while usuarioEsta != True:
#    introducirUsuario = str(input())
#    for x in range(len(usuario)):
#      if str(usuario[x][0]) == introducirUsuario:
#        usuarioEsta = True
#        break
#    if str(usuario[x][0]) != introducirUsuario:
#      print('"' +introducirUsuario + '" no es un usuario.')
#
#  print("Introduzca su contrasena por favor:")
#  introducirContrasena = str(input()) 
#  mycursor.execute("SELECT Contrasena FROM UsuarioBBDD WHERE Nombre = '" + introducirUsuario+"'")
#  contrasena = mycursor.fetchall()
#
#  while contrasena[0][0] != introducirContrasena:
#    print("'"+ introducirContrasena+"' no es la contrasena válida.")
#    introducirContrasena = str(input()) 
#
#  mycursor.execute("SELECT Rol FROM UsuarioBBDD WHERE Nombre = '" + introducirUsuario+"'")
#
#  rolUsuario = mycursor.fetchall()
#  
#  if rolUsuario[0][0] == "Administrador de usuarios":
#    print("¿Que quieres hacer, administrador de usuarios?")
#    opcionesAdmin = ["Crear usuario", "Borrar usuario", "Modificar usuario", "Crear rol", "Borrar rol"]
#    print(opcionesAdmin)
#    respuestaAdmin = str(input())
#  
#    if respuestaAdmin == opcionesAdmin[0]:
#      crearUsuario()
#    elif respuestaAdmin == opcionesAdmin[1]:
#      borrarUsuario()
#    elif respuestaAdmin == opcionesAdmin[2]:
#      modificarUsuario()
#    elif respuestaAdmin == opcionesAdmin[3]:
#      crearRol()
#    elif respuestaAdmin == opcionesAdmin[4]:
#      borrarRol()
#    else:
#      print("Esa no es una opción válida.")
#
#  else:
#    print("¿Que quieres hacer?")
#    opciones = ["Eliminar una tabla", "Anadir una tabla", "Modificar una tabla", "Ver datos de una tabla", "Insertar datos en una tabla", "Borrar datos en una tabla"]
#    print(opciones)
#    respuesta = str(input())
#  
#    if respuesta == opciones[0] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Administrador"):
#      borrarTabla()
#  
#    elif respuesta == opciones[1] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Administrador"):
#      anadirTabla()
#  
#    elif respuesta == opciones[2] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Administrador"):
#      modificarUnaTabla()
#  
#    elif respuesta == opciones[3] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Lector" or rolUsuario[0][0] == "Administrador"):
#      verUnaTabla()
#  
#    elif respuesta == opciones[4] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Administrador"):
#      insertarDatosEnTabla()
#  
#    elif respuesta == opciones[5] and (rolUsuario[0][0] == "Editor" or rolUsuario[0][0] == "Administrador"):
#      borrarDatosDeUnaTabla()
#  
#    else:
#      print("Esa no es una opción válida")
#
#  print("¿Que quieres hacer? ¿Seguir o terminar la operación?")
#  respuestaASeguir = input()
#  if respuestaASeguir.lower() == "seguir":
#    seguir = 1
#    seguir = 0
#  else:
