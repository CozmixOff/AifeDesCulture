import tkinter as tk


with open("AifeDesCulture - Questions/questions.txt", "r", encoding="utf-8") as fichier:
        data=fichier.read().split('\n')
        questions = int((len(data)-1)/8)
        avdiff = 0
        if questions > 0:
            for i in range (questions):
                avdiff += (int(data[i*8+6]))
            avdiff /= questions
            avdiff = round(avdiff, 2)
        
        geonum = 0
        histnum = 0
        scinum = 0
        litnum = 0
        jvdnum = 0
        musnum = 0
        artnum = 0
        cinnum = 0
        divnum = 0
        geodiff = 0
        histdiff = 0
        scidiff = 0
        litdiff = 0
        jvddiff = 0
        musdiff = 0
        artdiff = 0
        cindiff = 0
        divdiff = 0

        for i in range (questions):
            cate = data[i*8+5]
            if cate == "G":
                geonum += 1
                geodiff += int(data[i*8+6])
            elif cate == "H":
                histnum += 1
                histdiff += int(data[i*8+6])
            elif cate == "S":
                scinum += 1
                scidiff += int(data[i*8+6])
            elif cate == "L":
                litnum += 1
                litdiff += int(data[i*8+6])
            elif cate == "J":
                jvdnum += 1
                jvddiff += int(data[i*9+6])
            elif cate == "M":
                musnum += 1
                musdiff += int(data[i*8+6])
            elif cate == "A":
                artnum += 1
                artdiff += int(data[i*8+6])
            elif cate == "C":
                cinnum += 1
                cindiff += int(data[i*8+6])
            elif cate == "D":
                divnum += 1
                divdiff += int(data[i*8+6])
            else:
                pass

        if geonum > 0:
            geodiff /= geonum
            geodiff = round(geodiff,2)
        if histnum > 0:
            histdiff /= histnum
            histdiff = round(histdiff,2)
        if scinum > 0:
            scidiff /= scinum
            scidiff = round(scidiff,2)
        if litnum > 0:
            litdiff /= litnum
            litdiff = round(litdiff,2)
        if jvdnum > 0:
            jvddiff /= jvdnum
            jvddiff = round(jvddiff,2)
        if musnum > 0:
            musdiff /= musnum
            musdiff = round(musdiff,2)
        if artnum > 0:
            artdiff /= artnum
            artdiff = round(artdiff,2)
        if cinnum > 0:
            cindiff /= cinnum
            cindiff = round(cindiff,2)
        if divnum > 0:
            divdiff /= divnum
            divdiff = round(divdiff,2)

