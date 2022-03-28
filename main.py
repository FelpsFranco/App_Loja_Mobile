from tkinter import *
from beer import Beer

class Cardabiu:
    def __init__(self):
        self.janela_inicial = Tk()
        self.janela_inicial.geometry('1440x768+0+0')
        self.janela_inicial.resizable(width=False, height=False)
        self.janela_inicial.title('Bem Vindo')
        self.janela_inicial.configure(bg='gray20')
        self.tablet_image = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/Tablet.png')
        self.logo = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/logo.png')
        self.alien_e = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/Aliente_direita.png')
        self.alien_d = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/Alien_esquerda.png')
        self.abaixo = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/Abaixo.png')
        self.ilustr = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/cerveja.png')

        self.tablet = Label(self.janela_inicial, image=self.tablet_image, borderwidth=0, bg='gray20')
        self.tablet.place(x=110, y=10)

        self.desenho = Label(self.janela_inicial, image=self.ilustr, borderwidth=0, bg='gray20')
        self.desenho.place(x=180, y=70)

        self.desenho1 = Label(self.janela_inicial, image=self.ilustr, borderwidth=0, bg='gray20')
        self.desenho1.place(x=1220, y=70)

        self.borda = Label(self.janela_inicial, image=self.alien_e, borderwidth=0)
        self.borda.place(x=1079, y=240)

        self.borda = Label(self.janela_inicial, image=self.alien_d, borderwidth=0)
        self.borda.place(x=134, y=240)

        self.beers = Button(self.janela_inicial, text='Beers', command=self.beer, font=("Dubai Medium", 12), fg='white', bg='gray20', borderwidth=0, activebackground='gray20')
        self.beers.place(x=290, y=100)

        self.food = Button(self.janela_inicial, text='Food', font=('Dubai Medium', 12), fg='white', bg='gray20', borderwidth=0, activebackground='gray20')
        self.food.place(x=410, y=100)

        self.events = Button(self.janela_inicial, text='Events', font=('Dubai Medium', 12), fg='white', bg='gray20',borderwidth=0, activebackground='gray20')
        self.events.place(x=530, y=100)

        self.logo_label = Label(self.janela_inicial, image=self.logo, borderwidth=0, bg='gray20')
        self.logo_label.place(x=660, y=60)

        self.about = Button(self.janela_inicial, text='About', font=('Dubai Medium', 12), fg='white', bg='gray20',borderwidth=0, activebackground='gray20')
        self.about.place(x=870, y=100)

        self.merch = Button(self.janela_inicial, text='Merch', font=('Dubai Medium', 12), fg='white', bg='gray20',borderwidth=0, activebackground='gray20')
        self.merch.place(x=990, y=100)

        self.contact = Button(self.janela_inicial, text='Contact', font=('Dubai Medium', 12), fg='white', bg='gray20',borderwidth=0, activebackground='gray20')
        self.contact.place(x=1110, y=100)

        self.text = Label(self.janela_inicial, text='T C H O L A '+' T A V E R N', font=('Monotype Corsiva', 18), fg='purple', bg='gray20')
        self.text.place(x=610, y=300)

        self.text1 = Label(self.janela_inicial, text='T h e   l a r g e s t   T c h o l a s   c o m p a n y   i n   t h e   w o r l d. \n'
                                                     'H e r e   y o u   w i l l   f i n d   a l l   k i n d s   o f   d r i n k s.', font=('Monotype Corsiva', 18),fg='white', bg='gray20')
        self.text1.place(x=460, y=420)

        self.abaixo1 = Label(self.janela_inicial, image=self.abaixo, borderwidth=0, bg='gray20')
        self.abaixo1.place(x=710, y=620)
        self.abaixo2 = Label(self.janela_inicial, image=self.abaixo, borderwidth=0, bg='gray20')
        self.abaixo2.place(x=710, y=650)

        self.changeOnHover(self.beers, 'purple', 'gray20')
        self.changeOnHover(self.food, 'purple', 'gray20')
        self.changeOnHover(self.events, 'purple', 'gray20')
        self.changeOnHover(self.about, 'purple', 'gray20')
        self.changeOnHover(self.merch, 'purple', 'gray20')
        self.changeOnHover(self.contact, 'purple', 'gray20')

        self.janela_inicial.mainloop()


    def changeOnHover(self, button, colorOnHover, colorOnLeave):

        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def beer(self):
        beer_windows = Beer()
        beer_windows.inicia()


Cardabiu()
