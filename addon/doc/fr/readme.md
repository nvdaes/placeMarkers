[[!meta title="placeMarkers"]]

* Auteurs : Noelia, Chris.
* Télécharger : [Version 1.0][1]

This addon is used for saving and searching specific text strings or
bookmarks, on web pages or documents in NVDA's browse mode.  The plugin
saves the specified strings and bookmarks to text and pickle files. The name
of these files is based on the title and URL of the current document.

Ce module est basé sur les modules SpecificSearch et Bookmark&Search,
développés par le même auteur. Vous devrez les désinstaller avant
d'installer celui-ci, car ils possèdent des raccourcis et des
fonctionnalités communs.

## Touches de commandes : ##

*	control+maj+NVDA+s; Ouvre un dialogue pour sauvegarder a une chaîne de
  texte que vous désirez rechercher dans le document en cours. Par défaut,
  le texte précédemment sauvegardé pour ce document est proposé. Si ce texte
  est effacé, le fichier le contenant sera également effacé. 
*	control+maj+NVDA+f; Si le document en cours a un fichier texte pour une
  recherche spécifique, un dialogue s'ouvre affichant le texte
  sauvegardé. Quand vous pressez "OK", NVDA lance la recherche. Si ce
  document ne possède pas de fichier de recherche, NVDA l'annonce sans
  ouvrir de dialogue.
*	control+maj+NVDA+k; Sauvegarde la position courante comme marqueur
*	control+maj+NVDA+effac; efface le marqueur correspondant à cette position.
*	control+maj+k; Va au marqueur suivant.
*	maj+NVDA+k; Va au marqueur précédent.
*	NVDA+k; Copie dans le presse-papier le nom du fichier sans extension dans
  lequel pourraient être sauvegardés les marqueurs (mosition ou chaîne à
  rechercher).

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

## Changements pour la version 1.0 ##
* Première version
* Translated into: Brazilian Portuguese, Farsi, Finnish, French, Galician,
  German, Italian, Japanese, Korean, Nepali, Portuguese, Spanish, Slovak,
  Slovenian, Tamil.

[1]: http://addons.nvda-project.org/files/get.php?file=pm