def add_question(questions):
    question = question_entree.get()
    reponse = reponse_entree.get()
    theme = themes_dict[theme_menu_var.get()]
    difficulte = difficulte_scale.get()
    mauvaises_reponses = [mauvaise_reponse1_entree.get(), mauvaise_reponse2_entree.get(), mauvaise_reponse3_entree.get()]
    
    if question == '' or reponse == '':
        error_label = tk.Label(fenetre, text="Erreur, veuillez remplir tous les champs nécessaires", fg="red")
        error_label.grid(row=14, column=1)
        fenetre.after(2000, error_label.destroy)
        return

    with open("AifeDesCulture - Questions/questions.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"{question}\n{reponse}\n")
        for mauvaise_reponse in mauvaises_reponses:
            fichier.write(f"{mauvaise_reponse}\n")
        fichier.write(f"{theme}\n{difficulte}\n")
        fichier.write("------------------------------\n")
    espace.grid(row=13, column=0)
    succes_label = tk.Label(fenetre, text="La question a été ajoutée avec succès !", fg="dark green")
    with open("AifeDesCulture - Questions/questions.txt", "r", encoding="utf-8") as fichier:
        data=fichier.read().split('\n')
        questions = int((len(data)-1)/8)
    stats_label.config(text='Nombre de questions : '+str(questions))
    succes_label.grid(row=14, column=1)
    with open("AifeDesCulture - Questions/questions.txt", "r", encoding="utf-8") as fichier:
        avdiff = 0
        for i in range (questions):
            avdiff += (int(data[i*8+6]))
        avdiff /= questions
        avdiff = round(avdiff, 2)
    avdiff_label.config(text = 'Difficulté moyenne des questions : '+ str(avdiff))
    geonum = 0
    with open("AifeDesCulture - Questions/questions.txt", "r", encoding="utf-8") as fichier:
        histnum = 0
        scinum = 0
        litnum = 0
        jvdnum = 0
        musnum = 0
        artnum = 0
        cinnum = 0
        divnum = 0
        geodiff = 0
        histdiff = 0
        scidiff = 0
        litdiff = 0
        jvddiff = 0
        musdiff = 0
        artdiff = 0
        cindiff = 0
        divdiff = 0

        for i in range (questions):
            cate = data[i*8+5]
            if cate == "G":
                geonum += 1
                geodiff += int(data[i*8+6])
            elif cate == "H":
                histnum += 1
                histdiff += int(data[i*8+6])
            elif cate == "S":
                scinum += 1
                scidiff += int(data[i*8+6])
            elif cate == "L":
                litnum += 1
                litdiff += int(data[i*8+6])
            elif cate == "J":
                jvdnum += 1
                jvddiff += int(data[i*9+6])
            elif cate == "M":
                musnum += 1
                musdiff += int(data[i*8+6])
            elif cate == "A":
                artnum += 1
                artdiff += int(data[i*8+6])
            elif cate == "C":
                cinnum += 1
                cindiff += int(data[i*8+6])
            elif cate == "D":
                divnum += 1
                divdiff += int(data[i*8+6])
            else:
                pass

        if geonum > 0:
            geodiff /= geonum
            geodiff = round(geodiff,2)
        if histnum > 0:
            histdiff /= histnum
            histdiff = round(histdiff,2)
        if scinum > 0:
            scidiff /= scinum
            scidiff = round(scidiff,2)
        if litnum > 0:
            litdiff /= litnum
            litdiff = round(litdiff,2)
        if jvdnum > 0:
            jvddiff /= jvdnum
            jvddiff = round(jvddiff,2)
        if musnum > 0:
            musdiff /= musnum
            musdiff = round(musdiff,2)
        if artnum > 0:
            artdiff /= artnum
            artdiff = round(artdiff,2)
        if cinnum > 0:
            cindiff /= cinnum
            cindiff = round(cindiff,2)
        if divnum > 0:
            divdiff /= divnum
            divdiff = round(divdiff,2)
    geonum_label.config(text='Nombre de questions : '+str(geonum))
    histnum_label.config(text='Nombre de questions : '+str(histnum))
    scinum_label.config(text='Nombre de questions : '+str(scinum))
    litnum_label.config(text='Nombre de questions : '+str(litnum))
    jvdnum_label.config(text='Nombre de questions : '+str(jvdnum))
    musnum_label.config(text='Nombre de questions : '+str(musnum))
    artnum_label.config(text='Nombre de questions : '+str(artnum))
    cinnum_label.config(text='Nombre de questions : '+str(cinnum))
    divnum_label.config(text='Nombre de questions : '+str(divnum))
    geodiff_label.config(text='Difficulté moyenne des questions : '+str(geodiff))
    histdiff_label.config(text='Difficulté moyenne des questions : '+str(histdiff))
    scidiff_label.config(text='Difficulté moyenne des questions : '+str(scidiff))
    litdiff_label.config(text='Difficulté moyenne des questions : '+str(litdiff))
    jvddiff_label.config(text='Difficulté moyenne des questions : '+str(jvddiff))
    musdiff_label.config(text='Difficulté moyenne des questions : '+str(musdiff))
    artdiff_label.config(text='Difficulté moyenne des questions : '+str(artdiff))
    cindiff_label.config(text='Difficulté moyenne des questions : '+str(cindiff))
    divdiff_label.config(text='Difficulté moyenne des questions : '+str(divdiff))

    fenetre.after(2000, succes_label.destroy)

def reset_inputs():
    question_entree.delete(0, tk.END)
    reponse_entree.delete(0, tk.END)
    mauvaise_reponse1_entree.delete(0, tk.END)
    mauvaise_reponse2_entree.delete(0, tk.END)
    mauvaise_reponse3_entree.delete(0, tk.END)
    theme_menu_var.set("--Choisir le thème--")
    difficulte_scale.set(1)
    
fenetre = tk.Tk()
fenetre.geometry("450x350")
fenetre.resizable(False, False)
fenetre.title("AifeDesCultures - Ajouter une question")

question_label = tk.Label(fenetre, text="Question :")
question_label.grid(row=0, column=0, sticky="W")
question_entree = tk.Entry(fenetre, width=50)
question_entree.grid(row=0, column=1)

espace = tk.Label(fenetre, text="")
espace.grid(row=1, column=0, sticky="W")

reponse_label = tk.Label(fenetre, text="Réponse :")
reponse_label.grid(row=2, column=0, sticky="W")
reponse_entree = tk.Entry(fenetre, width=50)
reponse_entree.grid(row=2, column=1)

espace = tk.Label(fenetre, text="")
espace.grid(row=3, column=0, sticky="W")

mauvaise_reponse1_label = tk.Label(fenetre, text="Mauvaises réponses :")
mauvaise_reponse1_label.grid(row=4, column=0, sticky="W")
mauvaise_reponse1_entree = tk.Entry(fenetre, width=50)
mauvaise_reponse1_entree.grid(row=4, column=1)

mauvaise_reponse2_entree = tk.Entry(fenetre, width=50)
mauvaise_reponse2_entree.grid(row=5, column=1)

mauvaise_reponse3_entree = tk.Entry(fenetre, width=50)
mauvaise_reponse3_entree.grid(row=6, column=1)

espace = tk.Label(fenetre, text="")
espace.grid(row=7, column=0, sticky="W")

theme_label = tk.Label(fenetre, text="Thème :")
theme_label.grid(row=8, column=0, sticky="W")
theme_options = ["Géographie", "Histoire", "Sciences", "Littérature", "Jeux Vidéos", "Musique", "Art", "Cinéma", "Divers"]
theme_menu_var = tk.StringVar(value="--Choisir le thème--")
themes_dict = {
    "--Choisir le thème--":"",
    "Géographie":"G",
    "Histoire":"H",
    "Sciences":"S",
    "Littérature":"L",
    "Jeux Vidéos":"J",
    "Musique":"M",
    "Art":"A",
    "Cinéma":"C",
    "Divers":"D"
}
theme_menu = tk.OptionMenu(fenetre, theme_menu_var, *theme_options)
theme_menu.grid(row=8, column=1)

espace = tk.Label(fenetre, text="")
espace.grid(row=9, column=0, sticky="W")

difficulte_label = tk.Label(fenetre, text="Difficulté :")
difficulte_label.grid(row=10, column=0, sticky="W")
difficulte_scale = tk.Scale(fenetre, from_=1, to=5, orient="horizontal")
difficulte_scale.grid(row=10, column = 1)

espace = tk.Label(fenetre, text="")
espace.grid(row=11, column=0, sticky="W")

ajouter_question_button = tk.Button(fenetre, text="Ajouter la question", command=lambda: [add_question(questions), reset_inputs()])
ajouter_question_button.grid(row=12, column=1)

espace = tk.Label(fenetre, text="")
espace.grid(row=15, column=0, sticky="W")

#------------------------------------------------

stats = tk.Tk()
stats.geometry("300x850")
stats.resizable(False, False)
stats.title("AifeDesCultures - Statistiques")

stats_label = tk.Label(stats, text='Nombre de questions : '+str(questions))
stats_label.grid(row = 0, column=0, sticky='W')
avdiff_label = tk.Label(stats, text = 'Difficulté moyenne des questions : '+str(avdiff))
avdiff_label.grid(row=1, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 2, column = 0)

geo_title = tk.Label(stats, text="Géographie :")
geo_title.config(font=(10))
geo_title.grid(row=3, column=0, sticky="W")

geonum_label = tk.Label(stats, text = "Nombre de questions : "+str(geonum))
geonum_label.grid(row=4, column=0, sticky="W")

geodiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(geodiff))
geodiff_label.grid(row = 5, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 6, column = 0)

