# placeMarkers #
* Auteurs : Noelia, Chris.
* NVDA compatibility: 2019.3 or later.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension sert à sauvegarder et rechercher des chaînes de caractères
ou des marqueurs spécifiques sur des pages web ou des documents en Mode
navigation de NVDA. Elle peut également être utilisé pour sauvegarder et
rechercher des chaînes de caractères Dans des contrôleurs multilignes; dans
ce cas, s'il n'est pas possible de mettre à jour le point d'insertion, la
chaîne correspondante sera copiée dans le Presse-papiers, afin de pouvoir la
rechercher à l'aide d'autres outils. L'extension sauvegarde les textes et
les marqueurs spécifiés dans des fichiers. Le nom des fichiers est basé sur
le titre et l'url du document en cours.   Cette extension est basé sur les
extensions SpecificSearch et Bookmark&Search, développées par le même
auteur. Vous devriez les désinstaller pour utiliser celle-ci, car elles ont
des raccourcis et des caractéristiques communes.

## Touches de commandes : ##

*	Contrôle+maj+NVDA+f : Ouvre un dialogue avec une zone d'édition qui
  affiche la dernière recherche enregistrée; Dans ce dialogue, vous pouvez
  également sélectionner les recherches précédemment enregistrées dans une
  zone de liste déroulante ou supprimer la chaîne sélectionnée de
  l'historique à l'aide d'une case à cocher. Vous pouvez choisir si le texte
  contenu dans la zone d'édition sera ajouté à l'historique de vos textes
  enregistrés. Enfin, choisissez une action du prochain groupe de boutons
  radio (entre Recherche suivante, Recherche précédente ou Ne pas
  rechercher), et spécifiez si NVDA effectuera une recherche Respecter la
  casse. Lorsque vous appuyez sur OK, NVDA recherche cette chaîne.
*	Contrôle+maj+NVDA+k : Enregistre la position actuelle comme un
  marqueur. Si vous souhaitez donner un nom à ce marqueur, sélectionner un
  texte à partir de cette position avant de l'enregistrer.
*	Contrôle+maj+NVDA+effacement : Supprime le marqueur correspondant à cette
  position.
*	NVDA+k : Déplacer vers le marqueur suivant.
*	Maj+NVDA+k : Déplacer vers le marqueur précédent.
*	Not assigned: Shows the file name where the place markers data will be
  saved in browse mode, without an extension.
*	Alt+NVDA+k : Ouvre un dialogue avec les marqueurs sauvegardés pour ce
  document. Vous pouvez écrire une note pour chaque marqueur ; Appuyez sur
  Enregistrer note pour enregistrer les modifications. En appuyant sur
  Supprimer vous pouvez supprimer le marqueur sélectionné. En appuyant sur
  OK vous pouvez vous déplacer à la position sélectionnée.
*	Non assigné : Enregistrer la position actuelle en tant que marqueur
  temporaire.
*	Non assigné : Ce déplacer au marqueur temporaire pour le document en
  cours.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


## Sous-menu des marqueurs (NVDA+N) ##

En utilisant le sous-menu des marqueurs, dans le menu préférences de NVDA,
vous pouvez accéder à :

*	Dossier des recherches spécifiques : Ouvre le dossier des recherches
  spécifiques précédemment sauvegardées.
*	Dossier des marqueurs : Ouvre le dossier des marqueurs sauvegardés.
*	Copier le dossier des marqueurs : Vous pouvez sauvegarder une copie du
  dossier des marqueurs.
*	Restorer des marqueurs : Vous pouvez restorer vos marqueurs à partir d'un
  dossier de marqueurs précédemment sauvegardé.

Note : la position du marqueur est basé sur le nombre de caractères. Dans
les pages au contenu dynamique, il vaut mieux utiliser la recherche de texte
spécifique, pas les marqueurs.

## Changes for 14.0 ##
*	The command to copy the name of the file where place markers data will be
  saved has been replaced by a command which shows this file name in browse
  mode. This is not assigned to a gesture.
*	The "Text to search" field does not overlap the "Saved text" field
  anymore. (Thanks to Cyrille Bougot).
*	Requires NVDA 2019.3 or later.

## Changes for 13.0 ##
*	Added not assigned commands to find the next and previous occurrences of
  the last text searched for any specific document.
*	The specific search feature works when the NVDA's About dialog is open.
*	In the Specific search dialog, the case sensitive checkbox will be checked
  if this option was selected for the last search.
