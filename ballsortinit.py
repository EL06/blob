from tkinter import Tk
from tkinter import BOTH, N, S, X
from tkinter import Label, Menu
from tkinter.ttk import Button
from tkinter.messagebox import showinfo
from multiprocessing import freeze_support
from ballarea import GameArea
from ballpreferences import SettingsWindow


def about():
    """
    Display an informative window.
    """
    showinfo('À propos',
             message="Bienvenue dans cet outil  avec Tkinter.\n\n"
                     "Ce jeu consiste à composer des tubes de balles "
                     "de couleurs mélangées. Le but est de déplacer ces balles de tubes en tubes pour regrouper les couleurs\n\n"
                     "Vous pouvez configurer le nombre de tubes, la taille maximale des tubes "
                     "et  le  fichier de sauvegarde  dans le menu Préférences est test.txt."
            )

# Instantiate the global window:
freeze_support()
root = Tk()
root.title('Ballsort')
root.resizable(True, True)


# Create canvas in which to draw the pickable pegs, the playing field and the guess results:
Label(root,
      text='[F1] À propos - [F2] Préférences - [F5] Nouvelle partie - [ESC] Quitter',
      foreground="white",
      background="blue").pack(anchor=N, fill=X)


# Create the game area:
game_area = GameArea(text="Aire de jeu")
game_area.pack(anchor=N, expand=True, fill=BOTH)


# Create and populate the main menu:
root_menu = Menu(root)
root['menu'] = root_menu
main_cascade = Menu(root_menu)
root_menu.add_cascade(label='Ball Sort', menu=main_cascade)
main_cascade.add_command(label='Préférences', command=lambda: SettingsWindow(game_area))
main_cascade.add_separator()
main_cascade.add_command(label='À propos', command=about)


# Menu shortcuts:
root.bind("<F1>", lambda _event: about())
root.bind("<F2>", lambda _event: SettingsWindow(game_area))


# Add a last button for quitting the game:
Button(text='Quitter [ESC]', command=root.destroy).pack(anchor=S, fill=X)
root.bind('<Escape>', lambda _event: root.destroy())


# Launch the main loop that catches all user interactions:
root.mainloop()
