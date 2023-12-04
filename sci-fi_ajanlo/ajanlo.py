import json
import random
import os

class Ajanlo:
    
    def __init__(self, műfaj, útvonal):
        self.műfaj = műfaj
        self.útvonal = útvonal

    def üdvözlés(self):
        üdvözlő_szöveg = f"""
Ma felvirradt a szerencsenapod. Úgy hírlik, hogy {self.műfaj} regényt keresel.
Már feketeöves rajongó vagy vagy csak most ismerkedsz vele?
Mindegy is, csapjunk bele!
"""
        return print(üdvözlő_szöveg)
    
    def alműfaj_nyomtató(self):
        alműfajok = []
        with open(self.útvonal, "r") as file:
            db = json.load(file)

        for key, value in db.items():
            alműfajok.append(key)
        
        return alműfajok

    def alműfaj_választó(self):
        választott_alműfaj = input("Melyik alműfajból választasz? ")
        return választott_alműfaj

    def véletlen_szám_sorsoló(self, alműfaj):
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            random_könyv_sorszám = random.randint(0, (len(db[alműfaj]) - 1))
            return random_könyv_sorszám

    def műfaj_véletlen_könyve(self, alműfaj, sorszám):
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            könyv = db[alműfaj][sorszám]["cím"]
            return könyv

    def könyv_feljegyzése(self, alműfaj, sorszám):
         with open(self.útvonal, "r") as file:
            db = json.load(file)
            with open("ajanlas.txt", "w") as ajánlás:
                ajánlás.write(db[alműfaj][sorszám]["cím"])
                ajánlás.write(db[alműfaj][sorszám]["szerző"])
                ajánlás.write(str(db[alműfaj][sorszám]["sorozat része"]))
                ajánlás.write(str(db[alműfaj][sorszám]["film adaptáció"]))

    def ajánlás_hely_kiíró(self):
        hely = os.getcwd()
        hely_string = f"Az ajánlást részletesen lementettem az alábbi helyre: \
            {hely}/ajanlas.txt"
        return hely_string
        


