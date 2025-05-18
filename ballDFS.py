import copy
import tkinter as tk
from tkinter import ttk, Canvas

# Variables globales utilisées par les deux méthodes DFS et BFS
ALL_COLORS = ['red', 'blue', 'yellow', 'black', 'green', 'purple', 'orange', 'cyan','magenta4','green4','aquamarine']   # 11 couleurs dont 'black' = vide
NTUBES = 0
LTUBES = 0
THIST = []
TVUES = []
Minit = []
LMVT = []
SOLUTION = []
MSOLUTION = []
TROUVE = False
# variables d'affichage graphiques pour Tkinter
EXTERNAL_OFFSET = 10
OFFSET_X = 20
OFFSET_Y = 20
DIAMETER = 20


class Jeu():                 # Chaque étape du jeu avec ses mouvements possibles et sa méthode de recherche ici DFS on explore en profondeur
    def __init__(self, mat):
        self.minit = mat 
        self.lmvt = []
        self.cherche_solution(self.minit)

    def cherche_solution(self,m):
        global TROUVE
        global SOLUTION
        global THIST
        global TVUES
        
        self.m = m
        THIST.append(self.m)
        TVUES.append(self.m)

        niveau = len(THIST) * 'R'
        print('niveau et nb THIST',niveau)
        
        self.lmvt = cherche_mvt(self.m)
        if self.lmvt == []:
            THIST.pop()
            print('pas de mouvements trouvés pour ce niveau ', len(THIST))
            if len(THIST) == 0:
                print('********** impossible ')
                exit 
        else:
            while (len(self.lmvt) > 0)  and (not TROUVE):
                u, v,k = self.lmvt.pop()
                SOLUTION.append((u,v,k))
                test_essai = deplace(self.m,u,v,k)
                
                if dejavu_m(test_essai) :
                    print('deja vue')
                    SOLUTION.pop()
                    break
                               
                if compare_m_m(test_essai,MSOLUTION):
                    TROUVE = True
                    print('trouvé')
                    print(SOLUTION)
                    exit
                else:
                    Jeu(test_essai)
                    if not TROUVE:
                        SOLUTION.pop() 
                   
        
            

class App(tk.Tk):                # définit la fenêtre self=window=tk.Tk
    def __init__(self ):        # on transmet le jeu et la liste des mouvements
        super().__init__()
        # transmission du jeu
        
        # ************ affichage fenêtre globale
        self.title('Recherche de solution , méthode Deep First Search, recherche en profondeur')
        self.resizable(True, True)
        self.minsize(800,800)
       

        # ************* ce qu'on peut placer dans la fenêtre : les widgets : 
        self.menu = Menu(self)
        self.tubes = Tubes(self)
        
        # boucle du jeu
        self.mainloop()

  
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background='red').pack(expand=True,fill='both')
        self.place(x=0,y=0,relwidth=0.1,relheight=1)   # en pourcentage
        for i in range(15):
            self.label = tk.Label(self, text=str(i),fg='black',bg='white')
            self.label.place(x=10,y=30 +i*40)

        
