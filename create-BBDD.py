import mysql.connector


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

##COMANDO BORRAR : DROP TABLE IF EXISTS Grupo, Cantante, Usuario, Reparto, Serie, Pelicula, Musica

#ANER#
Foto1 = convertToBinaryData("yourRoute + 91fNrsx08tL._AC_SL1500_.jpg")
Foto2 = convertToBinaryData("yourRoute + 1596628368_372018_1596628747_sumario_normal.jpeg")
Foto58 = convertToBinaryData("yourRoute + MV5BMTJiMzgwZTktYzZhZC00YzhhLWEzZDUtMGM2NTE4MzQ4NGFmXkEyXkFqcGdeQWpybA@@._V1_.jpg")
Foto59 = convertToBinaryData("yourRoute + 1366_2000(1).jpeg")

Foto3 = convertToBinaryData("yourRoute + Fast_Furious_9-833854731-large.jpeg")
Foto60 = convertToBinaryData("yourRoute + im_20140703_entretenimiento02_140709790.jpg")

Foto4 = convertToBinaryData("yourRoute + R-1974560-1328907906.jpeg")
Foto5 = convertToBinaryData("yourRoute + 286897-baby-blue.jpg")
Foto6 = convertToBinaryData("yourRoute + 8d64e974c73f8cb168958407dc79eb17.jpeg")
Foto7 = convertToBinaryData("yourRoute + Cover_On_a_Clear_Day_You_Can_See_Forever.jpeg")
Foto8 = convertToBinaryData("yourRoute + R-1722054-1504288191-2492.jpeg")

Foto9 = convertToBinaryData("yourRoute + ab67616d00001e0216dbd686d5d99a24360be0f8.jpeg")
Foto10 = convertToBinaryData("yourRoute + c16da94c0e2727d8ccb2f74f9ceb4990.1000x1000x1.png")
Foto11 = convertToBinaryData("yourRoute + 8263f36556d2761ceafe7df17cd0d74a.1000x1000x1.png")
Foto12 = convertToBinaryData("yourRoute + ab67616d0000b273013c00ee367dd85396f79c82.jpeg")
Foto13 = convertToBinaryData("yourRoute + ab67616d0000b273cbd268ca7dd04dbd94b69e5f.jpeg")

Foto14 = convertToBinaryData("yourRoute + The_Runaways_(album).png")
Foto15 = convertToBinaryData("yourRoute + ab67616d0000b273255e131abc1410833be95673.jpeg")
Foto16 = convertToBinaryData("yourRoute + R-145109-1646079409-4032.jpeg")
Foto17 = convertToBinaryData("yourRoute + Aerosmith_-_Aerosmith.jpeg")
Foto18 = convertToBinaryData("yourRoute + 71Thj-faSdL._SL1500_.jpg")

Foto19 = convertToBinaryData("yourRoute + descarga.jpeg")

#IKER#
#series#
Foto20 = convertToBinaryData("yourRoute + descarga2.jpeg")
Foto61 = convertToBinaryData("yourRoute + arcane-final-poster-16x9-no-text-no-border.jpeg")
#peliculas#
Foto21 = convertToBinaryData("yourRoute + Posteres-Ready-Player-One-Poster-Ready-Player-One-293844-l.jpeg")
Foto22 = convertToBinaryData("yourRoute + s-l500.jpeg")
Foto62 = convertToBinaryData("yourRoute + ready-player-one-2862279.jpg")
Foto63 = convertToBinaryData("yourRoute + 1366_2000.jpeg")
#musica#
Foto23 = convertToBinaryData("yourRoute + Twisted_Sister_We_re_Not_Gonna_Take_It_V_deo_musical-862486259-large.jpeg")
Foto24 = convertToBinaryData("yourRoute + site_thumb.jpeg")
Foto25 = convertToBinaryData("yourRoute + R-7222376-1436515122-9022.jpeg")
Foto26 = convertToBinaryData("yourRoute + hqdefault.jpeg")
Foto27 = convertToBinaryData("yourRoute + 118185166.jpeg")
Foto28 = convertToBinaryData("yourRoute + arcaneFoto.jpeg")
Foto29 = convertToBinaryData("yourRoute + arcaneFoto.jpeg")
Foto30 = convertToBinaryData("yourRoute + arcaneFoto.jpeg")
Foto31 = convertToBinaryData("yourRoute + arcaneFoto.jpeg")
Foto32 = convertToBinaryData("yourRoute + arcaneFoto.jpeg")
Foto33 = convertToBinaryData("yourRoute + s-l500.jpeg")
Foto34 = convertToBinaryData("yourRoute + s-l500.jpeg")
Foto35 = convertToBinaryData("yourRoute + s-l500.jpeg")
Foto36 = convertToBinaryData("yourRoute + s-l500.jpeg")
Foto37 = convertToBinaryData("yourRoute + s-l500.jpeg")
#usuario#
Foto38 = convertToBinaryData("yourRoute + how-hollow-knights-community-crafted-gibberish-into-a-real-language-1567781461548.jpeg")


#GUILLE#

Foto39 = convertToBinaryData("yourRoute + cyberpunk.jpeg")
Foto64 = convertToBinaryData("yourRoute + 5fa91ab921cfd.png")

Foto40 = convertToBinaryData("yourRoute + guardianes-de-la-galaxia-one-sheet-i28451.jpeg")
Foto41 = convertToBinaryData("yourRoute + deadpool.jpeg")
Foto65 = convertToBinaryData("yourRoute + scale.jpeg")
Foto66 = convertToBinaryData("yourRoute + scale(1).jpeg")

