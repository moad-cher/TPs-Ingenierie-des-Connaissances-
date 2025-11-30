
'''

#### Contexte :
On veut diagnostiquer un patient à partir des symptômes. On utilise un système expert basé sur des règles.

#### Base de faits initiale (symptômes connus)

- Fièvre
- Toux
- Fatigue
- Maux de gorge

#### Règles :
- R1 : Si fièvre Et toux → Infection respiratoire
- R2 : Si fièvre Et maux de gorge → Angine
- R3 : Si fatigue Et maux de gorge → Rhume
- R4 : Si infection respiratoire Et fatigue → Pneumonie

'''





# ---------------------------
# Mini-Système Expert Médical
# ---------------------------

# Faits initiaux
faits = ["fièvre", "toux", "maux de gorge", "fatigue"]

# Règles du système expert
regles = [
    {"conditions": ["fièvre", "toux"], "conclusion": "Infection respiratoire possible"},
    {"conditions": ["maux de gorge", "fièvre"], "conclusion": "Angine possible"},
    {"conditions": ["fatigue", "maux de gorge"], "conclusion": "Rhume possible"},
    {"conditions": ["Infection respiratoire possible", "fatigue"], "conclusion": "Pneumonie possible"},
]

# ---------------------------
# Fonction : Forward Chaining
# ---------------------------
def forward_chaining(faits, regles):
    faits = faits.copy()
    nouveau_fait = True
    print("=== Forward Chaining ===")
    while nouveau_fait:
        nouveau_fait = False
        for regle in regles:
            if all(c in faits for c in regle["conditions"]) and regle["conclusion"] not in faits:
                faits.append(regle["conclusion"])
                print(f"Règle appliquée : {regle['conditions']} -> {regle['conclusion']}")
                nouveau_fait = True
    print("\nFaits finaux :", faits)
    print("\n")
    return faits

# La règle ["fièvre", "toux"] -> "Infection respiratoire possible" s’applique.
# La règle ["maux de gorge", "fièvre"] -> "Angine possible" s’applique.
# La règle ["fatigue", "maux de gorge"] -> "Rhume possible" s’applique.
# Ensuite, comme "Infection respiratoire possible" et "fatigue" sont maintenant dans les faits, la règle ["Infection respiratoire possible", "fatigue"] -> "Pneumonie possible" s’applique.

# ---------------------------
# Fonction : Backward Chaining
# ---------------------------
def backward_chaining(objectif, faits, regles, chemin=None):
    if chemin is None:
        chemin = []
    # Objectif déjà dans les faits
    if objectif in faits:
        return True
    # Chercher règle qui produit l'objectif
    for regle in regles:
        if regle["conclusion"] == objectif:
            # Vérifier si toutes les conditions sont atteignables
            toutes_conditions_ok = True
            for cond in regle["conditions"]:
                if cond not in faits:
                    if not backward_chaining(cond, faits, regles, chemin):
                        toutes_conditions_ok = False
            if toutes_conditions_ok:
                faits.append(objectif)
                chemin.append(objectif)
                return True
    return False

# ---------------------------
# Exécution Forward Chaining
# ---------------------------
faits_finals = forward_chaining(faits, regles)

# ---------------------------
# Exécution Backward Chaining
# ---------------------------
objectif = "Pneumonie possible"
faits_bc = faits.copy()
resultat = backward_chaining(objectif, faits_bc, regles)
print("=== Backward Chaining ===")
if resultat:
    print(f"L'objectif '{objectif}' est atteint avec les faits : {faits_bc}")
else:
    print(f"L'objectif '{objectif}' n'est pas atteint avec les faits : {faits_bc}")

# ---------------------------
# Comparaison rapide
# ---------------------------
print("\n=== Comparaison ===")
print("Forward Chaining : dérive toutes les conclusions possibles à partir des faits connus.")
print("Backward Chaining : vérifie seulement si un objectif spécifique peut être atteint.")
