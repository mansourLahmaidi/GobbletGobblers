#!/usr/bin/env python3
# module: tkinter
from tkinter import *
from random import randrange

class Position:
	def __init__( self, var):
		self.var=var
	def getPosition(self):
		return self.var
	def setPosition(self, _var):
		 self.var= _var
_position= Position(0)

class Bac_a_sable(Canvas):
	"Canevas modifié pour prendre en compte quelques actions de la souris"
	def __init__(self, boss, width=80, height=80, bg="white"):
	# invocation du constructeur de la classe parente :
		Canvas.__init__(self, boss, width=width, height=height, bg=bg)
		# association-liaison d'événements <souris> au présent widget :
		self.bind("<Button-1>", self.mouseDown)
		self.bind("<Button1-Motion>", self.mouseMove)
		self.bind("<Button1-ButtonRelease>", self.mouseUp)
	def mouseDown(self, event):
		"Opération à effectuer quand le bouton gauche de la souris est enfoncé"
		self.currObject =None
		# event.x et event.y contiennent les coordonnées du clic effectué :
		self.x1, self.y1 = event.x, event.y
		# <find_closest> renvoie la référence du dessin le plus proche :
		self.selObject = self.find_closest(self.x1, self.y1)
		# modification de l'épaisseur du contour du dessin :
		_position.setPosition(self.coords(self.selObject))
		self.itemconfig(self.selObject, width =3)
		# <lift> fait passer le dessin à l'avant-plan :
		self.lift(self.selObject)
		whatCase(event.x , event.y)
		if whatCase(event.x , event.y) !=(-1,-1):
			deleteDernierePiece(whatCase(event.x , event.y))
	def mouseMove(self, event):
		"Op. à effectuer quand la souris se déplace, bouton gauche enfoncé"
		x2, y2 = event.x, event.y
		dx, dy = x2 -self.x1, y2 -self.y1
		typeObjet=self.type(self.selObject)
		if self.selObject  and  typeObjet== "rectangle"  :
			self.move(self.selObject, dx, dy)
			self.x1, self.y1 = x2, y2
	def mouseUp(self, event):
		"Op. à effectuer quand le bouton gauche de la souris est relâché"
		if self.selObject :
			if canAdd(whatCase(event.x , event.y), taille(self.coords(self.selObject)))== False  :
				couleur2=self.itemcget(self.selObject, "fill")

				Canevas.delete('Gobblet gobblers',self.selObject) 
				Canevas.create_rectangle(_position.getPosition(), outline='black', fill=couleur2)
			else :
				self.itemconfig(self.selObject, width =1)
				#self.selObject =None
		
				couleur=self.itemcget(self.selObject, "fill")
				typeObjet=self.type(self.selObject)

				if typeObjet== "rectangle"  :
					def getCouleurVoid():
						couleur =self.itemcget(self.selObject, "fill")
						return couleur
					def getTailleVoid():
						taille=taille(coordonneesRectangle)
						return taille
					couleur2Int(getCouleurVoid())
					coordonneesRectangle = self.coords(self.selObject)
					taille(coordonneesRectangle)

					#Centrer(self.selObject, whatCase(event.x , event.y),taille(coordonneesRectangle), getCouleurVoid() )

					setCase( whatCase(event.x,event.y), getCouleurVoid(), taille(coordonneesRectangle) )
					""" On supprime un rec s'il s'agit d'un deplacement dans la grille"""	

					if (whatCase(event.x , event.y)) == (0,0) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,55,55,95,95)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,36,37,116,117)
							else :
								Canevas.coords(self.selObject,36,47,116,107)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,26,27,126,127)

					if (whatCase(event.x , event.y)) == (0,1) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,57,245,97,205)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,36,266,116,186)
							else :
								Canevas.coords(self.selObject,36,256,116,196)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,26,174,126,274)


					if (whatCase(event.x , event.y)) == (0,2) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,57,394,97,354)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,36,414,116,334)
							else :
								Canevas.coords(self.selObject,36,404,116,344)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,26,324,126,424)


					if (whatCase(event.x , event.y)) == (1,0) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,205,57,245,97)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,185,37,265,117)
							else :
								Canevas.coords(self.selObject,185,47,265,107)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,174,127,274,27)

					if (whatCase(event.x , event.y)) == (1,1) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,205,205,245,245)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,185,187,265,267)
							else :
								Canevas.coords(self.selObject,185,197,265,257)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,174,174,273,274)


					if (whatCase(event.x , event.y)) == (1,2) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,206,394,246,354)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,186,415,266,335)
							else :
								Canevas.coords(self.selObject,186,405,266,345)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,175,424,275,324)


					if (whatCase(event.x , event.y)) == (2,0) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,406,99,366,59)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,424,119,344,39)
							else :
								Canevas.coords(self.selObject,424,109,344,49)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,434,127,334,27)


					if (whatCase(event.x , event.y)) == (2,1) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,405,205,365,245)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,426,187,346,267)
							else :
								Canevas.coords(self.selObject,426,197,346,257)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,434,174,334,274)


					if (whatCase(event.x , event.y)) == (2,2) :
						if (taille(coordonneesRectangle)) == 1 :
							Canevas.coords(self.selObject,405,394,365,354)
						if (taille(coordonneesRectangle)) == 2 :
							if (couleur2Int(getCouleurVoid())) == 2 :
								Canevas.coords(self.selObject,426,415,346,335)
							else :
								Canevas.coords(self.selObject,426,405,346,345)
						if (taille(coordonneesRectangle)) == 3 :
							Canevas.coords(self.selObject,434,424,334,324)


				else:
					whatCase(event.x , event.y)
			affichePlateau()
			if victoire == True:
				rejouer()