Foto42 = convertToBinaryData("yourRoute + cyberpunk.jpg")
Foto43 = convertToBinaryData("yourRoute + cyberpunk.jpg")
Foto44 = convertToBinaryData("yourRoute + cyberpunk.jpg")
Foto45 = convertToBinaryData("yourRoute + cyberpunk.jpg")
Foto46 = convertToBinaryData("yourRoute + cyberpunk.jpg")

Foto47 = convertToBinaryData("yourRoute + Hooked on a Feeling.jpeg")
Foto48 = convertToBinaryData("yourRoute + Spirit In The Sky.jpeg")
Foto49 = convertToBinaryData("yourRoute + I Want You Back.jpg")
Foto50 = convertToBinaryData("yourRoute + Escape (The Piña Colada Song).jpeg")
Foto51 = convertToBinaryData("yourRoute + Ain't No Mountain High Enough.jpeg")

Foto52 = convertToBinaryData("yourRoute + Angel of the Morning.jpeg")
Foto53 = convertToBinaryData("yourRoute + Shoop.jpg")
Foto54 = convertToBinaryData("yourRoute + Deadpool Rap.jpeg")
Foto55 = convertToBinaryData("yourRoute + X Gon' Give It To Ya.jpeg")
Foto56 = convertToBinaryData("yourRoute + Careless Whisper.jpeg")

Foto57 = convertToBinaryData("yourRoute + doggy.jpeg")

mydb = mysql.connector.connect(
  user="root", 
  password="Kh4FbzizGsd84PyaUumb", 
  host="containers-us-west-96.railway.app", 
  port="6053", 
  database="railway"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES FROM railway")
myresult = mycursor.fetchall()
mydb.commit()


mycursor.execute("CREATE TABLE IF NOT EXISTS Serie (IDSerie INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Director VARCHAR(255), Protagonista VARCHAR(255), DescripcionCorta VARCHAR(750), Temporadas INT(4), Episodios INT(5), FotoDeSerie LONGBLOB,AnoDePublicacion INT(5), Duracion VARCHAR(10), Lista VARCHAR(5), FotoPaisaje LONGBLOB)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Pelicula (IDPelicula INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Director VARCHAR(255), Protagonista VARCHAR(255), DescripcionCorta VARCHAR(750), FotoDePelicula LONGBLOB, AnoDePublicacion INT(5), Duracion VARCHAR(10), Lista VARCHAR(5), FotoPaisaje LONGBLOB)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Musica (IDMusica INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), Cantante VARCHAR(255), FotoDeMusica LONGBLOB, MultimediaDeAparicion VARCHAR(255),MomentoDeAparicion VARCHAR(255), Grupo VARCHAR(255), AnoDePublicacion INT(5), Duracion VARCHAR(10), EnlaceYoutube VARCHAR(255),EnlaceAmazon VARCHAR(255),EnlaceItunes VARCHAR(255),EnlaceSpotify VARCHAR(255),Favorito VARCHAR(5))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Usuario (IDUsuario INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Genero VARCHAR(255), FotoDePerfil LONGBLOB, Contrasena VARCHAR(255), DNI VARCHAR(255), TipoDeCuenta VARCHAR(255), FechaDeNacimiento VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Cantante (IDCantante INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Grupo VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Grupo (IDGrupo INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Cantante VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Reparto (IDReprto INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), Rol VARCHAR(255))")
mydb.commit()





sql = "INSERT INTO Musica (Nombre, Genero, Cantante, FotoDeMusica, MultimediaDeAparicion, MomentoDeAparicion, Grupo, AnoDePublicacion, Duracion, EnlaceYoutube, EnlaceAmazon, EnlaceItunes, EnlaceSpotify, Favorito) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Who's Ready for Tomorrow", "Cyberpunk", "Rat Boy", Foto42, "Cyberpunk: Edgerunners", "T:1  E:01 - 12:45", "Rat Boy", "2022", "3:36", "https://www.youtube.com/watch?v=FRSTaBZfxK4&list=PLl-vhnGPY7cpGmDrC1P5qzY9QebtwuYAe&index=3", "https://music.amazon.es/albums/B08NXBQ6KY?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_eafHHrqXLOt8v6pFIzgGEm9jX&trackAsin=B08NXG3MZ7", "https://music.apple.com/us/album/whos-ready-for-tomorrow/1540792622?i=1540793076", "https://open.spotify.com/track/4mn5HdatHKN7iFGDes9G8i?si=0f0f8aa265924f99", "true"),
("Friday Night Fire Fight", "Cyberpunk", "Aligns", Foto43, "Cyberpunk: Edgerunners","T:1  E:03 - 14:05", "Rubiciones", "2022", "3:37", "https://www.youtube.com/watch?v=XGUy0__LJKw&list=PLl-vhnGPY7cpGmDrC1P5qzY9QebtwuYAe&index=8", "https://music.amazon.es/albums/B08QZ6LQSS?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_9AV1wBa2tit02YPRWWF2Gqhg7&trackAsin=B08QZ1BKXF", "https://music.apple.com/cr/album/friday-night-fire-fight/1545493788?i=1545493799", "https://open.spotify.com/track/1GhEAuoPdSPiOgqiwLvdf0?si=3af052a4ee0246c2", "false"),
("I Really Want to Stay at Your House", "Cyberpunk", "Rosa Walton", Foto44, "Cyberpunk: Edgerunners", "Ending", "Hallie Coggins", "2022", "4:09", "https://www.youtube.com/watch?v=Wi17ybKXmXE&list=PLl-vhnGPY7cpGmDrC1P5qzY9QebtwuYAe&index=11", "https://music.amazon.es/albums/B08NXBQ6KY?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_P2SveEOOlQ5diVfDxw40sz39X&trackAsin=B08NXFKYQC", "https://music.apple.com/us/album/i-really-want-to-stay-at-your-house/1540792622?i=1540793097", "https://open.spotify.com/track/7mykoq6R3BArsSpNDjFQTm?si=48a142df2916412c", "false"),
("Me Machine", "Cyberpunk", "Poly Face", Foto45, "Cyberpunk: Edgerunners","T:1  E:08 - 02:45", "Kuba Sojka", "2022", "3:42", "https://www.youtube.com/watch?v=CuvLONbTBPA&list=PLl-vhnGPY7cpGmDrC1P5qzY9QebtwuYAe&index=13", "https://music.amazon.es/albums/B07HYKPMQP?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_4BOMi2qBPOsoL3QP7T3OlDUDn&trackAsin=B07HYL62ZM", "https://music.apple.com/us/album/reversion-single/1669721853", "https://open.spotify.com/track/1v5WrRqHvuqAoYNIMSFuG2?si=4740793e4e5b42ed", "false"),
("I Will Follow", "Cyberpunk", "Snot Abundance", Foto46, "Cyberpunk: Edgerunners","Opening", "Snot Abundance", "2022", "2:42", "https://www.youtube.com/watch?v=TGE5SEmib9k&list=PLl-vhnGPY7cpGmDrC1P5qzY9QebtwuYAe&index=12", "https://music.amazon.es/albums/B06Y3ZM9DK?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_FDJNy2KRz8XM4pDIR2u3JMhxY&trackAsin=B06Y3XG71W", "https://music.apple.com/us/album/i-will-follow-you-are-with-me/1440812960?i=1440813081", "https://open.spotify.com/track/40lKv5fLpzPHV1YQ7nrfMg?si=1b260fd8093044c4", "false"),