hist_title = tk.Label(stats, text="Histoire :")
hist_title.config(font=(10))
hist_title.grid(row=7, column=0, sticky="W")

histnum_label = tk.Label(stats, text = "Nombre de questions : "+str(histnum))
histnum_label.grid(row=8, column=0, sticky="W")

histdiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(histdiff))
histdiff_label.grid(row = 9, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 10, column = 0)

sci_title = tk.Label(stats, text="Sciences :")
sci_title.config(font=(10))
sci_title.grid(row=11, column=0, sticky="W")

scinum_label = tk.Label(stats, text = "Nombre de questions : "+str(scinum))
scinum_label.grid(row=12, column=0, sticky="W")

scidiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(scidiff))
scidiff_label.grid(row = 13, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 14, column = 0)

lit_title = tk.Label(stats, text="Littérature :")
lit_title.config(font=(10))
lit_title.grid(row=15, column=0, sticky="W")

litnum_label = tk.Label(stats, text = "Nombre de questions : "+str(litnum))
litnum_label.grid(row=16, column=0, sticky="W")

litdiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(litdiff))
litdiff_label.grid(row = 17, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 18, column = 0)

jvd_title = tk.Label(stats, text="Jeux vidéos :")
jvd_title.config(font=(10))
jvd_title.grid(row=19, column=0, sticky="W")

