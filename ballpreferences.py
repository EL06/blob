from tkinter import Button, IntVar, Label, Radiobutton, Spinbox, Toplevel, Entry



ALL_COLORS = ['black','red', 'blue', 'yellow', 'azure', 'green', 'purple',
               'orange', 'cyan','magenta4','green4','brown', 'chartreuse2','deeppink2','firebrick1','black']
NTUBES=3
LTUBES=4
NVIDES = 1

FICHOUT = 'test.txt'


SETTINGS = {
    'n_colors': len(ALL_COLORS),
    'n_tries': NTUBES,
    'code_size': LTUBES ,
    'fich_out': FICHOUT,
    'nvides': NVIDES
}


class SettingsWindow(Toplevel):

    def __init__(self, game_area):
        super().__init__()
        self.bg_color = 'wheat'
        self.config(bg=self.bg_color)
        self.title("Préférences")
        self.resizable(False, False)
        self.game_area = game_area

        paddings = {'padx': (12, 12), 'pady': (12, 12)}

        Label(self, text="Nombre total de tubes :", bg=self.bg_color) \
            .grid(row=0, column=0, columnspan=2, sticky='nws', **paddings)
        self.n_tubes_box = Spinbox(self, from_=2, to=15)
        self.n_tubes_box.grid(row=0, column=2, columnspan=2, sticky='nes', **paddings)

        Label(self, text="Dont vides pour finir :", bg=self.bg_color) \
            .grid(row=1, column=0, sticky='nws', **paddings)
        self.nvides = Entry(self)
        self.nvides.grid(row=1, column=2, columnspan=2, sticky='nes', **paddings)
        

        Label(self, text="Taille maximale des tubes en nombre de balles :", bg=self.bg_color) \
            .grid(row=2, column=0, columnspan=2, sticky='nws', **paddings)
        self.tube_size_var  =Entry(self)
        self.tube_size_var.grid(row=2, column=2, columnspan=2, sticky='nes', **paddings)
        
        Label(self, text="Nom du fichier de sortie :", bg=self.bg_color) \
            .grid(row=3, column=0, columnspan=2, sticky='nws', **paddings)
        self.fichout_var  =Entry(self)
        self.fichout_var.grid(row=3, column=2, columnspan=2, sticky='nes', **paddings)

        Button(self, text="Annuler", command=self.destroy, bg=self.bg_color) \
            .grid(row=4, column=0, columnspan=2, sticky='nesw', **paddings)
        Button(self, text="Appliquer", command=self.apply, bg=self.bg_color) \
            .grid(row=4, column=2, columnspan=2, sticky='nesw', **paddings)

        self.bind("<Escape>", lambda _event: self.destroy())

    def apply(self):
        global SETTINGS
        
        SETTINGS['n_tries'] = int(self.n_tubes_box.get())
        SETTINGS['code_size'] = int(self.tube_size_var.get())
        SETTINGS['nvides'] = int(self.nvides.get())
        SETTINGS['fichout'] = self.fichout_var.get()
        print("Settings dans préférences", SETTINGS)
        
        self.game_area.new_game()
        self.destroy()