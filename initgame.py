import tkinter as tk
from tkinter import ttk, Canvas

ALL_COLORS = ['red', 'blue', 'yellow', 'azure', 'green', 'purple',
               'orange', 'cyan','magenta4','green4','brown', 'chartreuse2','deeppink2','firebrick1','black']
NTUBES=0
LTUBES=0
M = []


EXTERNAL_OFFSET = 30
OFFSET_X = 20
OFFSET_Y = 20
DIAMETER = 20
SMALL_DIAMETER = 10
colors=ALL_COLORS
band_width = OFFSET_X + DIAMETER

class App(tk.Tk):                # définit la fenêtre self=window=tk.Tk
    def __init__(self ):        # on transmet le jeu et la liste des mouvements
        super().__init__()
        # transmission du jeu
        
        # ************ affichage fenêtre globale
        self.title('Choix des couleurs, 14 couleurs possibles, 16 tubes maximum, noir pour vide')
        self.resizable(True, True)
        self.minsize(800,800)
        n_colors= len(ALL_COLORS)
        self.color_cv =Canvas(background="wheat")
        self.color_cv.place(x=0,y=0,relwidth=0.1,relheight=1)
        self.color_cv.create_rectangle(EXTERNAL_OFFSET, EXTERNAL_OFFSET,
                                      EXTERNAL_OFFSET + OFFSET_X + band_width,
                                      EXTERNAL_OFFSET + OFFSET_Y + n_colors * (DIAMETER +OFFSET_Y),
                                      fill="white")
        offsets = (EXTERNAL_OFFSET +OFFSET_X, EXTERNAL_OFFSET + OFFSET_Y,
                   EXTERNAL_OFFSET + OFFSET_X + DIAMETER,
                   EXTERNAL_OFFSET + OFFSET_Y + DIAMETER)
        for color in colors:
            self.color_cv.create_oval(*offsets, fill=color, tags=color + '_choice')
            offsets = (offsets[0], offsets[1] + OFFSET_Y + DIAMETER,
                       offsets[2], offsets[3] + OFFSET_Y + DIAMETER)
            
        label_frame = tk.LabelFrame(self, text='tubes' )
        for i in range(NTUBES):
            label = tk.Label(label_frame, text=str(i),fg='black',bg='white')
            label.place(x=500,y=30 +i*40)
           
        #self.main_cv.create_window(600, 600, window=label_frame, anchor='w') 

        # ************* ce qu'on peut placer dans la fenêtre : les widgets : 
        
        
         # boucle du jeu
        self.mainloop()
        

    

    def trace_oval(self, i,posi,colorm) : 
        self.main_cv.create_oval( OFFSET_X + posi * ( OFFSET_X+DIAMETER),
                       EXTERNAL_OFFSET+OFFSET_Y +(i)*( OFFSET_Y+ DIAMETER),
                       OFFSET_X + posi *  (OFFSET_X+DIAMETER) +DIAMETER,
                       EXTERNAL_OFFSET+OFFSET_Y +(i)* (OFFSET_Y+DIAMETER)+DIAMETER , fill=colorm)  
                  
NTUBES= int(input('Nombre total de tubes :'))
NVIDES = int(input('Dont vides :'))
LTUBES = int(input('Nombre de billes possibles par tube :'))
Fichout = input('Nom du fichier texte de sortie :')
App()

    
       