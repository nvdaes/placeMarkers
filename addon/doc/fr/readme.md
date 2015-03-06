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

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

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


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

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
