# Mes Collections — Ondres · Sud des Landes

Album personnel de collectionneur, en une seule page web :

- **Cartes postales** : fiches recto/verso, filtres (Ondres, Boucau, Tarnos, Landes, pays, thèmes, époques), carte des points de vue et statistiques.
- **Pièces de 2 €** : les 663 pièces émises de 1999 à 2026 dans les pays de l'euro, à cocher, avec une notice historique pour chaque émission.

Site : https://paullerouxlarre-debug.github.io/mes-collections/

## Organisation du dépôt

| Fichier | Rôle |
| --- | --- |
| `src/app.html` | Source unique de l'application (on ne modifie que ce fichier). |
| `src/build.py` | Construit `index.html` et `dist/mes-collections.html`. |
| `index.html` | Page servie par GitHub Pages. |
| `dist/mes-collections.html` | Même page, publiée dans Claude. |
| `manifest.webmanifest`, `icon-*.png` | Icône et nom pour l'écran d'accueil de l'iPhone. |

Après une modification : `python3 src/build.py`, puis commit et push. GitHub Pages redéploie en une minute environ.

## Vos données

Les cartes, photos et pièces cochées sont enregistrées **dans le navigateur** de l'appareil. Une mise à jour du site ne les efface pas : elles restent liées à l'adresse du site, pas au code.

Le bouton **Sauvegarde** (en haut à droite, ou sur l'écran d'accueil) permet :

- de **télécharger** un fichier `.json` avec toutes les cartes, leurs photos et les pièces cochées ;
- de **restaurer** ce fichier sur un autre appareil, ou dans la version Claude ; les éléments existants sont conservés.

Gardez une sauvegarde récente : vider les données du navigateur efface l'album.

## Sources

Notices des pièces rédigées d'après les fiches de la Banque centrale européenne. Contours des communes : IGN (via france-geojson). Côtes et fleuves : Natural Earth.