("Hooked on a Feeling", "Pop Rock", "Blue Swede", Foto47, "Guardianes de la Galaxia", "0:02:20", "-", "1974", "2:47", "https://www.youtube.com/watch?v=NrI-UBIB8Jk&list=PLEijU2q67K_twQnJ06-3DnrvsAdEii_MQ&index=3", "https://music.amazon.es/albums/B00LL9YAJG?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_KW28eQAQfVwfrUU9V7uFseyrO&trackAsin=B00LL9YDKM", "https://music.apple.com/us/album/hooked-on-a-feeling-single/1467944024", "https://open.spotify.com/track/6Ac4NVYYl2U73QiTt11ZKd?si=42d4d0dbe6e84b20", "false"),
("Spirit In The Sky", "Rock", "Norman Greenbaum", Foto48, "Guardianes de la Galaxia", "0:12:20", "Norman Greenbaum", "1969", "3:57", "https://www.youtube.com/watch?v=n95A6G9IxlM&list=PLEijU2q67K_twQnJ06-3DnrvsAdEii_MQ&index=4", "https://music.amazon.es/albums/B07R972RTD?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_o6RPAbwAqFVaJUPgSoSgX3zQf&trackAsin=B07RCWHQMK", "https://music.apple.com/us/album/spirit-in-the-sky/1462211353?i=1462211356", "https://open.spotify.com/track/0jvN7eQJJt4nxQzgQfZ1SP?si=ab882c889df849e9", "false"),
("I Want You Back", "Rock", "Jackson 5", Foto49, "Guardianes de la Galaxia", "0:52:20", "Jackson 5", "1969", "2:53", "https://www.youtube.com/watch?v=DGDyAb6pePo&list=PLEijU2q67K_twQnJ06-3DnrvsAdEii_MQ&index=7", "https://music.amazon.es/albums/B0097EX1QK?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_lTrZfdcwANd4BvnSzimWeZMiz&trackAsin=B0097EX2AA", "https://music.apple.com/us/album/i-want-you-back-unreleased-masters/1443838560", "https://open.spotify.com/track/5LxvwujISqiB8vpRYv887S?si=4f7e3932b62946ec", "false"),
("Escape (The Piña Colada Song)", "Soft Rock", "Rupert Holmes", Foto50, "Guardianes de la Galaxia", "2:12:20", "Rupert Holmes", "1979", "3:47", "https://www.youtube.com/watch?v=TazHNpt6OTo&list=PLEijU2q67K_twQnJ06-3DnrvsAdEii_MQ&index=10", "https://music.amazon.es/albums/B009ILYH6A?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_pCBo3sb16fKiwrYTv71zDEVx5&trackAsin=B0098BHLF4", "https://music.apple.com/us/album/escape-the-pina-colada-song/1443846037?i=1443846163", "https://open.spotify.com/track/5IMtdHjJ1OtkxbGe4zfUxQ?si=4f4adeace21c46fb", "false"),
("Ain't No Mountain High Enough", "R&B/Soul", "Marvin Gaye", Foto51, "Guardianes de la Galaxia", "2:42:20", "Tammi Terrell", "1967", "2:25", "https://www.youtube.com/watch?v=-C_3eYj-pOM&list=PLEijU2q67K_twQnJ06-3DnrvsAdEii_MQ&index=11", "https://music.amazon.es/albums/B0098A3PNW?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_H6VqcC9vY6oVnTGxvCEVgnvlT&trackAsin=B0098F7QB4", "https://music.apple.com/us/album/aint-no-mountain-high-enough/1469575128?i=1469575663", "https://open.spotify.com/track/7tqhbajSfrz2F7E1Z75ASX?si=93b35bf0a5854b37", "false"),