class Tubes(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        global NTUBES
        global LTUBES
        global M
        global LMVT

       
        self.main_cv =Canvas(self,background="wheat")
        self.main_cv.pack(expand=True, fill='both')
       
        # affichage initial
        for j in range(LTUBES):
            for i in range(NTUBES):
                colorm = color_m(M,i,j)
                #print(colorm)
                self.trace_oval(i,j,colorm)
          

        #********************* début du jeu  
        print(M)      
        
        # voir la solution
        SOLUTION.reverse()
        LMVT =SOLUTION
        self.place(x=100,y=0,relwidth=0.9,relheight=0.8)   # en pourcentage
        self.labelbutton = tk.Label(self, text="Voici la solution pas à pas ")
        self.labelbutton.place(x=400,y=10)
        self.buttonsuiv = tk.Button(self, text="Attendez je réfléchis !", command=self.on_enter)
        self.buttonsuiv.place(x=400,y=50)
        if LMVT != []:
            u,v,k=LMVT[-1]
            textsuiv = 'voici le mouvement suivant du tube '+ str(u)+ ' vers '+str(v)
            self.buttonsuiv.config(text=textsuiv)
            
        else:
            self.buttonsuiv.config(text='attendez je réfléchis !')  

    def on_enter(self):
        global LMVT
        print("Enter button clicked!")

        if not TROUVE: 
            self.button.config(text="Attendez je réfléchis, je n'ai pas encore trouvé la solution")
        elif LMVT != []:
            u,v,k = LMVT.pop()
            
            print('----------M au click')
            print(M)
            print('mouvement de i vers j, k fois',u,v,k)
            self.maj(u,v,k)
            u,v,k=LMVT[-1]
            textsuiv = 'voici le mouvement suivant du tube '+ str(u)+ ' vers '+str(v)
            self.buttonsuiv.config(text=textsuiv)
        else:
            textfin = 'Fin du jeu atteinte en '+str(len(THIST))+' coups'
            self.buttonsuiv.config(text=textfin)

    def maj(self,i,j,k):
        print('on va de ', i,  'vers ', j, k, 'fois')
        global M
        # le mouvement va se faire du tube i vers le tube j, la matrice est avant mouvement
        # je cherche la position de la balle supérieure de i et sa couleur
        posi = len(M[i]) -1
        color = M[i][posi]
        for nb in range(k):
            self.trace_oval(i,len(M[i]) -1,'black')  # on met le point de départ en k noir
            M[i].pop()                                 # on met à jour le point de départ 
            M[j].append(color)
            self.trace_oval(j,len(M[j])-1,color)  # on met le point d'arrivéé
        

        

    def trace_oval(self, i,posi,colorm) : 
        self.main_cv.create_oval( OFFSET_X + posi * ( OFFSET_X+DIAMETER),
                       EXTERNAL_OFFSET+OFFSET_Y +(i)*( OFFSET_Y+ DIAMETER),
                       OFFSET_X + posi *  (OFFSET_X+DIAMETER) +DIAMETER,
                       EXTERNAL_OFFSET+OFFSET_Y +(i)* (OFFSET_Y+DIAMETER)+DIAMETER , fill=colorm)  


def color_m(m,i,j):
    if j>len(m[i])-1:
        return 'black'
    else:
        return m[i][j]

def deplace(m,i,j,nb):
    # doit déplacer n balles de du tube i vers le tube j
    posi = len(m[i]) -1
    color = m[i][posi]
    n=copy.deepcopy(m)
    while nb > 0:
        n[i].pop()
        n[j].append(color)
        nb -=1    
    return n
    
def dejavu_m(m):
    # le but est de comparer m aux jeux déjà vus
    if m in TVUES:          # les tubes de m 

        return True
    else :
        for t in TVUES:     #t est une matrice jeu
            return compare_m_m(m,t)
    return False
            


def compare_m_m(m1,m2):
    #print('*********** compare ')
    if m_properties(m1) != m_properties(m2):
        #print('false properties dans compare')
        return False
    # les tubes peuvent être dans le désordre
    for l in m1:
        if l not in m2:
            #print('False dans compare')
            return False
    return True

def test_uniform(m,t) :
    # doit retourner  si uniforme 0 ou 1 
    #  
    if len(m[t]) == 1:
        return True
    else:
        color = m[t][len(m[t])-1] 
        j=0
        while color == m[t][len(m[t])-1-j] :
            j += 1
            if len(m[t])-1-j ==-1:
                break
        if j== len(m[t]):
            return True 
        else:
            return False
        
def cherche_mvt(m):
    tmvt = []
    for t in range(NTUBES) :
        # ne pas toucher les tubes vides ou 
        #  les couleurs pleines uniformes
        if len(m[t]) == 0:
            #print('tube vide, on passe ',t)
            pass
        else :
            color = m[t][len(m[t]) - 1]
            ref = LTUBES * [m[t][len(m[t]) - 1]]
            if m[t] == ref:
                pass   # le tube est plein et uniforme, on n'y touche pas  
            else:
            # on cherche un tube avec cette couleur et place libre
                for u in range(NTUBES) :
                    if u==t:
                        pass
                    # si le tube est plein
                    elif  len(m[u]) == LTUBES:
                        pass
                    elif (len(m[u]) == 0) and test_uniform(m,t):
                        # on ne déplace pas 1 tube t uniforme  vers un tube vide
                        pass
                    elif (len(m[u])==0) or ((len(m[u]) < LTUBES) & ( m[u][len(m[u])-1] == color)):
                        # nombre de répétition de la couleur dans t
                        k= 1
                        while m[t][len(m[t])-1 -k] == color:
                            if len(m[t])-1 -k >=0:
                                k+=1
                            else:
                                break
                        place_libreu = LTUBES-len(m[u])
                        if k > place_libreu:
                            k= place_libreu
                        mvt=(t,u,k)
                        tmvt.append(mvt)              
    return tmvt


def m_properties(m):
    # nombre de tubes, taille des tubes 
    properties = []
    properties.append(len(m))
    lt = 0
    for l in m:
        taille = len(l)
        if taille > lt:
            lt = taille
    properties.append(lt)
    return(properties)

def colors_init(m):
    # matrice tubes couleur uniforme ou vide
    colors= []
    msolution = []
    for i in range(NTUBES):
        if len(m[i]) != 0:
            for j in range(len(m[i])):
                #print('couleurs ', colors)
                #print(m[i][j])
                if m[i][j] not in colors:
                    colors.append(m[i][j])
    for c in range(len(colors)): 
        ctube= LTUBES * [colors[c]]    
        msolution.append(ctube) 
    for i in range(NTUBES - len(colors)) :
        msolution.append([])        
    return msolution

def read_init(f):
    with open(f,'r') as f:
        tlist= []
        while True:
            ligne = f.readline()
            if not ligne:
                return tlist
            liste = ligne.split()
            tlist.append(liste)

def start():
    global MSOLUTION
    global NTUBES
    global LTUBES
    M = read_init('game_init.txt')
    for l in M:
        if l[0] == '0':
            l.pop()
    NTUBES, LTUBES = m_properties(M)
    MSOLUTION = colors_init(M)
    return M

def read_init(f):
    with open(f,'r') as f:
        tlist= []
        while True:
            ligne = f.readline()
            if not ligne:
                return tlist
            liste = ligne.split()
            tlist.append(liste)

# ******************************************************** 
Minit = start()
print('jeu initial ', Minit)
print('Solution ',MSOLUTION)
print('***********************************************')
print('NTUBES  ',NTUBES, ' LTUBES ', LTUBES)


Jeu(Minit)
print('SOLUTION', SOLUTION )
LMVT = SOLUTION  #
M = Minit 
print(SOLUTION)
App()           

