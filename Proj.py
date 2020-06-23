import sqlite3
import random
import datetime
import sqlite3 as sql
conn=sql.connect("student.sqlite")
conn=sqlite3.connect('student.db')
c= conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS Auteur(
      Nauteur INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      nomA TEXT,
      prenomA TEXT,
      nationaliteA TEXT
    )
""")
conn.commit()
#Création de la table Livre
c.execute("""
    CREATE TABLE IF NOT EXISTS Livre(
      Nlivre INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      num_ISBN NUMERIC,
      titre TEXT,
      nbPages INTEGER,
      annéeS INTEGER,
      prix REAL 
    )
""")
conn.commit()
#Création de la table Possede
c.execute("""
    CREATE TABLE IF NOT EXISTS Possede(
      Nlivre INTEGER,
      Nauteur INTEGER,
      PRIMARY KEY(Nlivre,Nauteur),
      FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre),
      FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur)
    )
""")
conn.commit()
#Création de la table Class
c.execute("""
    CREATE TABLE IF NOT EXISTS Class(
      numClass INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      nomclass TEXT
    )
""")
conn.commit()
#Création de la table Etudiant
c.execute("""
    CREATE TABLE IF NOT EXISTS Etudiant(
      num_etu INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      nomE TEXT,
      prenomE  TEXT,
      date_naissance NUMERIC,
      ville TEXT,
      dateInscripBU TEXT,
      dateAbs TEXT,
      numClass INTEGER,
      FOREIGN KEY(numClass) REFERENCES Class(numClass)
    )
""")
conn.commit()
#Création de la table  Pret 
c.execute("""
    CREATE TABLE IF NOT EXISTS Pret(
      Npret INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      num_etu INTEGER,
      Nlivre INTEGER,
      datePret NUMERIC,
      dateRetour NUMERIC,
      DateRetourPrevue NUMERIC,
      FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),
      FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre)
    )
""")
conn.commit()
#Création de la table Enseignant 
c.execute("""
    CREATE TABLE IF NOT EXISTS Enseignant(
      num_ens INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      nomP TEXT,
      prénomP TEXT,
      specialite TEXT,
      departement TEXT
    )
""")
conn.commit()
#Création de la table Cours 
c.execute("""
    CREATE TABLE IF NOT EXISTS Cours(
      num_cours INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      nomC TEXT,
      nb_heures NUMERIC,
      num_ens INTEGER,
      FOREIGN KEY(num_ens) REFERENCES Enseignant(num_ens)
    )
""")
conn.commit()
#Création de la table Resultat
c.execute("""
    CREATE TABLE IF NOT EXISTS Resultat(
      num_etu INTEGER,
      num_cours INTEGER,
      note REAL,
      PRIMARY KEY(num_etu,num_cours),
      FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),
      FOREIGN KEY(num_cours) REFERENCES Cours(num_cours)
    )
""")
conn.commit()
#Création de la table CHARGE
c.execute("""
    CREATE TABLE IF NOT EXISTS Charge(
      num_cours INTEGER,
      num_ens INTEGER,
      nbH REAL,
      PRIMARY KEY(num_cours,num_ens),
      FOREIGN KEY(num_cours) REFERENCES Cours(num_cours),
      FOREIGN KEY(num_ens) REFERENCES Enseignant(num_ens)
    )
""") 
conn.commit()
#Création de la table Inscrit
c.execute("""
    CREATE TABLE IF NOT EXISTS Inscrit(
      num_etu INTEGER,
      num_cours INTEGER,
      dateInsC TEXT,
      PRIMARY KEY(num_etu,num_cours),
      FOREIGN KEY(num_cours) REFERENCES Cours(num_cours),
      FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu)
    )
