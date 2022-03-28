from tkinter import *

class Beer:
    def __init__(self):
        pass

    def inicia(self):
        self.janela_beer = Toplevel()
        self.janela_beer.geometry('1440x768+0+0')
        self.janela_beer.resizable(width=False, height=False)
        self.janela_beer.title('Beer')
        self.janela_beer.configure(bg='gray20')
        self.voltar = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/voltar.png')
        self.tablet_image = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/Tablet.png')
        self.beers = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer1.png')

        self.fundo = Label(self.janela_beer, image=self.tablet_image, borderwidth=0, bg='gray20')
        self.fundo.place(x=110, y=10)

        self.volta_incio = Button(self.janela_beer,command=self.janela_beer.destroy, image=self.voltar, bg='gray20', borderwidth=0, activebackground='gray20')
        self.volta_incio.place(x=150, y=45)

        self.title = Label(self.janela_beer, text='B E E R S   ON   T A P', font=('Curlz MT', 20), bg='gray20', fg='yellow', borderwidth=1)
        self.title.place(x=600, y=50)

        self.escolhe1 = Button(self.janela_beer, text='MAALI THINGS SEEM', command=self.troca_beer1, font=('Calibri', 12), bg='gray20', fg='white', borderwidth=0, activebackground='yellow')
        self.escolhe1.place(x=230, y=100)

        self.escolhe2 = Button(self.janela_beer, text='IGNORUS MUTUM', command=self.troca_beer2, font=('Calibri', 12), bg='gray20', fg='white', borderwidth=0, activebackground='yellow')
        self.escolhe2.place(x=430, y=100)

        self.escolhe3 = Button(self.janela_beer, text='BUDDY BREWERY KHARMA',command=self.troca_beer3, font=('Calibri', 12), bg='gray20', fg='white', borderwidth=0, activebackground='yellow')
        self.escolhe3.place(x=630, y=100)

        self.escolhe4 = Button(self.janela_beer, text='MASMORRA MALIGNA', command=self.troca_beer4, font=('Calibri', 12),bg='gray20', fg='white', borderwidth=0, activebackground='yellow')
        self.escolhe4.place(x=900, y=100)

        self.escolhe5 = Button(self.janela_beer, text='IGNORUS BERUS', command=self.troca_beer5, font=('Calibri', 12), bg='gray20', fg='white', borderwidth=0, activebackground='yellow')
        self.escolhe5.place(x=1130, y=100)

        self.beer1 = Label(self.janela_beer, image=self.beers, bg='black', borderwidth=0)
        self.beer1.place(x=300, y=200)

        self.info_name = Label(self.janela_beer, text='MAALI  THINGS  SEEM', font=('Calibri', 16), bg='gray20', fg='yellow')
        self.info_name.place(x=1030, y=290)

        self.info1 = Label(self.janela_beer, text='Desenvolvida exatamente como a sua versão \n'
                                                 '“Loira” com exceção da aplicação de uma calda \n'
                                                 'feita a partir de malte alemão escuro. \n'
                                                 'Graças e essa técnica o malte escuro não traz amargor \n'
                                                 'ou adstringência somente uma leve nota de cacau e café \n'
                                                 'que deixam esse cerveja ainda mais incrível.', font=('Calibri', 12), bg='gray20', fg='white')
        self.info1.place(x=945, y=350)


        self.changeOnHover(self.escolhe1, 'purple', 'gray20')
        self.changeOnHover(self.escolhe2, 'purple', 'gray20')
        self.changeOnHover(self.escolhe3, 'purple', 'gray20')
        self.changeOnHover(self.escolhe4, 'purple', 'gray20')
        self.changeOnHover(self.escolhe5, 'purple', 'gray20')

        self.janela_beer.mainloop()


    def voltando(self):
        self.janela_beer.destroy()


    def changeOnHover(self, button, colorOnHover, colorOnLeave):

        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))


    def troca_beer2(self):
        self.beers['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer2.png'
        self.info_name['text'] = 'IGNORUS MUTUM'
        self.beer1.place(x=300, y=200)
        self.info1['text'] = 'Com uma base de maltes consistente e uma enorme\n' \
                             'carga de lúpulos norte-americanos, \n' \
                            'é a cerveja ideal para lupulomaníacos. \n' \
                             'Possui aromas intensos remetendo a\n' \
                            'frutas  cítricas como abacaxi, limão e maracujá, \n' \
                             'tem final amargo, potente, longo e seco, \n' \
                            'como uma IPA de respeito deve ter.'
        self.info_name.place(x=1040, y=290)
        self.info1.place(x=945, y=350)

    def troca_beer1(self):
        self.beers['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer1.png'
        self.info_name['text'] = 'MAALI  THINGS  SEEM'
        self.info1['text'] = 'Desenvolvida exatamente como a sua versão \n' \
                             '“Loira” com exceção da aplicação de uma calda \n' \
                             'feita a partir de malte alemão escuro. \n' \
                             'Graças e essa técnica o malte escuro não traz amargor \n' \
                             'ou adstringência somente uma leve nota de cacau e café \n' \
                             'que deixam esse cerveja ainda mais incrível.'

    def troca_beer3(self):
        self.beers['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer3.png'
        self.beer1.place(x=300, y=200)
        self.info_name['text'] = 'BUDDY BREWERY KHARMA'
        self.info1['text'] = 'KHARMA, a lei de conservação da força, mostra a importância\n'\
                             'de desenvolver ações equilibradas e sentimentos positivos!\n' \
                             'Esse é o ideal que nos guia! A Buddy apresenta a vocês\n' \
                             'sua American Ipa, que traz no paladar só positividade\n' \
                             'e boas vibrações... \n' \
                             'Com os lúpulos Citra e Mosaic essa cerveja\n' \
                             'além de saborosa é deliciosamente aromática!'
        self.info_name.place(x=1000, y=290)
        self.info1.place(x=910, y=350)



    def troca_beer4(self):
        self.beers['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer4.png'
        self.beer1.place(x=300, y=200)
        self.info_name['text'] = 'MASMORRA MALIGNA'
        self.info1['text'] = 'A Maligna foi criada para agradar todos os paladares.\n' \
                             'Fácil de se beber. Cerveja de corpo leve, clara,\n' \
                             'amargor médio e aromas provenientes do lúpulo\n' \
                             'americano Mosaic. Mas não se engane, o teor\n' \
                             'alcoólico pode ser maligno.'
        self.info_name.place(x=1020, y=290)
        self.info1.place(x=945, y=350)

    def troca_beer5(self):
        self.beers['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/Loja/Imagem/beer5.png'
        self.beer1.place(x=300, y=200)
        self.info_name['text'] = 'IGNORUS BERUS'
        self.info1['text'] = 'O nome desta cerveja vem de Vipera berus, nome científico\n' \
                             ' de uma espécie de víbora alemã, homenageando a origem\n' \
                             ' e "mordida" ácida das Berliner Weisse. Produzida com \n' \
                             'adição de pitaya e framboesas, que complementam a acidez\n' \
                             ' e paladar seco com leves sabores frutados.'
        self.info_name.place(x=1040, y=290)
        self.info1.place(x=920, y=350)