jvdnum_label = tk.Label(stats, text = "Nombre de questions : "+str(jvdnum))
jvdnum_label.grid(row=20, column=0, sticky="W")

jvddiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(jvddiff))
jvddiff_label.grid(row = 21, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 22, column = 0)

mus_title = tk.Label(stats, text="Musique :")
mus_title.config(font=(10))
mus_title.grid(row=23, column=0, sticky="W")

musnum_label = tk.Label(stats, text = "Nombre de questions : "+str(musnum))
musnum_label.grid(row=24, column=0, sticky="W")

musdiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(musdiff))
musdiff_label.grid(row = 25, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 26, column = 0)

art_title = tk.Label(stats, text="Musique :")
art_title.config(font=(10))
art_title.grid(row=27, column=0, sticky="W")

artnum_label = tk.Label(stats, text = "Nombre de questions : "+str(artnum))
artnum_label.grid(row=28, column=0, sticky="W")

artdiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(artdiff))
artdiff_label.grid(row = 29, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 30, column = 0)

cin_title = tk.Label(stats, text="Cinéma :")
cin_title.config(font=(10))
cin_title.grid(row=31, column=0, sticky="W")

cinnum_label = tk.Label(stats, text = "Nombre de questions : "+str(cinnum))
cinnum_label.grid(row=32, column=0, sticky="W")

cindiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(cindiff))
cindiff_label.grid(row = 33, column=0, sticky="W")

stats_space = tk.Label(stats, text = "")
stats_space.grid(row = 34, column = 0)

div_title = tk.Label(stats, text="Divers :")
div_title.config(font=(10))
div_title.grid(row=35, column=0, sticky="W")

divnum_label = tk.Label(stats, text = "Nombre de questions : "+str(divnum))
divnum_label.grid(row=36, column=0, sticky="W")

divdiff_label = tk.Label(stats, text="Difficulté moyenne des questions : "+str(divdiff))
divdiff_label.grid(row = 37, column=0, sticky="W")

fenetre.mainloop()