*	When the add-on is updated, bookmarks and strings for specific search
  saved in the previous version of the add-on will be automatically copied
  to the new version, unless you prefer to import place markers saved in the
  main configuration folder of NVDA.
*	When using the dialog to copy place markers, if the chosen folder is not
  named placeMarkersBackup, a subfolder with this name will be created to
  prevent the deletion of directories containing important data, such as
  Documents or Downloads.

## Changements pour la version 12.0 ##
*	Correction d'un bug critique qui provoquait le blocage de NVDA lors de la
  tentative d'ouverture de la boîte de dialogue Notes, si les caractères
  chinois étaient sélectionnés avant la sauvegarde des marqueurs.

## Changements pour la version 11.0 ##
*	Compatible avec NVDA 2018.3 ou version ultérieure (requis).
*	Si nécessaire, vous pouvez télécharger la [dernière version compatible
  avec NVDA 2017.3][3].

## Changements pour la version 10.0 ##
*	Dans Edge, les gestes associés à la sélection de marqueurs tels que
  NVDA+k, NVDA+maj+k ou NVDA+alt+k, seront envoyés à l'application au lieu
  d'essayer de déplacer le curseur sur les marqueurs pour éviter les
  erreurs, en particulier dans de longs documents.
*	La recherche de texte spécifique est maintenant prise en charge dans Edge.

## Changements pour la version 9.0
*	Lorsque vous déplacez un marqueur dans le dialogue Notes, le curseur de
  revue suit le curseur système.
*	La commande permettant de sélectionner le marqueur précédent fonctionne à
  nouveau correctement.
*	Les marqueurs peuvent être supprimés depuis le dialogue Notes.
*	Vous pouvez maintenant assigner des gestes pour sauvegarder et déplacer un
  marqueur temporaire pour chaque document.

## Changements pour la version 8.0 ##
*	Identificateurs de fragment Supprimé pour les noms de fichiers  des
  marqueurs, qui peut éviter des problèmes dans le lecteur VitalSource
  Bookshelf ePUB.
*	Ajout d'un dialogue Notes, pour associer des commentaires aux marqueurs
  sauvegardés et se déplacer à la position sélectionnée.

## Changements pour la version 7.0 ##
*	Le dialogue pour enregistrer une chaîne de caractères pour la recherche
  spécifique a été supprimée. Cette fonctionnalité est maintenant incluse
  dans le dialogue Recherche spécifique, qui a été redessinée pour permettre
  différentes actions lorsque vous appuyez sur le bouton OK.
*	La présentation visuelle des dialogues a été améliorée, en respectant
  l'apparence des dialogues présentés dans NVDA.
*	L'exécution d'une commande Rechercher Suivant ou Rechercher Précédent dans
  le Mode Navigation effectuera maintenant correctement une recherche
  Respecter la casse si la recherche d'origine était Respecter la casse.
*	Nécessite NVDA 2016.4 ou ultérieur.
*	Vous pouvez maintenant assigner des gestes pour ouvrir les dialogues
  Copier et Restaurer les marqueurs de position.
*	NVDA affichera un message pour notifier lorsque les marqueurs de position
  auront été copiés ou restaurés avec les dialogues correspondants.

## Changements pour la version 6.0 ##
* Lorsque les fonctionnalités de l'extension ne sont pas utilisables, les
  gestes sont envoyés à l'application correspondante.

## Changements pour la version 5.0 ##
* Ajout de la recherche Respecter la casse.
* L'option d'ouverture de la documentation a été retirée du menu des
  marqueurs.
* Commandes de base plus intuitives.

## Changements pour la version 4.0 ##
* Identificateurs de fragment Supprimé pour les noms de fichiers  des
  marqueurs, qui peut éviter des problèmes dans le module ePUBREADER de
  Firefox.
* L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 3.1 ##
* Mises à jour des traduction et nouvelle langue.
* La position du marqueur n'est pas annoncé dans la lecture rapide.

## Changements pour la version 3.0 ##
* Ajout du support de la lecture rapide.

## Changements pour la version 2.0 ##
* Ajout de la possibilité de sauvegarder et supprimer des recherches
  différentes pour chaque fichier ajouté.
* Correction d'un bug avec des chemins contenant des caractères non latins.
* Les raccourcis peuvent désormais être réaffectés en utilisant le dialogue
  des raccourcis de NVDA.

## Changements pour la version 1.0 ##
* Première version
* Traduit en : Portugais Brésilien , Farsi, Finnois, Français, Galicien,
  Allemand, Italien, Japonais, Coréen, Nepali, Portugais, Espagnol,
  Slovaque, Slovène, Tamil.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
