<style>
h1{
    font-weight:bold;
    font-family:"lucida handwriting"
}
h2{
    text-decoration:underline;
}
p{display:inline}
</style>

<center>

# TD:<br>les réseaux sémantiques
</center>

## Exercice 1 :

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
        pondre((Pondre))
        Voler((Voler))
        Allaiter((Allaiter))

        Mammifere -->|peut| Allaiter
        Mammifere -->|est un| Animal
        Oiseau -->|est un| Animal
        Oiseau -->|peut| Voler
        ChauveSouris -->|est un| Mammifere
        ChauveSouris -->|est un| Oiseau
        ChauveSouris -->|peut| Voler
        ChauveSouris -->|peut| pondre
        n(("non"))-->pondre
```

1. Les propriétés que la chauve-souris hérite:
    - De **Mammifère** : allaite ses petits
    - De **Oiseau** : peut voler

2. Conflits identifiés :
    - Un oiseau pond des oeufs, mais la chauve-souris ne pond pas d'Oeufs
    - Un oiseau n'allaite pas ses petits, mais la chauve-souris (mammifère) allaite ses petits
    - $\implies$ Contradiction : la chauve-souris ne peut pas être à la fois un oiseau et un mammifère selon les définitions classiques


## Exercice 2 :
- Tous les poissons vivent dans l’eau.
- Tous les animaux qui vivent dans l’eau peuvent nager.
- Les dauphins sont des mammifères.
- Les mammifères sont des animaux.
- Les dauphins vivent dans l’eau.

>En utilisant uniquement le réseau sémantique et la propagation d’héritage, démontrez que les dauphins peuvent nager


####  réseau sémantique
```mermaid
graph LR
    Animal((Animal))
    Poisson((Poisson))
    Mammifere((Mammifère))
    Dauphin((Dauphin))
    Eau((Etre <br> aquatique<hr>etre qui vie <br> dans l'eau))
    Nager((Nager))

    Poisson -->|est un| Eau
    Dauphin -->|est un| Eau
    Dauphin -->|est un| Mammifere
    Mammifere -->|est un| Animal
    Eau ---- et((et))
    Animal----et
    et-->|peut| Nager
```

dauphin herite le pouvoire de najer de l'agent etre aquatique


## Exercice 3 :
- Une personne possède un âge (valeur numérique).
- Un étudiant est une personne qui étudie un domaine.
- Un enseignant est une personne qui enseigne un domaine.
- Un professeur est à la fois enseignant et chercheur.
- Le domaine enseigné doit être le même que le domaine étudié pour un même cours.

>1. Construisez le réseau (nœuds, liens, types).
>2. Identifiez le type de contrainte.

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
    étudie -->|agent| Etudiant 
    étudie -->|objet| Domaine
    Enseignant -->|est une| Personne
    Cours -->|requiert| Domaine
    enseigne -->|objet| Domaine
    enseigne -->|agent| Enseignant
    Professeur -->|est un| Enseignant
    Professeur -->|est un| Chercheur
```
`est un(e)` : logique
<p style='border:1px solid;'> [un lien] </p>: conceptuel

## Exercice 4 :
- Chien → est un → Animal
- Chat → est un → Animal
- Animal → est un → ÊtreVivant
- Chien → lié À → Os
- Chat → lié À → Lait
- Os → type → Nourriture
>On active initialement le nœud Chien.<br>Appliquez une propagation d’activation (niveau = 3, facteur = 0.5).

```mermaid
graph
    chien((Chien<br> 1))
    chat((Chat<br>0.25))
    animal((Animal<br> 0.5))
    etre((ÊtreVivant<br>0.25))

    chien --est un--> animal
    chat --est un--> animal
    animal --est un--> etre
    os --est sort de--> n((Nouriture<br>0.25))
    chien --lié à--> os((Os<br>0.5))
    chat --lié à--> lait((Lait<br>0.125))
```

## Exercice 5 :
- Les oiseaux peuvent voler. 
- Les oiseaux nocturnes chassent la nuit. 
- Les hiboux sont des oiseaux nocturnes. 
- Les pingouins sont des oiseaux mais ne volent pas. 
- Les hiboux ne vivent pas dans l'eau. 
>Déterminez pour Pingouin et Hibou les propriétés héritées finales. 

#### réseau sémantique
```mermaid
graph
    Oiseau((Oiseau))
    OiseauNocturne((Oiseau<br>Nocturne))
    Hibou((Hibou))
    Pingouin((Pingouin))
    Voler((Voler))
    Chasser((Chasser<br>la nuit))
    Eau((Vivre dans<br>l'eau))
    peut((peut))
    peut2((peut))
    peut-->|agent| Oiseau
    peut-->|objet| Voler
    OiseauNocturne -->|peut| Chasser
    OiseauNocturne -->|est un| Oiseau
    Hibou -->|est un| OiseauNocturne
    n1((non))-->peut2
    peut2 -->|agent|Hibou
    peut2-->|objet|Eau
    Pingouin -->|est un| Oiseau
    Pingouin -->|exclusion|peut


```

#### Propriétés héritées finales :

**Hibou :**
- De **Oiseau** : peut voler
- De **Oiseau Nocturne** : chasse la nuit

**Pingouin :**
- De **Oiseau** : (exclusion pour voler)


## Exercice 6 :
>Traduisez en réseau sémantique :

- (∀x) Étudiant(x) → Personne(x) 
- (∀x) Étudiant(x) → ¬Travailleur(x) 
- Étudiant(Ali)
```mermaid
graph
    Personne((Personne))
    Etudiant((Étudiant))
    Travailleur((Travailleur))
    Ali((Ali))

    Etudiant -->|est une| Personne
    Etudiant -->|est un| Travailleur
    n(non)--> Travailleur
    Ali -->|est un| Etudiant
```

## Exercice 7 :

#### réseau sémantique partitionné
- Fièvre → symptôme → Maladie 
- Toux → symptôme → MaladieRespiratoire 
- Grippe → isa → MaladieRespiratoire 
- Grippe → hasSymptom → Fièvre, Toux 
- Pneumonie → isa → MaladieRespiratoire 
- Pneumonie → hasSymptom → Fièvre, DouleurPoitrine 
>Si un patient présente fièvre + toux, quelles maladies sont possibles ?


1. Patient présente : Fièvre + Toux
2. Grippe possède les deux symptômes (Fièvre + Toux) 
3. Pneumonie possède Fièvre mais pas Toux

**Maladies possibles : Grippe**

```mermaid
graph LR
    subgraph Hypothèse
        P((Patient))
        F((Fièvre))
        T((Toux))
        P -->|présente| F
        P -->|présente| T
    end
    
    subgraph Conclusion
        F-->|arg1|et1((et))
        T-->|arg2|et1
        et1-->|symptoms de|Grippe
    end
    T-->|arg1|et2((et))
    D-->|arg2|et2
    Grippe((Grippe))
    Pn((Pneumonie))

    et2-->|symptoms de|Pn

    D((Douleur<br>Poitrine))
    MR((Maladie<br>Respiratoire))
    Maladie((Maladie))
    Grippe -->|est une|MR
    Pn -->|est une|MR
    MR -->|est une|Maladie
    I((implication))
    I-->|h|Hypothèse
    I-->|c|Conclusion

```
