# placeMarkers #

* Auteurs : Noelia, Chris.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce module sert à sauvegarder et rechercher des chaînes de caractères ou des
marqueurs spécifiques sur des pages web ou des documents en mode
navigation. Le module sauvegarde les textes et les marqueurs spécifiés dans
des fichiers. Le nom des fichiers est basé sur le titre et l'url du document
en cours.

Ce module est basé sur les modules SpecificSearch et Bookmark&Search,
développés par le même auteur. Vous devrez les désinstaller avant
d'installer celui-ci, car ils possèdent des raccourcis et des
fonctionnalités communs.

## Touches de commandes : ##

*	control+maj+NVDA+s; Ouvre une boîte de dialogue qui vous permet d'enregistrer une chaîne de texte que vous voulez trouver dans le document actuel. Par défaut, le texte précédemment enregistré pour ce fichier est affiché. Supprimer ce texte et appuyez sur le bouton OK si vous souhaitez supprimer le fichier texte correspondant à la recherche enregistrée, ou tapez un nouveau texte pour ajouter une autre recherche.
*	Control+maj+NVDA + f; ouvre une boîte de dialogue avec un champ d'édition qui indique la dernière recherche enregistrée, dans ce dialogue, vous pouvez également sélectionner les recherches précédemment sauvegardées à partir d'une zone de liste déroulante et choisir une action dans la liste déroulante suivante. S'il n'y a pas de fichiers disponibles pour la recherche spécifiée dans le document actuel, NVDA vous préviendra qu'il ne trouve pas un fichier pour la recherche spécifiée.
*	Control+maj+NVDA + k; Enregistre la position actuelle comme signet
*	Control+maj+NVDA+Suppr; Supprime le signet correspondant à cette position
*	NVDA+k; Passe au signet suivant
*	Maj+NVDA+k; Passe au signet précédent
*	Control+maj+k; Copies au presse-papiers le nom du fichier, sans extension, où la place des données de marqueurs seront sauvés

## Sous-menu des marqueurs (NVDA+N) ##


En utilisant le sous-menu des marqueurs, dans le menu préférences, vous
pouvez accéder à :

*	Dossier des recherches spécifiques : Ouvre le dossier des recherches
  spécifiques précédemment sauvegardées.
*	Dossier des marqueurs : Ouvre le dossier des marqueurs sauvegardés.
*	Copier le dossier des marqueurs; Vous pouvez sauvegarder une copie du
  dossier des marqueurs.
*	Restorer le dossier des marqueurs; Vous pouvez restorer le dossier des
  marqueurs à partir d'un dossier de marqueurs précédemment sauvegardé.
*	Fichier de documentation, dans votre langue si elle est disponible ou en
  Anglais par défaut.

Note: la position du marqueur est basé sur le nombre de caractères. Dans les
pages au contenu dynamique, il vaut mieux utiliser la recherche de texte
spécifique pour marquer une position particulière.

## Changements pour la version 6.0 ##
* Lorsque les fonctionnalités du module complémentaire ne sont pas
  utilisables, les gestes sont envoyés à l'application correspondante.

## Changements pour la version 5.0 ##
* Ajout de la recherche sensible à la casse.
* L'option d'ouverture de la documentation a été retirée du menu des
  marqueurs.
* Commandes de base plus intuitives.

## Changements pour la version 4.0 ##
* Identificateurs de fragment Supprimé pour les noms de fichiers  des
  marqueurs , qui peut éviter des problèmes dans le module ePUBREADER de
  Firefox.
* L'aide du module complémentaire est disponible à partir du Gestionnaire de
  modules complémentaires.

## Changements pour la version 3.1 ##
* Mises à jour des traduction et nouvelle langue.
* La position du marqueur n'est pas annoncé dans la lecture rapide.

## Changements pour la version 3.0 ##
* Ajout du support de la lecture rapide.

## Changements pour la version 2.0 ##
* Ajout de la possibilité de sauvegarder et supprimer des recherches
  différentes pour chaque fichier ajouté.
* Correction d'un bug avec des chemins contenant des caractères non latins.
* Les raccourcis peuvent désormais être réaffectés en utilisant la boîte de
  dialogue des raccourcis de NVDA.

## Changements pour la version 1.0 ##
* Première version
* Traduit en : Portugais Brésilien , Farsi, Finnois, Français, Galicien,
  Allemand, Italien, Japonais, Coréen, Nepali, Portugais, Espagnol,
  Slovaque, Slovène, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