""")
conn.commit()
c.close()
conn.close()
#la partie 2
#Q1 ---fonction insBU(nomE)---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def insBU(nomE):
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req1="SELECT dateInscripBU FROM Etudiant WHERE nomE=?"

  c.execute(req1,[nomE])

  data1=c.fetchall()
  c.close()
  conn.close() 
  if not data1:
      return "il n'ya pas Date d'inscription de l'étudiant "
  else:
      return data1
print('------------------------------------------1---------------------\n')
print("Date d'inscription de l'étudiant 'ABIB' :", insBU('ABIB'))
print("Date d'inscription de l'étudiant 'EL HILALI' :", insBU('EL HILALI '))
print("Date d'inscription de l'étudiant 'BECHCHAR' :", insBU('BECHCHAR'))
print("Date d'inscription de l'étudiant 'FEDDOUL' :", insBU('FEDDOUL'))
#Q2 ---fonction incCour(num_cours)---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()

def insCour(num_cours):
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req2='''Select nomE,prenomE from Etudiant 
  inner join Inscrit on Inscrit.num_etu=Etudiant.num_etu 
  inner join Cours on Cours.num_cours =inscrit.num_cours 
  where Inscrit.num_cours=?'''

  c.execute(req2, [num_cours])

  data2=c.fetchall()
  c.close()
  conn.close()
  if not data2:
      return "! il n'y a pas d'étudiant inscrit dans le cours N° :" +str(num_cours)
  else:
      return data2
print('------------------------------------------1---------------------\n')
print("le nom et le prenom de l'étudiant inscrit dans le cours N° 6:", insCour(6))
#Q3 ---fonction ResuEtu(num_etu)---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def ResuEtu(num_etu):
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req3='''SELECT nomE,prenomE,note,nomC,AVG(note),MAX(note),MIN(note) FROM Etudiant 
  inner join Resultat on Resultat.num_etu=Etudiant.num_etu 
  inner join Cours on Cours.num_cours =Resultat.num_cours 
  where Etudiant.num_etu=?'''

  c.execute(req3,[num_etu])

  data3=c.fetchall()
  c.close()
  conn.close() 
  if not data3:
      return "! il n'y a pas de resultat sur les cours de l'étudiant N° :" +str(num_etu)
  else:
      return data3
print('------------------------------------------1---------------------\n')
print(" le nom de cours et le nom, prénom et la note de l'étudiant de N° 6 :", ResuEtu(6))
print(" le nom de cours et le nom, prénom et la note de l'étudiant de N° 6 :", ResuEtu(50))
print(" le nom de cours et le nom, prénom et la note de l'étudiant de N° 6 :", ResuEtu(27))
#Q4 ---resultEchec()---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def resultEchec():
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req4='''SELECT nomE,prenomE,note,AVG(note),nomC FROM Etudiant 
  inner join Resultat on Resultat.num_etu=Etudiant.num_etu 
  inner join Cours on Cours.num_cours =Resultat.num_cours
  WHERE Resultat.note<10 GROUP BY Cours.nomC'''

  c.execute(req4)

  data4=c.fetchall()
  c.close()
  conn.close() 
  if not data4:
    return "! il n'ya pas de de resultat des cours de note:" 
  else:
    return data4
print('------------------------------------------1---------------------\n')
print("le nom de cours et le nom, prénom et la note de l'étudiant qui a note<10 :",resultEchec() )
#Q5 ---fonction insr()---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def insr():
  conn = sqlite3.connect('student.db')
  c = conn.cursor()  
  req5='''SELECT nomE from Etudiant 
  inner join Inscrit on Inscrit.num_etu=Etudiant.num_etu 
  inner join Cours on Cours.num_cours =inscrit.num_cours 
  WHERE NOT EXISTS (SELECT * FROM Cours WHERE NOT EXISTS (SELECT * FROM Inscrit))'''
  c.execute(req5)

  data5=c.fetchall()
  c.close()
  conn.close() 
  for row in data5:
    print(row)
  return data5
print('------------------------------------------1---------------------\n')
print(" les noms des étudiant inscrit dans tous les cours :",insr())
#Q6 fonction ---empLiv(Nlivre)---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def empLiv(Nlivre):
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req6='''Select nomE from Etudiant 
  inner join Pret on Pret.num_etu=Etudiant.num_etu 
  inner join Livre on Livre.Nlivre =Pret.Nlivre 
  where Pret.Nlivre=?'''
  c.execute(req6,[Nlivre])

  data6=c.fetchall()
  c.close()
  conn.close() 
  if not data6:
      return "! il n'y a pas d'étudiant qui ont empruntés le livre N° :" +str(Nlivre)
  else:
      return data6
print('------------------------------------------1---------------------\n')
print(" le nom d'étudiant qui ont empruntés le livre N° 7 :", empLiv(7))
print(" le nom d'étudiant qui ont empruntés le livre N° 1 :", empLiv(1))
#Q7 ---fonction retard()---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def retard():
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req7=''' SELECT nomE, prenomE FROM Etudiant 
  inner join Pret on  Pret.num_etu=Etudiant.num_etu
  WHERE Nlivre IN ( SELECT Nlivre FROM Pret WHERE dateRetour IS NULL) '''
  c.execute(req7)

  data7=c.fetchall()
  c.close()
  conn.close() 
  if not data7:
    return "we don't find this Etu"
  else:
    return data7
print('------------------------------------------1---------------------\n')
print(" le nom et le prénom d'étudiant n’ayant pas encore rendus au moins un livre :",retard())
#Q8 ---fonction noEmp()---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def noEmp():
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req8=''' SELECT titre FROM Livre 
  inner join Pret on Livre.Nlivre =Pret.Nlivre 
  where NOT EXISTS (select * from Pret WHERE Livre.Nlivre =Pret.Nlivre )'''
  c.execute(req8)

  data8=c.fetchall()
  c.close()
  conn.close() 
  if not data8:
    return "tout les livres ont déjà été emprunter"
  else:
      for row in data8:
          print(row)
  return 'selected Successfully!'
print('------------------------------------------1---------------------\n')
print(" les noms des livres empruntés par personne :",noEmp())
#Q9 ---fonction ResultTot()---
import sqlite3
conn = sqlite3.connect('student.db')
c = conn.cursor()
def  ResultTot():
  conn = sqlite3.connect('student.db')
  c = conn.cursor()
  req9=''' SELECT nomC,nomclass,AVG(note) FROM Resultat 
  inner join Cours on Resultat.num_cours =Cours.num_cours 
  inner join Etudiant on Resultat.num_etu=Etudiant.num_etu 
  inner join Class on Class.numClass =Etudiant.numClass
  GROUP BY nomC,nomclass'''
  c.execute(req9)

  data9=c.fetchall()
  c.close()
  conn.close() 
  for row in data9:
    print(row[0],row[1],row[2])
print('------------------------------------------1---------------------\n')
print(" le nom de la classe et la moyenne des notes obtenues par cours obtenue dans la classe :", ResultTot())




##Modification des Tables
#Q1 : 
import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
def updateCours(num_cours):
     newNom= input("entrer le nouveau nom de cours "+str(num_cours)+" : ")
     cur.execute("""UPDATE Cours SET nomC=? where 
     num_cours=?""",(newNom,num_cours,))
     a=cur.execute("""select num_cours,nomC from Cours where num_cours=?""",(num_cours,))
     print("le nouveau cours numero :",a.fetchone())

num_cours=int(input("entrer le numero du cours: "))
updateCours(num_cours)
conn.commit()
conn.close()

#Q2 : 
import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
def deleteCours(num_cours):
     cur.execute("""DELETE FROM Cours where 
     num_cours=?""",(num_cours,))

num_cours=int(input("entrer le numero du cours: "))
deleteCours(num_cours)
conn.commit()
conn.close()

## la partie 3
#Q1:
from matplotlib import pyplot as plt 
import sqlite3 
connection = sqlite3.connect ('student.db') 
cursor = connection.cursor ( ) 
name = ['-10', '10-12', '12-14', '14+']
data = [74, 69, 61, 196]

explode=(0, 0.15, 0, 0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()
#Q2:
from matplotlib import pyplot as plt 
import sqlite3 
connection = sqlite3.connect ('student.db') 
cursor = connection.cursor ( ) 

note = " SELECT note From Resultat INNER JOIN Etudiant ON Etudiant.num_etu = Resultat.num_etu GROUP BY note " 
cursor.execute ( note ) 
y = [ item [ 0 ] for item in cursor.fetchall() ] 


nbr_etu = " SELECT COUNT ( E.num_etu ) FROM Etudiant AS E INNER JOIN Resultat ON Resultat.num_etu = E.num_etu GROUP BY note "
cursor.execute ( nbr_etu ) 
x = [item [ 0 ] for item in cursor.fetchall() ] 
plt.xlabel ( " Note ") 
plt.ylabel ( " Nombre d'Etu " ) 
plt.bar ( y , x , 0.07 ) 
plt.show ( ) 
