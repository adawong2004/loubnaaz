class voiture :
     def __init__(self, p_couleur, p_marque, p_vitesse = 0): 
        
        self.couleur= p_couleur
        self.marque= p_marque
        self.vitesse= p_vitesse

        def accelerer(self, p_vitesse):
            p_vitesse += p_vitesse

            def frainer (self, p_vitesse):
                self.vitesse -= p_vitesse
                if self.vitesse > 0:
                    self.vitesse =  0

            

voiture_bleu = voiture('bleu', 'Peugeaot', 20)
voiture_rouge = voiture('rouge', 'BMW', 18)


print(voiture_bleu.couleur)
print(voiture_bleu.marque)
print(voiture_bleu.vitesse)
print('-'*8)
print(voiture_rouge.couleur)
print(voiture_rouge.marque)
print(voiture_rouge.vitesse)
print('-'*8)
print(voiture_bleu.vitesse)
print(voiture_bleu.vitesse)
print(voiture_bleu.vitesse)
print(voiture_bleu.vitesse)