("Angel of the Morning", "Pop", "Juice Newton", Foto52, "Deadpool", "1:32:20", "Juice Newton ", "1981", "4:12", "https://www.youtube.com/watch?v=u1oiWcN05po&list=PLKlfy6eYBwbxE1Jc6Ztr71sIplZqS9iEI&index=1", "https://music.amazon.es/albums/B008P6GG2M?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_wyA51GxRV7FsEAwAAPUxVziE5&trackAsin=B008P6GGTU", "https://music.apple.com/mx/album/angel-of-the-morning-ep/405852622", "https://open.spotify.com/track/6NVB6W7G3svCKe5zB7kY8q?si=9ed2d5b998794b79", "false"),
("Shoop", "Hip Hop Rap", "Salt-N-Pepa", Foto53, "Deadpool", "0:42:20", "Sandra Denton", "1990", "4:08", "https://www.youtube.com/watch?v=y8Rf1OECxYY&list=PLKlfy6eYBwbxE1Jc6Ztr71sIplZqS9iEI&index=4", "https://music.amazon.es/albums/B07GJVFXTW?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_T9RVzkZhBvzyHJZWyOWWkadwc&trackAsin=B07GJZD9P9", "https://music.apple.com/us/album/shoop/1442956980?i=1442957143", "https://open.spotify.com/track/0Pu71wxadDlB8fJXfjIjeJ?si=e653a3c1777d42ae", "false"),
("Deadpool Rap", "Rap", "Teamheadkick", Foto54, "Deadpool", "0:52:20", "Teamheadkick", "2014", "4:08", "https://www.youtube.com/watch?v=y8Rf1OECxYY&list=PLKlfy6eYBwbxE1Jc6Ztr71sIplZqS9iEI&index=4", "https://music.amazon.es/albums/B0BNJ7WR8H?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_mfzGc3R8HUIn4kOJKRf14dS1Z&trackAsin=B0BNJ7QRYG", "https://music.apple.com/ar/album/deadpool-rap-film-mix/1076661307?i=1076662043", "https://open.spotify.com/track/2pBY04GIRFS3QsztMa4i2W?si=c6e3845c65f64d5a", "false"),
("X Gon' Give It To Ya", "Rap", "DMX", Foto55, "Deadpool", "0:45:20", "DMX", "2003", "3:37", "https://www.youtube.com/watch?v=Rw2U8rm32ps&list=PLKlfy6eYBwbxE1Jc6Ztr71sIplZqS9iEI&index=17", "https://music.amazon.es/albums/B0BLXTPD3B?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_TmbJwcY5Pzn7usKirPN3eCMgb&trackAsin=B0BLXFVR23", "https://music.apple.com/us/album/x-gon-give-it-to-ya/1434906919?i=1434907126", "https://open.spotify.com/track/1zzxoZVylsna2BQB65Ppcb?si=1c54bfcc370044ae", "false"),
("Careless Whisper", "Pop", "George Michael ", Foto56, "Deadpool", "0:54:20", "-", "1984", "5:02", "https://www.youtube.com/watch?v=N50ga0sR3_4&list=PLKlfy6eYBwbxE1Jc6Ztr71sIplZqS9iEI&index=23", "https://music.amazon.es/albums/B009IGXZPE?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_n75OfX2Dt6wHbg9rHpgLtdY8S&trackAsin=B009BC3E6U", "https://music.apple.com/us/album/careless-whisper/282658449?i=282658481", "https://open.spotify.com/track/4jDmJ51x1o9NZB5Nxxc7gY?si=a08bf28a00b349c7", "false"),

("Chaotica", "Rock Indie", "AI Wodtke", Foto4, "Breaking Bad","T:1  E:01 - 12:45", " The Bambi Molesters", "1998", "3:34", "https://www.youtube.com/watch?v=9KDnfMpt4-Q", "https://music.amazon.es/albums/B09BFX1FLH?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_7kuVqQeoFyuqLGN7EufoM9dJu&trackAsin=B09BFXMVZ5", "https://music.apple.com/es/album/chaotica/1578868429?i=1578868941", "https://open.spotify.com/track/4XhYignKL35SQ1rvrQZ8XW?si=aeiKzW3SRaOTQ_rx-mCJTg", "false"),
("Baby Blue", "Rock", "Kotomi", Foto5, "Breaking Bad","T:5  E:02 - 00:45", "Badfinger", "2000", "2:42", "https://www.youtube.com/watch?v=TkA7xQb6uPk", "https://music.amazon.es/albums/B009BGOYZG?trackAsin=B009BGOZQO", "https://music.apple.com/es/album/baby-blue/771784195?i=771784201", "https://open.spotify.com/track/6S3JlDAGk3uu3NtZbPnuhS?si=F2podseqRZGC6nNuSH--hQ", "false"),
("Everyday", "Rock", "Mack Self", Foto6, "Breaking Bad","T:8  E:11 - 02:45", "-", "1997", "4:00", "http://www.youtube.com/watch?v=EscLDJIpnGI", "https://music.amazon.es/albums/B07GS64V3F?trackAsin=B07GS45N89", "https://music.apple.com/us/album/everyday/1578339644?i=1578339651", "https://open.spotify.com/track/1FFDmEumw3YsSHtIeyqzCv?si=PjNj-vIaS9GBrnCOgiEakg", "false"),
("On a Clear Day (You Can See Forever)", "Rock Indie", "Roy Phillips", Foto7, "Breaking Bad","T:2  E:04 - 02:45", "The Peddlers", "2006", "3:34", "http://www.youtube.com/watch?v=yxf1IFgPH5s", "https://music.amazon.es/albums/B009AEWSKM?trackAsin=B009AEX7MU", "https://music.apple.com/es/album/on-a-clear-day-you-can-see-forever-main-title/181590522?i=181590873", "https://open.spotify.com/track/3FzBRKgDtjtv0Xu0diOzib?si=jNPJDR3BSVG9GozipwFyvw", "false"),
("If I Didn't Love You", "Rock Indie", "Glenn Tilbrook", Foto8, "Breaking Bad","T:1  E:05 - 01:45", "Squeeze", "2001", "2:34", "http://www.youtube.com/watch?v=6p9sPVXGa1Y", "https://music.amazon.es/albums/B07L6XCCMZ?trackAsin=B07L6MDQCQ", "https://music.apple.com/us/album/if-i-didnt-love-you/1452792772?i=1452793214&l=es", "https://open.spotify.com/track/65p2AbWFdX0aLAsdxcTDbN?si=LZUKrUptQXCTyYMr3Ez4_Q", "false"),

