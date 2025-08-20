import random

class De:
    def __init__(self,valeur=random.randint(1,6),verrouillage=False):
        self.valeur=valeur
        self.verrouillage=verrouillage
    
    def verrouiller(self):
        self.verrouillage=True
    
    def deverrouiller(self):
        self.verrouillage=False
        
    def lancer(self):
        self.valeur=random.randint(1,6)
        return self.valeur

de1=De()
de2=De()
de3=De()
de4=De()
de5=De()


feuille_score=[]
#Légende tableau_score=[description,1,2,3,4,5,6,1er total,"Brelan","Full","Carré","Petite suite","Grande suite","Yam's","Chance", Total]

def lancer_des(de1,de2,de3,de4,de5):
    if not(de1.verrouillage):
        de1.lancer()
    if not(de2.verrouillage):
        de2.lancer()
    if not(de3.verrouillage):
        de3.lancer()
    if not(de4.verrouillage):
        de4.lancer()
    if not(de5.verrouillage):
        de5.lancer()
    return([de1.valeur,de2.valeur,de3.valeur,de4.valeur,de5.valeur])


"""
Test des différentes combinaisons possibles
Rappel des règles du Yam's
Prendre au 1 2 3 4 5 6 

"""
def est1(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==1:
            score+=1
    return score

def est1(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==1:
            score+=1
    return score

def est2(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==2:
            score+=2
    return score

def est3(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==3:
            score+=3
    return score

def est4(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==4:
            score+=4
    return score

def est5(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==5:
            score+=5
    return score

def est6(resultat_lancer):
    score=0
    for v in resultat_lancer:
        if v==6:
            score+=6
    return score

def estx(resultat_lancer):
    score_estx=[]
    score_estx.append(est1(resultat_lancer))
    score_estx.append(est2(resultat_lancer))
    score_estx.append(est3(resultat_lancer))
    score_estx.append(est4(resultat_lancer))
    score_estx.append(est5(resultat_lancer))
    score_estx.append(est6(resultat_lancer))
    return (score_estx)

def prendre_au_x(resultat_lancer):
    score_estx=estx(resultat_lancer)
    texte=""
    for i in range (1,7):
        ajout="Prendre au "+str(i)+" : " +str(score_estx[i-1])+" points \n"
        texte+=ajout
    return texte

def somme_de(resultat_lancer):
    somme=0
    for v in resultat_lancer:
        somme+=v
    return somme

def triple(resultat_lancer):
    valeur_du_de=0
    for i in range(5):
        valeur_du_de_boucle=resultat_lancer[i]
        compteur=0
        for j in range(5):
            if resultat_lancer[j]==valeur_du_de_boucle:
                compteur+=1
        if compteur>=3:
            valeur_du_de=valeur_du_de_boucle
            return (True,valeur_du_de)
            break
    return(False,valeur_du_de)

def quadruple(resultat_lancer):
    valeur_du_de=0
    for i in range(5):
        valeur_du_de_boucle=resultat_lancer[i]
        compteur=0
        for j in range(5):
            if resultat_lancer[j]==valeur_du_de_boucle:
                compteur+=1
        if compteur>=4:
            valeur_du_de=valeur_du_de_boucle
            return (True,valeur_du_de)
            break
    return(False,valeur_du_de)

def triple_et_double(resultat_lancer):
    est_brelan=triple(resultat_lancer)
    liste_des=resultat_lancer.copy()
    if est_brelan[0]:
        for i in range(3):
            liste_des.remove(est_brelan[1]) #s'il y a un brelan, on éjecte le triple du résultat des lancers, afin qu'il ne reste que deux dés
        if len(liste_des)==2:  #pour éviter le cas où il y a un carré ou un yam's 
            if liste_des[0]==liste_des[1]:
                return (True, est_brelan [1],liste_des[0]) #on retourne (booléen, valeur_triple, valeur_double)
    return (False,0,0)
               

def brelan(resultat_lancer):
    score=0
    est_brelan=triple(resultat_lancer)
    if est_brelan[0]:
        score+=est_brelan[1]*3
    return score

def carre(resultat_lancer):
    score=0
    est_carre=quadruple(resultat_lancer)
    if est_carre[0]:
        score+=est_carre[1]*4
    return score

def full(resultat_lancer):
    score=0
    est_full=triple_et_double(resultat_lancer)
    if est_full[0]:
        score=25
    return score

def grande_suite(resultat_lancer):
    score = 0
    liste_des=resultat_lancer.copy()
    liste_des.sort()
    if liste_des==[1,2,3,4,5] or liste_des==[2,3,4,5,6]:
        score=40
    return score

def petite_suite(resultat_lancer):
    score = 0
    if (1 in resultat_lancer and 2 in resultat_lancer and 3 in resultat_lancer and 4 in resultat_lancer):
        score=30
    if (2 in resultat_lancer and 3 in resultat_lancer and 4 in resultat_lancer and 5 in resultat_lancer):
        score=30
    if (3 in resultat_lancer and 4 in resultat_lancer and 5 in resultat_lancer and 6 in resultat_lancer):
        score=30
    return score

def yams(resultat_lancer):
    score=0
    compteur=1
    valeur=resultat_lancer[0]
    for v in resultat_lancer[1:]:
        if v==valeur:
            compteur+=1
    if compteur==5:
        score=50
    return score

def chance(resultat_lancer):
    score=somme_de(resultat_lancer)
    return score

def resultat_majeur(resultat_lancer):
    combinaisons_majeures=["Brelan","Full","Carré","Petite suite","Grande suite","Yam's","Chance"]
    score_estx=estx(resultat_lancer)
    score_combi_majeures=[brelan(resultat_lancer),full(resultat_lancer),carre(resultat_lancer),petite_suite(resultat_lancer),grande_suite(resultat_lancer),yams(resultat_lancer),chance(resultat_lancer)]
    texte="Résultat du lancer : " + str(resultat_lancer) + "\n"
    for i in range (1,7):
        ajout="Prendre au "+str(i)+" : " +str(score_estx[i-1])+" point(s) \n"
        texte+=ajout
    for i in range(7):
        ajout=str(combinaisons_majeures[i]) + " : " + str(score_combi_majeures[i]) + " point(s) \n"
        texte+=ajout
    return [texte, score_estx,score_combi_majeures]

def remplir_score(choix, score_estx,score_combi_majeures,feuille_score):
    score=-1 #en cas d'erreur, si aucun input n'est reconnu parmi les combinaisons possibles, ou combinaison déjà choisie
    while score==-1:
        choix.lower()
        for i in range (1,7):
            if "prendre au "+str(i) in choix and feuille_score[i]==-1:
                score+=score_estx[i-1]+1
                feuille_score[i]=score
        if "brelan" in choix and feuille_score[8]==-1:
            score+=score_combi_majeures[0]+1
            feuille_score[8]=score
        if "full" in choix and feuille_score[9]==-1:
            score+=score_combi_majeures[1]+1
            feuille_score[9]=score
        if "carre" in choix and feuille_score[10]==-1:
            score+=score_combi_majeures[2]+1
            feuille_score[10]=score
        if "petite suite" in choix and feuille_score[11]==-1:
            score+=score_combi_majeures[3]+1
            feuille_score[11]=score
        if "grande suite" in choix and feuille_score[12]==-1:
            score+=score_combi_majeures[4]+1
            feuille_score[12]=score
        if "yams" in choix and feuille_score[13]==-1:
            score+=score_combi_majeures[5]+1
            feuille_score[13]=score
        if "chance" in choix and feuille_score[14]==-1:
            score+=score_combi_majeures[6]+1
            feuille_score[14]=score
        if score==-1:
            choix=input("La combinaison n'a pas été reconnue ou a déjà été choisie, veuillez en choisir une de nouveau : ")
    somme_mineure=0
    somme_majeure=0
    for i in range(1,7):
        if feuille_score[i]!=-1:
            somme_mineure+=feuille_score[i]
    if somme_mineure !=0:
        feuille_score[7]=somme_mineure
    if feuille_score[7]>=63:
        feuille_score[7]+=35
    for i in range (8,15):
        if feuille_score[i]!=-1:
            somme_majeure+=feuille_score[i]
    if somme_majeure!=0:
        feuille_score[15]=somme_majeure
    return (feuille_score)

def afficher_score(feuille_score):
    texte=str(feuille_score[0]) + "\n"
    for i in range(1,len(feuille_score)):
        if i <=6:
            texte+=str(i) + " : " + str(feuille_score[i]) + "\n"
        if i==7:
            texte+= "Total 1 : " + str(feuille_score[i]) + "\n"
        if i==8:
            texte+= "Brelan : " +str(feuille_score[i]) + "\n"
        if i==9:
            texte+= "Full : " +str(feuille_score[i]) + "\n"
        if i==10:
            texte+= "Carré : " +str(feuille_score[i]) + "\n"
        if i==11:
            texte+= "Petite suite : " +str(feuille_score[i]) + "\n"
        if i==12:
            texte+= "Grande suite : " +str(feuille_score[i]) + "\n"
        if i==13:
            texte+= "Yam's : " +str(feuille_score[i]) + "\n"
        if i==14:
            texte+= "Chance : " +str(feuille_score[i]) + "\n"
        if i==15:
            texte+="Total 2 : " +str(feuille_score[i]) + "\n"
    total=feuille_score[7]+feuille_score[15]
    texte+="Total : "+str(total)+"\n"
    texte=texte.replace("-1","")
    return(texte)   
    








        


    

"""
Test

print ([resultat_lancer])
print (carre([5,5,5,1,5]))
print(full([3,2,3,2,2]))
print(grande_suite([3,2,4,1,5]))
print(yams([3,3,3,2,3]))
print(resultat_majeur(resultat_lancer)[0])
"""
#Début du jeu

tour=1
nb_joueurs=int(input("Entrez le nombre de joueurs : "))
for i in range (nb_joueurs):
    nom_joueur=input("Entrez le nom du joueur " + str(i+1) + " : ")
    feuille_score.append([nom_joueur,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,0])

while tour<=13:
    print("---Début du tour " + str(tour) + "---")
    for j in range(nb_joueurs):
        print("--C'est au tour de "+feuille_score[j][0]+" ! --")
        resultat_lancer=lancer_des(de1,de2,de3,de4,de5)
        for i in range(3):
            valeurs_des=resultat_majeur(resultat_lancer)[0]
            score_estx=resultat_majeur(resultat_lancer)[1]
            score_combi_majeures=resultat_majeur(resultat_lancer)[2]
            print(valeurs_des)
            if i<2:
                a_verrouiller=input ("Quels dés souhaitez vous conserver ? (Entrez 0 si vous voulez choisir directement une combinaison) ")
                if "1" in a_verrouiller:
                    de1.verrouiller()
                if "2" in a_verrouiller:
                    de2.verrouiller()
                if "3" in a_verrouiller:
                    de3.verrouiller()
                if "4" in a_verrouiller:
                    de4.verrouiller()
                if "5" in a_verrouiller:
                    de5.verrouiller()
                resultat_lancer=lancer_des(de1,de2,de3,de4,de5)

                #On déverrouille tous les dés avant le tour suivant
                de1.deverrouiller()
                de2.deverrouiller()
                de3.deverrouiller()
                de4.deverrouiller()
                de5.deverrouiller()

            if i==2 or "0" in a_verrouiller:
                choix=input("Fin du tour, choisissez une combinaison : ")
                feuille_score[j]=remplir_score(choix,score_estx,score_combi_majeures,feuille_score[j]) #il faudra mettre un filtre/une condition en fonction du joueur qui joue
                print(afficher_score(feuille_score[j]))
                break
    tour+=1