def  couleur2Int(c):
	couleurInt=0
	if c=="red":
		couleurInt=2
	else :
		couleurInt=1
	
	#print(" couleur=" ,couleurToString(couleurInt))
	return couleurInt

def taille( _taille):
	tailleRrectangle=0
	"""Rectangle bleu"""
	if _taille[2]-_taille[0] <=40 : 
		tailleRrectangle=1
	else:
		if _taille[2]-_taille[0] <=80  and _taille[2]-_taille[0] > 40  : 
				tailleRrectangle=2
		else:
			if _taille[2]-_taille[0] <=100 : 
				tailleRrectangle=3
	
	#print( "taille:", tailleToString(tailleRrectangle))
	return tailleRrectangle


"""def Centrer( Object, cle, taille,couleur):
	if cle== (0,0) :
		if taille==1:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(62,65,102,105, outline='black', fill=couleur)
		if taille==2:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(33,52,113,132, outline='black', fill=couleur)
		if taille==3:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(27,33,127,133, outline='black', fill=couleur)
	
	if cle== (1,0) :
		if taille==1:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(201,65,241,105, outline='black', fill=couleur)
		if taille==2:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(180,50,260,130, outline='black', fill=couleur)
		if taille==3:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle( 172 ,  30,272,130, outline='black', fill=couleur)
		
		if cle== (2,0) :
		if taille==1:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(201,65,241,105, outline='black', fill=couleur)
		if taille==2:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle(183,54,263,134, outline='black', fill=couleur)
		if taille==3:
			Canevas.delete('Gobblet gobblers',Object) 
			Canevas.create_rectangle( 172 ,  30,272,130, outline='black', fill=couleur)

"""

																																																																																																																																																																			
def teste(a,b):
	print("Case (" , a ,", " , b,")")

def whatCase(a,b):
	if a<149 :
		if b<169:
			a,b=0,0

		if b>169 and b<300 :
			a,b=0,1
		if b>300:
			a,b=0,2		
	if a>149 and a<300:
		if b<169:
			if b<169:
				a,b=1,0

		if b>169 and b<300 :
				a,b=1,1

		if b>300:
			a,b=1,2
				
	if a>300 and a<470 :
		if b<169:
			if b<169:
				a,b=2,0

		if b>169 and b<300 :
				a,b=2,1

		if b>300:
			a,b=2,2
	"""a ou b hors de la grille"""
	if a<3:
		"""teste(a,b)	"""		
		return a,b
	
	else :
		return -1,-1


