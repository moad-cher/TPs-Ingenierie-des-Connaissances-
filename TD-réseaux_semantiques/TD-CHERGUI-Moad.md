# TD

## <u>Exercice 1 :</u>

- Un oiseau est un animal qui peut voler.
- Un mammifère est un animal qui allaite ses petits.
- Une chauve-souris est à la fois un mammifère et un oiseau.
- Les chauves-souris ne pondent pas d’œufs.

1. réseau sémantique
    ```mermaid
    graph
        Animal((Animal))
        Oiseau((Oiseau))
        Mammifere((Mammifère))
        ChauveSouris((Chauve-souris))
        Oeufs((Œufs))
        Voler((Voler))
        Allaiter((Allaite <br>ses petits))

        Oiseau -->|est un| Animal
        Oiseau -->|peut| Voler
        Mammifere -->|est un| Animal
        Mammifere -->|allaite| Allaiter
        ChauveSouris -->|est un| Mammifere
        ChauveSouris -->|est un| Oiseau
        ChauveSouris -->|ne pond pas| Oeufs
        ChauveSouris -->|peut| Voler
    ```

2. Les propriétés que la chauve-souris hérite:
    - De **Mammifère** : allaite ses petits
    - De **Oiseau** : peut voler

3. Conflits identifiés :
    - Un oiseau pond des oeufs, mais la chauve-souris ne pond pas d'Oeufs
    - Un oiseau n'allaite pas ses petits, mais la chauve-souris (mammifère) allaite ses petits
    - $\implies$ Contradiction : la chauve-souris ne peut pas être à la fois un oiseau et un mammifère selon les définitions classiques


## <u>Exercice 2 :</u>
- Tous les poissons vivent dans l’eau.
- Tous les animaux qui vivent dans l’eau peuvent nager.
- Les dauphins sont des mammifères.
- Les mammifères sont des animaux.
- Les dauphins vivent dans l’eau.

####  réseau sémantique
```mermaid
graph
    Animal((Animal))
    Poisson((Poisson))
    Mammifere((Mammifère))
    Dauphin((Dauphin))
    Eau((Eau))
    Nager((Nager))

    Poisson -->|vit dans| Eau
    Mammifere -->|est un| Animal
    Dauphin -->|est un| Mammifere
    Dauphin -->|vit dans| Eau
    Eau -->|permet de| Nager
```

## <u>Exercice 3 :</u>
- Une personne possède un âge (valeur numérique).
- Un étudiant est une personne qui étudie un domaine.
- Un enseignant est une personne qui enseigne un domaine.
- Un professeur est à la fois enseignant et chercheur.
- Le domaine enseigné doit être le même que le domaine étudié pour un même cours.

#### réseau sémantique
```mermaid
graph
    Personne((Personne))
    Etudiant((Étudiant))
    Enseignant((Enseignant))
    Chercheur((Chercheur))
    Professeur((Professeur))
    Age((Âge))
    Domaine((Domaine))
    Cours((Cours))

    Personne -->|possède| Age
    Etudiant -->|est une| Personne
    Etudiant -->|étudie| Domaine
    Enseignant -->|est une| Personne
    Enseignant -->|enseigne| Domaine
    Chercheur -->|est une| Personne
    Professeur -->|est un| Enseignant
    Professeur -->|est un| Chercheur
    Cours -->|requiert| Domaine
    Domaine -->|même pour| Cours
```

## <u>Exercice 4 :</u>
- Chien → est un → Animal
- Chat → est un → Animal
- Animal → est un → ÊtreVivant
- Chien → lié À → Os
- Chat → lié À → Lait
- Os → type → Nourriture

```mermaid
graph
    chien((Chien))
    chat((Chat))
    animal((Animal))
    etre((ÊtreVivant))

    chien --est un--> animal
    chat --est un--> animal
    animal --est un--> etre
    chien --lié à--> os((Os))
    chat --lié à--> lait((Lait))
    os --est sort de--> n((Nouriture))