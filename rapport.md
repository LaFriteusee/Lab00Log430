# Rapport – Labo 00 : Infrastructure (Git, Docker, CI/CD)

ÉTS - LOG430 - Architecture logicielle

**Étudiant : Thomas Journault**  
**Date : 11 mai 2026**  
**Dépôt GitHub : [https://github.com/LaFriteusee/Lab00Log430](https://github.com/LaFriteusee/Lab00Log430)**  

---

## Question 1

Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

### Réponse

Lorsqu'un test échoue, pytest affiche un rapport détaillé qui aide à localiser l'erreur de plusieurs façons :

- **Le nom du test en échec** est affiché clairement avec la mention `FAILED` en rouge dans le bas tu test.
- **L'erreur est montrer sur plusieurs ligne qui commence par E** qui nous dit d'où viens l'erreur et nous dit la ligne et le fichier ou l'erreur c'est produite a la fin. dans ce cas ci `src\tests\test_calculator.py:18` donc le fichier test_calculator à la ligne 18.
- **La valeur obtenue et la valeur attendue** sont comparées côte à côte, ce qui permet de voir immédiatement l'écart.
- Un résumé final indique le nombre de tests passés, échoués et ignorés.

### Test provoquant volontairement une erreur

```python
def test_addition_erreur_volontaire():
    assert Calculator().addition(2, 3) == 99  # erreur volontaire : le résultat attendu est faux
```


### Sortie du terminal

![alt text](/Image/image.png)

---

## Question 2

Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

### Réponse

#### Set up job

L'étape **Set up job** est automatiquement ajoutée par GitHub Actions au début de chaque job. Elle prépare l'environnement d'exécution avant que les étapes définies dans le workflow ne commencent. On peut voir dans la sortie ci-dessous que GitHub :

- Indique la version du runner utilisé (`2.334.0`) ainsi que l'image du système d'exploitation (`ubuntu-24.04`) qui est l'os de la vm que nous avons créer au cours de ce laboratoire.
- Configure les permissions du token `GITHUB_TOKEN` (lecture du contenu, des métadonnées et des packages).
- Prépare le répertoire de travail du workflow.
- Télécharge les actions nécessaires (`actions/checkout@v3` et `actions/setup-python@v4`) afin de les préparer pour les prochaines étapes dont Checkout dépôt.

![Set up job](/Image/image-1.png)

#### Checkout dépôt

L'étape **Checkout dépôt** utilise l'action `actions/checkout@v3`. Son rôle est de cloner le dépôt GitHub sur le runner afin que les étapes suivantes puissent accéder au code source. On peut voir dans la sortie ci-dessous que GitHub :

- Initialise un dépôt Git vide sur le runner (` /usr/bin/git init /home/runner/work/Lab00Log430/Lab00Log430` ligne 24).
- Configure l'URL du dépôt distant (` /usr/bin/git remote add origin https://github.com/LaFriteusee/Lab00Log430` ligne 39).
- Télécharge le code source depuis GitHub (` /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +b349a6a2f133ee38a6533377b2523b36281ee9c3:refs/remotes/origin/main` ligne 49).
- Se positionne sur la bonne branche (`/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main` ligne 125).

![Checkout dépôt - partie 1](/Image/image-2.png)
![Checkout dépôt - partie 2](/Image/image-3.png)

---

## Question 3

Quel type d'informations pouvez-vous obtenir via la commande `top` ? Veuillez donner quelques exemples. Veuillez inclure la sortie du terminal dans votre réponse.

### Réponse

La commande `top` affiche en temps réel les différents processus de linux et elle est divisée en deux sections :

**En-tête (informations globales du système) :**
- **Uptime et charge** : la VM `vm-thomas-log430` tourne depuis 1 jour et 20 heures, avec une charge moyenne très faible (`0.08, 0.03, 0.01`), ce qui indique que le système est presque inactif.
- **Tâches (Tasks)** : 80 processus au total, dont 1 en cours d'exécution (`running`) et 79 en attente (`sleeping`). 
- **CPU (%)** : le CPU est inactif à 100% (`100.0 id`), ce qui confirme qu'aucune tâche ne sollicite le processeur au moment de la capture.
- **Mémoire (MiB Mem)** : la VM dispose de 3587 MiB de RAM au total, dont seulement 154.8 MiB utilisés et 2410.1 MiB en cache.

**Liste des processus :**

Chaque ligne correspond à un processus actif. Les colonnes principales sont :

| Colonne | Description |
|---------|---------|-------------|
| `PID` | Identifiant unique du processus |
| `USER` | Utilisateur propriétaire du processus |
| `%CPU` | Pourcentage du CPU consommé |
| `%MEM` | Pourcentage de la RAM consommée |
| `COMMAND` | Nom de la commande ou du programme |

**exemple**
le système roule sur le PID 1 sur l'utilisateur root qui est admin du système. ont peut voir qu'il utilise 0% du cpu donc très faible utilisation ainsi que 0.3% de la mémoire ce qui est très fiable aussi
### Sortie du terminal

![alt text](/Image/image-4.png)