("De Museo", "Trap", "Bad Bunny", Foto9, "Fast and Furious 9", "0:52:20", "-", "2020", "5:04", "https://www.youtube.com/watch?v=ss0Un7fa-Mw", "https://music.amazon.es/albums/B098L6B167?trackAsin=B098L6NV64", "https://music.apple.com/es/album/de-museo/1575007987?i=1575007990", "https://open.spotify.com/track/267NGliXM8YLVZiKAD9Otm?si=6fNpXdpUQVe8OmOaUYe1rQ", "false"),
("Fast 9", "Trap", "Brian Tyler", Foto10, "Fast and Furious 9", "1:02:20", "-", "2020", "4:34", "https://www.youtube.com/watch?v=CYRSazil8Bs", "https://music.amazon.es/albums/B093XXVYGH?trackAsin=B093XYX51Q", "https://music.apple.com/us/album/fast-9/1565626445?i=1565626842", "https://open.spotify.com/track/0n0LxJE8y3i4QThQOjPvqS?si=nx7aFJ9FSMyYHtweGbfmNQ", "false"),
("Selah", "Trap", "Kanye West", Foto11, "Fast and Furious 9", "2:12:20", "-", "2019", "2:34", "https://www.youtube.com/watch?v=6CNPg2IQoC0", "https://music.amazon.es/albums/B07ZKXY6HF?trackAsin=B07ZKXXCFY", "https://music.apple.com/cl/album/selah/1484936940?i=1484937098", "https://open.spotify.com/track/39JRmdKFka1Oe09FoOCPI4?si=6CWqSoDBTOaE-Nr2ZHuB4A", "false"),
("Feel The Love", "Dance", "Kid Cudi", Foto12, "Fast and Furious 9", "1:42:20", "Kids SEE GOST", "2021", "3:52", "https://www.youtube.com/watch?v=rnZQvgWhM5s", "https://music.amazon.es/albums/B07DM9MRCW?trackAsin=B07DM821CS", "https://music.apple.com/us/album/feel-the-love-feat-pusha-t/1396710872?i=1396711193", "https://open.spotify.com/track/3aUFrxO1B8EW63QchEl3wX?si=OneUp1-dTOqzMTRA9UVWNQ", "false"),
("Furiosa", "Trap", "Annita", Foto13, "Fast and Furious 9", "2:20:10", "-", "2021", "3:25", "https://www.youtube.com/watch?v=s_yWthzaZFs", "https://music.amazon.es/albums/B095XMD73J?trackAsin=B095XL89ND", "https://music.apple.com/us/album/furiosa/1569423035?i=1569424110", "https://open.spotify.com/track/3AuBvhpKxvDynlPFwbaqJF?si=nzS0YnLeSN2FJZXJyMCSpQ", "false"),

