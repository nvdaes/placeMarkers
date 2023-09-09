# placeMarkers #

* Auteurs : Noelia, Chris.

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
*	Contrôle+maj+NVDA+y : Enregistre la position actuelle comme un
  marqueur. Si vous souhaitez donner un nom à ce marqueur, sélectionner un
  texte à partir de cette position avant de l'enregistrer.
*	Contrôle+maj+NVDA+effacement : Supprime le marqueur correspondant à cette
  position.
*	NVDA+y : Aller au marqueur suivant.
*	Maj+NVDA+y : Aller au marqueur précédent.
*	Non assignée : Affiche le nom du fichier dans lequel seront sauvegardés
  les marqueurs en mode navigation, sans extension.
*	Alt+NVDA+y : Ouvre un dialogue avec les marqueurs sauvegardés pour ce
  document. Vous pouvez écrire une note pour chaque marqueur ; Appuyez sur
  Enregistrer note pour enregistrer les modifications. En appuyant sur
  Supprimer vous pouvez supprimer le marqueur sélectionné. En appuyant sur
  OK vous pouvez vous déplacer à la position sélectionnée.
*	Non assigné : Enregistrer la position actuelle en tant que marqueur
  temporaire.
*	Non assigné : Ce déplacer au marqueur temporaire pour le document en
  cours.
*	Non assignée : Trouver l'occurrence suivante du dernier texte recherché
  pour n'importe quel document spécifique.
*	Non assignée : Trouver l'occurrence précédente du dernier texte recherché
  pour n'importe quel document spécifique.


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

## Changements pour la version 24.0
* Y est utilisé à la place de k dans des gestes tels que NVDA+k, NVDA+maj+k,
  NVDA+alt+k et NVDA+contrôle+maj+k.
* Compatible avec NVDA 2023.1.

## Changements pour la version 23.0
* L'extension fonctionne à nouveau avec Microsoft Word.

## Changements pour la version 22.0
* Nous pouvons passer aux marqueurs et les supprimer avec UIA activé, merci
  à Abdel.

## Changements pour la version 21.0
* Les marqueurs peuvent être enregistrés avec UIA activés dans les
  navigateurs basé sur Chromium, merci à Abdel.

## Changements pour la version 20.0
* Nécessite NVDA 2022 ou ultérieur.

## Changements pour la version 19.0 ##
* L'extension ne peut pas être exécuté sur des écrans sécurisés.

## Changements pour la version 18.0 ##
* La commande pour voir le chemin de placeMarkers affiche s'il y a des
  marqueurs permanents, du texte pour une recherche spécifique ou un
  marqueur temporaire pour le document actuel.

## Changements pour la version 17.0 ##
* Correction d'un bug qui ne permettait pas d'enregistrer les marqueurs dans
  certains documents.
* Correction des chaînes traduites faisant que les traductions fonctionnent
  correctement.

## Changements pour la version 16.0 ##
* Compatible avec NVDA 2021.1 ou version ultérieure (requis).
* La lecture rapide est prise en charge lors du passage à des marqueurs
  temporaires.
* Si nécessaire, vous pouvez télécharger [d'autres
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Changements pour la version 15.0 ##
* Durant la lecture avec Dire tout en mode navigation, les commandes
  spécifiques  de recherche précédent et suivant n'interrompront plus la
  lecture si "Permettre le survol en mode dire-tout" est activé,
  conformément aux commandes rechercher suivant et rechercher précédent de
  NVDA 2020.4.
* Si le dialogue de recherche spécifique est ouvert après exécution de la
  commande de recherche spécifique du précédent,  l'option "recherche
  précédent" sera sélectionnée.

## Changements pour la version 14.0 ##
*	La commande permettant de copier le nom du fichier dans lequel les données
  de Place Markers seront sauvegardées a été remplacée par une commande
  permettant d'afficher ce nom en mode navigation. Cette commande n'est pas
  assignée à un geste.
*	Le champ "Texte à rechercher" n'empiète plus sur le champ "texte
  sauvegardé". (Merci à Cyrille Bougot).
*	Nécessite NVDA 2019.3 ou ultérieur.

## Changements pour la version 13.0 ##
*	Ajout de commandes non assignées pour trouver l'occurrence suivante et
  l'occurrence précédente du dernier texte recherché pour l'importe quel
  document spécifique.
*	La fonctionnalité de recherche spécifique est disponible quand le dialogue
  "À propos" de NVDA est ouvert.
*	Dans le dialogue de recherche spécifique, la case à coché "sensible à la
  casse" sera cochée si cette option était sélectionnée lors de la dernière
  recherche.
*	Lors de la mise à jour de l'extension, les signets et textes de recherche
  spécifique sauvegardés dans la version précédente de l'extension seront
  automatiquement copiés dans la nouvelle version, à moins que vous ne
  préfériez importer les marqueurs sauvegardés dans le dossier principal de
  configuration de NVDA.
*	Lors de l'utilisation du dialogue de copie des marqueurs, si le dossier
  choisi ne s'appelle pas placeMarkersBackup, un sous-dossiers de ce nom
  sera créé pour éviter l'effacement de certains dossiers importants, tels
  que Documents ou Téléchargements. 

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