if __name__ == '__main__':
# ---- Programme de test ----
	Mafenetre = Tk()
	Mafenetre.title('GobbletGobblers')
	Mafenetre.geometry('800x700+400+300')# mise en place du canevas 
	Largeur = 780
	Hauteur = 550

	Canevas =Bac_a_sable(Mafenetre, width =Largeur, height =Hauteur, bg ='ivory')

	Canevas.pack(padx =5, pady =5)
	def affiche():
		Canevas.create_rectangle(600, 40, 640, 80, outline='black', fill='blue')
		Canevas.create_rectangle(550, 40, 590, 80, outline='black', fill='blue')

		Canevas.create_rectangle(500, 90, 580, 150, outline='black', fill='blue')
		Canevas.create_rectangle(590, 90, 670, 150, outline='black', fill='blue')
			
		Canevas.create_rectangle(480, 170, 580, 270, outline='black', fill='blue')
		Canevas.create_rectangle(590, 170, 690, 270, outline='black', fill='blue')


		Canevas.create_rectangle(600, 280, 640, 320, outline='black', fill='red')
		Canevas.create_rectangle(550, 280, 590, 320, outline='black', fill='red')

		Canevas.create_rectangle(500, 330, 580, 390, outline='black', fill='red')	
		Canevas.create_rectangle(590, 330, 670, 390, outline='black', fill='red')

		Canevas.create_rectangle(480, 420, 580, 520, outline='black', fill='red')
		Canevas.create_rectangle(590, 420, 690, 520, outline='black', fill='red')


		Canevas.create_line(5,5,5,450)
		Canevas.create_line(150,5,150,450)
		Canevas.create_line(300,5,300,450)
		Canevas.create_line(470,5,470,450)
		Canevas.create_line(5,5,470,5)

		Canevas.create_line(5,450,470,450)
		Canevas.create_line(5,300,470,300)
		Canevas.create_line(5,150,470,150)
	affiche()
	def Effacer():
		Canevas.delete(ALL)
	def rejouer():
		global victoire
		Effacer()
		initPlateau() #On refait un nouveau plateau
		victoire = False #On ré-initialise la variable de victoire pour la prochaine partie
		affiche()

	bouton=Button(Mafenetre, text="Fermer", command=Mafenetre.quit)
	bouton.pack()

	bouton=Button(Mafenetre, text="rejouer", command= rejouer)
	bouton.pack()

	"""
	Structure de données pour le projet Gobblet Gobblers
	____________________________________________________
	Représentation des couleurs:
	1 = bleu
	2 = rouge
	Représentation des tailles:
	1 = petit
	2 = moyen
	3 = grand
	Représentation des pièces:
	Une pièce = une liste sous la forme [numCouleur,numTaille]
	ex : petite pièce bleue = [1,1]
	Représentation des cases du plateau:
	Une case du plateau de coordonnée (x,y) = un élément du dictionnaire plateau avec une clé (x,y)
	Chaque case du plateau est une liste
	On peut ajouter à chaque case une liste de 3 pièces maximum imbriquées de 0 à 2 de la plus petite pièce à la plus grande
	"""

	plateau = {}
	victoire = False
	#dictionnaire

	def initPlateau():
		global plateau
		coordonnees = '012'
		for i in list(coordonnees):
			for j in list(coordonnees):
					plateau[(int(i),int(j))] = []

	def getCase(cle):
		global plateau
		coordonnees = '012'
		for i in list(coordonnees):
			for j in list(coordonnees):
					if a==i and b==j:
						return plateau[(int(cle))]
	
	def setCase(cle, couleur, taille):
		plateau[cle].append([couleur, taille])

	def affichePlateau():
		global victoire
		print("Contenu du plateau à cet instant : ")
		print("__________________________________ ")
		for cle in plateau.keys():
			print("Nombre de pieces a la case = ",cle,":",getNbPieces(cle))
			#print("Couleur de la deuxieme piece = ", getDernierePiece(cle))
			if getNbPieces(cle) > 0 :
				print("Taille de la premiere piece a la case = ", cle,":",getTaille(cle,0))
				print("Couleur de la derniere piece a la case = ", cle,":", getCouleur(cle,getDernierePiece(cle)))
		verifVictoire()
		print("Victoire ?", victoire)
        
	def getCouleur(cle,numPiece):
		global plateau
		return plateau[cle][numPiece][0]

	def getTaille(cle,numPiece):
		global plateau
		return plateau[cle][numPiece][1]

	def getNbPieces(cle):
		global plateau
		return len(plateau[cle])

	def canAdd(cle, tailleCourante):
		if cle == (-1,-1) :
			return False
		if getNbPieces(cle) == 0 :
			return True
		if getNbPieces(cle) < 3 :
			if tailleCourante > getTaille(cle,getDernierePiece(cle)) :
				return True
			else :
				return False
		else :
			return False

	def getDernierePiece(cle):
		return getNbPieces(cle)-1

	def deleteDernierePiece(cle):
		plateau[cle] = plateau[cle][:getNbPieces(cle)-1]
				
	def tailleToString(x):
		if x == 1:
			return "petite"
		elif x == 2:
			return "moyenne"
		elif x == 3:
			return "grande"

	def couleurToString(x):
		if x == 1:
			return "bleue"
		elif x == 2:
			return "orange"
			
	def checkLigne(x,y,u,v,t,z):
		global victoire
		if(getNbPieces((x,y)) > 0):
			c1 = getCouleur((x,y),getDernierePiece((x,y)))
			if(getNbPieces((u,v)) > 0):
				c2 = getCouleur((u,v),getDernierePiece((u,v)))
				if(getNbPieces((t,z)) > 0):
					c3 = getCouleur((t,z),getDernierePiece((t,z)))
					if(c1 == c2 and c2 == c3):
						victoire = True

	def verifVictoire():
		#Lignes horizontales :
		checkLigne(0,0,1,0,2,0)
		checkLigne(0,1,1,1,2,1)
		checkLigne(0,2,1,2,2,2)
		#Lignes verticales :
		checkLigne(0,0,0,1,0,2)
		checkLigne(1,0,1,1,1,2)
		checkLigne(2,0,2,1,2,2)
		#Diagonales :
		checkLigne(0,0,1,1,2,2)
		checkLigne(2,0,1,1,0,2)
    
	""" On considère qu'on note le plateau de jeu dans un plan de cette façon (avec O représentant les cases)
	  0 1 2 (X)
	0 O O O
	1 O O O
	2 O O O
	(Y)"""

	initPlateau()
	Mafenetre.mainloop()