("Cherry Bomb", "Pop", "Cherie Currie", Foto14, "The Boys","T:1  E:06 - 02:45", "The Runnaways", "2000", "3:52", "https://www.youtube.com/watch?v=_EBvXpjudf8", "https://music.amazon.es/albums/B0098IR7G0?trackAsin=B0098IR8GE", "https://music.apple.com/us/album/cherry-bomb/1440747926?i=1440747928", "https://open.spotify.com/track/7cdnq45E9aP2XDStHg5vd7?si=lfpda9ncT2OhtDRKiTFuTQ", "false"),
("Never Gonna Give You Up", "Pop", "Rick Astley", Foto15, "The Boys","T:2  E:02 - 02:22", "-", "2003", "3:13", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://music.amazon.es/albums/B07X34HZMY?trackAsin=B07X32ZM3X", "https://music.apple.com/us/album/never-gonna-give-you-up/1478168215?i=1478168518", "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT?si=R-Ka3X4USQW19YxKGGZaEQ", "false"),
("Psycho Killer", "Rock", "David Byrne", Foto16, "The Boys","T:5  E:05 - 25:55", "Talking Heads", "2004", "3:53", "https://www.youtube.com/watch?v=CKti7QixnJI", "https://music.amazon.es/albums/B00NILM06A?trackAsin=B00NILM4SE", "https://music.apple.com/us/album/psycho-killer/20833651?i=20833655", "https://open.spotify.com/track/1i6N76fftMZhijOzFQ5ZtL?si=7vQQfjywRlqhUbsVTIga7w", "false"),
("Dream On", "Soft Metal", "Steven Tyler", Foto17, "The Boys","T:2  E:02 - 12:45", "AeroSmith", "2006", "3:35", "https://www.youtube.com/watch?v=89dGC8de0CA", "https://music.amazon.es/albums/B0094Y6AUM?trackAsin=B0094ZU5AM", "https://music.apple.com/us/album/dream-on/1658644936?i=1658644941&l=es", "https://open.spotify.com/track/1xsYj84j7hUDDnTTerGWlH?si=kBkGmqepQMyvRTpy9bj64Q", "false"),
("Baby One More Time", "Pop", "Britney Spears", Foto18, "The Boys","T:6  E:06 - 22:45", "-", "1999", "3:33", "https://www.youtube.com/watch?v=C-u5WLJ9Yk4", "https://music.amazon.es/albums/B0093C8LX4?trackAsin=B00939BT86", "https://music.apple.com/us/album/baby-one-more-time/268284599?i=268284600", "https://open.spotify.com/track/3MjUtNVVq3C8Fn0MP3zhXa?si=MfoWYX6ES7OKHoOeDGkXXQ", "false"),

("We are not gonna take it", "Glamm Rock", "Frank Karuba", Foto23, "Ready player one", "0:00:20", "Twisted Sister", "1983", "3:40", "https://www.youtube.com/watch?v=ZqOp76R12DM", "https://music.amazon.es/albums/B00J7WSFKO?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_mgcqJ4LeUA4tnHqrtNCn6TajT&trackAsin=B00J7WSHCK", "https://music.apple.com/es/album/were-not-gonna-take-it/1093420230?i=1093420483", "https://open.spotify.com/track/1hlveB9M6ijHZRbzZ2teyh?autoplay=true", "false"),
("Jump", "rock", "Van Halen", Foto24, "Ready player one", "0:02:20", "-", "1984", "4:03", "https://www.youtube.com/watch?v=ggJI9dKBk48", "https://music.amazon.es/albums/B008MC5G1G?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_cmFUHJj0OxFta7TvUOxlvatE1&trackAsin=B008MC5K1C", "https://music.apple.com/es/album/jump-2015-remastered/984704583?i=984704837", "https://open.spotify.com/track/6Fba9RZtC6vTY814JToDtP?autoplay=true", "false"),
("Dead man`s party", "rock", "Danny Elfman", Foto25, "Ready player one", "0:12:20", "-", "1984", "6:21", "https://youtu.be/yhN8SdulOFc", "https://music.amazon.es/albums/B07H1BSMY9?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_C1uCuUZhBWWQ9TuDpdgHctpGE&trackAsin=B07H1DS55C", "https://music.apple.com/es/album/dead-mans-party-1988-boingo-alive-version/1452877744?i=1452878369", "https://music.apple.com/es/album/dead-mans-party-1988-boingo-alive-version/1452877744?i=1452878369", "false"),
("Can`t hide love", "Maurice White", "Van Halen", Foto26, "Ready player one", "1:12:20", "-", "1984", "4:08", "https://youtu.be/1TxgfbPl9Qg", "https://music.amazon.es/albums/B07R53HR79?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_pNT3MP4pSFUwk8tprzU3D1Fkp&trackAsin=B07R626FXP", "https://music.apple.com/es/album/cant-hide-love/1456623332?i=1456623335", "https://open.spotify.com/track/6hsQO3hz648zS7t2QyUpfz?autoplay=true", "false"),
("Stand on It", "rock", "Bruse Springsteen", Foto27, "Ready player one", "2:12:20", "-", "1984", "3:05", "https://youtu.be/8CxaXbCEYzE", "https://music.amazon.es/albums/B07JG2W7KB?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_ngVitUyrBluJUH8cqzjXd77sL&trackAsin=B07JHKZRGJ", "https://music.apple.com/us/album/stand-on-it-single-b-side-1985/1439282181?i=1439282690", "https://open.spotify.com/track/6eKh5kCernNwQrYPcfBunx", "false"),


("Misfit toys", "Trap", "Pusha T & Mako", Foto28, "Arcane","T:1  E:08 - 22:45", "-", "2021", "3:21", "https://www.youtube.com/watch?v=f_Z1E32mxGg&list=PLJP5_qSxMbkI7B5W8uo_FLAtmSKwhxXLt&index=7", "https://music.amazon.es/albums/B09L5K97LG?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_4yVv6S8ixgtQ71os4NDqxZbon&trackAsin=B09L5JHV93", "https://music.apple.com/mx/song/misfit-toys-from-the-series-arcane-league-of-legends/1593944615", "https://open.spotify.com/track/7HQSxHyORPbCQ1XtgV1k1P", "false"),
("When everything  went wrong", "R&B", "Xavier Amin Dphrepaulezz", Foto29, "Arcane","T:1  E:02 - 12:45", "Fantastic negrito", "2021", "3:13", "https://www.youtube.com/watch?v=G0XE4OHoqn8&list=RDEMOs6hz2tMHmFZRO21c5mHgQ&start_radio=1", "https://music.amazon.es/albums/B09L5K97LG?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_JS0uHfH6KGcUMV3NaOcRhjA0N&trackAsin=B09L5GYHLR", "https://music.apple.com/es/album/when-everything-went-wrong-from-the-series-arcane/1593944607?i=1593944768", "https://open.spotify.com/track/6YCW1g7XwaDZX7sUSM8LWq?autoplay=true", "false"),
("Snakes", "Rock", "Miyavi & PVRIS ", Foto30, "Arcane","T:1  E:01 - 02:45", "Miyavi & PVRIS", "2021", "2:41", "https://open.spotify.com/track/https://youtu.be/4UprHuO_zCc", "https://music.amazon.es/albums/B09L5K97LG?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_p4FEFpbGZXiERvtti7nXXLxT6&trackAsin=B09L5H79PL", "https://music.apple.com/es/album/snakes-from-the-series-arcane-league-of-legends/1593944607?i=1593944767", "https://open.spotify.com/album/14M8F8rKpr6LGlIgPmm6t6", "false"),
("Guns for hire", "Orchestra", "Yoann Lemoine", Foto31, "Arcane","T:1  E:04 - 10:45", "WoodKid", "2021", "3:46", "https://youtu.be/pKNEx-9OqRM", "https://music.amazon.es/albums/B09L5K97LG?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_p4HCY7KPfsf5KUFjHipS9kuyF&trackAsin=B09L5JP8CD", "https://music.apple.com/es/album/guns-for-hire-from-the-series-arcane-league-of-legends/1593944607?i=1593944614", "https://open.spotify.com/album/4UhhAzmY6tSTfmSqdhOttH", "false"),
("Get Jinxed", "Punk", "Agnete Kjolsrud", Foto32, "Arcane","T:1  E:09 - 24:55", "Djerv", "2014", "2:14", "https://youtu.be/KedDZiXoVTw", "https://music.amazon.es/albums/B07SZJFZH2?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_n4w2BI8auGxvg2J4DmEs8Wz1v&trackAsin=B07T3RV562", "https://music.apple.com/mx/album/get-jinxed-from-league-of-legends-single/1125503813", "https://open.spotify.com/track/0WpRF4X2LyMTZnqqrXX19U", "false"),


("Danger zone", "Rock", "Kenny Loggins", Foto33, "Top Gun Maverik", "0:02:20", "-", "1986", "3:33", "https://www.youtube.com/watch?v=yK0P1Bk8Cx4", "https://music.amazon.es/albums/B009IGAJAS?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_YPprjTh5u6As1UNZM3KKKCn3R&trackAsin=B009398AOW", "https://music.apple.com/us/album/danger-zone-from-top-gun-original-soundtrack/1058077856?i=1058079261", "https://open.spotify.com/track/34x6hEJgGAOQvmlMql5Ige", "false"),
("Great balls of fire(Live)", "Rock", "Miles teller", Foto34, "Top Gun Maverik","0:12:20", "-", "1986", "2:14", "https://youtu.be/pVcMsjyKlaM", "https://music.amazon.es/albums/B09Z7VDZ4T?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_TFPbO02R8EwYSG41vWcdLgAIs&trackAsin=B09Z7S8LSV", "https://music.apple.com/es/album/great-balls-of-fire-live/1621817793?i=1621817891", "https://open.spotify.com/track/7xe3EQCvXnx6Q0zs41Y65n?autoplay=true", "false"),
("The Man , The Legend / Touchdown", "Orchestra", "Hans Zimmer", Foto35, "Top Gun Maverik","0:22:20", "-", "2021", "3:50", "https://youtu.be/JiXjziluIx8", "https://music.amazon.es/albums/B09Z7VDZ4T?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_VPTBl32fUlUvyGCH0EprlAKW7&trackAsin=B09Z84YCK3", "https://music.apple.com/es/album/the-man-the-legend-touchdown/1621817793?i=1621817902", "https://open.spotify.com/track/3vPFtJIPNknOiMK7IcBtzn?autoplay=true", "false"),
("Top Gun Anthem", "Orchestra", "Hans Zimmer", Foto36, "Top Gun Maverik","0:52:20", "-", "2021", "4:15", "https://youtu.be/5zq7ujKwuRY", "https://music.amazon.es/albums/B09Z7VDZ4T?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_qQ3XrCgdhmJvlBzjY5zhaIGQC&trackAsin=B09Z7SBBPV", "https://music.apple.com/es/album/top-gun-anthem/1621817793?i=1621817907", "https://open.spotify.com/track/3vPFtJIPNknOiMK7IcBtzn?autoplay=true", "false"),
("Hold My Hand", "PoP", "Lady gaga", Foto37, "Top Gun Maverik","1:52:20", "-", "2021", "3:50", "https://youtu.be/Yx3K3g4CtoQ", "https://music.amazon.es/albums/B09Z7VDZ4T?marketplaceId=A1RKKUPIHCS9HS&musicTerritory=ES&ref=dm_sh_m3RXeL0wDlM7LUW9yQPmRL9rr&trackAsin=B09Z7TQ986", "https://music.apple.com/es/album/hold-my-hand/1621817793?i=1621817905", "https://open.spotify.com/track/3vPFtJIPNknOiMK7IcBtzn?autoplay=true", "false")]

mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Serie (Nombre, Genero, Director, Protagonista, DescripcionCorta, Temporadas, Episodios, FotoDeSerie, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Cyberpunk: Edgerunners", "Ciberpunk", "Hiroyuki Imashi", "David Martinez", "Cyberpunk: Edgerunners, nos presenta la vida de un chico llamado David Martínez. Este vive en una ciudad futurista (Night City) llena de vida y color, donde mucha parte de la sociedad vive obsesionada con los implantes y las mejoras corporales que el futuro les puede ofrecer.","5" ,"59", Foto39, "2008", "40:00:00", "false", Foto64)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Pelicula (Nombre, Genero, Director, Protagonista, DescripcionCorta, FotoDePelicula, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Guardianes de la Galaxia", "Ciencia ficcion", "James Gunn", "Chris Pratt", "Peter Quill es un forajido legendario abducido de la Tierra cuando era niño. Después de recuperar un antiguo artefacto, Quill debe reunir a un equipo de inadaptados cósmicos para evitar que un poderoso villano destruya la galaxia.", Foto40, "2014", "02:02:00", "false", Foto65),
("Deadpool", "Comedia cinematografica", "Tim Miller", "Ryan Reynolds", "Wade Wilson, tras ser sometido a un cruel experimento científico, adquiere poderes especiales que le convierten en Deadpool. Armado con sus nuevas habilidades y un retorcido sentido del humor tratará de dar caza al hombre que casi destruye su vida.", Foto41, "2016", "01:48:00", "false", Foto66)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Usuario (Nombre, Genero, FotoDePerfil, Contrasena, DNI, TipoDeCuenta, FechaDeNacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("Guillermo Sanchez", "Hombre", Foto57, "1235", "51699087Y", "Premium", "06-06-97")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Cantante (Nombre, Grupo) VALUES (%s, %s)"
val = [("Blue Swede", "Blue Swede"),
("george michael", "george michael"),
("DMX", "DMX")]
mycursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO Grupo (Nombre, Cantante) VALUES (%s, %s)"
val = [("Jackson 5", "Jackson 5"),
("Salt-N-Pepa", "Sandra Denton"),
("Marvin Gaye", "Tammi Terrell")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Reparto (Nombre, Rol) VALUES (%s, %s)"
val = [("Hiroyuki Imashi", "Director"),
("David Martinez", "Protagonista"),
("Ryan Reynolds", "Protagonista")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Serie (Nombre, Genero, Director, Protagonista, DescripcionCorta, Temporadas, Episodios, FotoDeSerie, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Breaking Bad", "Drama", "Vince Giligan", "Bryan Cranston", "Breaking Bad es una serie estadounidense ambientada en Albuquerque, Nuevo México, que relata la historia de Walter White, un profesor de química al que le diagnostican un cáncer de pulmón inoperable.", "5" ,"59", Foto1, "2008", "58:00:00", "false", Foto58),
("The Boys", "Accion", "Erik Kripke", "Jack Quaid", "Basada en el cómic del mismo nombre de Garth Ennis y Darick Robertson, sigue al equipo homónimo de justicieros en su lucha contra diversos individuos con superpoderes que abusan de sus habilidades.", "4" ,"24", Foto2, "2019", "27:00:00", "false", Foto59)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Serie (Nombre, Genero, Director, Protagonista, DescripcionCorta, Temporadas, Episodios, FotoDeSerie, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Arcane", "Fantasia", "Ash Brannon", "Ella Punrell", "Caitlyn, una vigilante rebelde, recorre la ciudad subterránea en busca de Silco. Jayce se convierte en objetivo al intentar acabar con la corrupción en Piltover. Un protegido sabotea a su mentor en el Consejo mientras una tecnología mágica evoluciona a gran velocidad.","2" ,"12", Foto20, "2021", "6:00:00", "false", Foto61)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Pelicula (Nombre, Genero, Director, Protagonista, DescripcionCorta, FotoDePelicula, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Fast and Furious 9", "Accion", "Justin Lin", "Vin Diesel", "Dom Toretto lleva una vida tranquila, pero sabe que el peligro siempre acecha. Esta vez, Dom y el equipo se reúnen para impedir un complot a escala mundial, liderado por uno de los asesinos más peligrosos y hábiles al volante a los que se han enfrentado; un hombre que además es el hermano desaparecido de Dom, Jako.", Foto3, "2021", "2:20:30", "false", Foto60)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Pelicula (Nombre, Genero, Director, Protagonista, DescripcionCorta, FotoDePelicula, AnoDePublicacion, Duracion, Lista, FotoPaisaje) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [("Ready Player one", "Drama", "Steven Splilberg", "Tye Sheridan", "Año 2045. El adolescente Wade Watts es solo una de las millones de personas que se evaden del sombrío mundo real para sumergirse en un mundo utópico virtual donde todo es posible: OASIS. Wade participa en la búsqueda del tesoro que el creador de este mundo imaginario dejó oculto en su obra. No obstante, hay gente muy peligrosa compitiendo contra él.", Foto21, "2018", "2:20:00", "false", Foto62),
("Top Gun Maverik", "Accion", "Joseph Kosinski", "Tom Cruise", "Tras más de 30 años de servicio como uno de los mejores aviadores de la Armada, Pete Maverick Mitchel se encuentra donde siempre quiso estar, empujando los límites como un valiente piloto de pruebas.", Foto22, "2021", "2:11:00", "false", Foto63)]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Usuario (Nombre, Genero, FotoDePerfil, Contrasena, DNI, TipoDeCuenta, FechaDeNacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("Aner Jimenez", "Hombre", Foto19, "cev2408", "51699087Y", "Premium", "30-03-03")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Usuario (Nombre, Genero, FotoDePerfil, Contrasena, DNI, TipoDeCuenta, FechaDeNacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("Iker Randez", "Hombre", Foto38, "Ikerrda2345", "51267507S", "Normal", "05-05-02")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Cantante (Nombre, Grupo) VALUES (%s, %s)"
val = [("Bad Bunny", "-"),
("Rick Astley", "-"),
("Kanye West", "-")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Cantante (Nombre, Grupo) VALUES (%s, %s)"
val = [("Frank Karuba", "Twisted Sister"),
("Danny Elfman", "Oingo Boingo"),
("Maurice White", "Earth wind and fire")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Grupo (Nombre, Cantante) VALUES (%s, %s)"
val = [("Badfinger", "AI Wodstke"),
("Aerosmith", "Steven Tyler"),
("Talking Heads", "David Byrne")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Grupo (Nombre, Cantante) VALUES (%s, %s)"
val = [("Frank Karuba", "Twisted Sister"),
("Danny Elfman", "Oingo Boingo"),
("Maurice White", "Earth wind and fire")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Reparto (Nombre, Rol) VALUES (%s, %s)"
val = [("Steven Spilberg", "Director"),
("Ella Punrell", "Actriz"),
("Tom Cruise", "Actor")]
mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO Reparto (Nombre, Rol) VALUES (%s, %s)"
val = [("Bryan Cranston", "Actor"),
("Jensen Ackles", "Actor"),
("Vin Diesel", "Actor")]
mycursor.executemany(sql, val)
mydb.commit()
