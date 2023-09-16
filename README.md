# Scrapart - Scraper Automatique pour la Recherche d'Appartement

Scrappart est un scraper conçu pour automatiser la recherche d'appartements sur différents sites web d'annonces immobilières tels que LeBonCoin, SeLoger et PAP. Ce README vous guidera à travers la configuration et l'utilisation de ce bot.

## Configuration

### Requirements

Installez les dépendances : 
```
pip install -r requirements.txt
```

### Fichier de Configuration

Tout d'abord, vous devez accéder au fichier de configuration du bot.

### Encodage des Variables d'URL en Base64

Pour chaque site, les variables d'URL nécessaires doivent être encodées en base64. Par exemple, si vous recherchez un appartement à Rennes de 50 mètres carrés à moins de 200 euros, l'URL devrait être encodée en base64 comme suit :

URL d'origine :
```
https://www.leboncoin.fr/recherche?category=10&locations=Rennes__48.10980729840584_-1.6675040381352901_10000&real_estate_type=2&price=min-250&square=50-max
```

URL encodée en base64 :
```
aHR0cHM6Ly93d3cubGVib25jb2luLmZyL3JlY2hlcmNoZT9jYXRlZ29yeT0xMCZsb2NhdGlvbnM9UmVubmVzX180OC4xMDk4MDcyOTg0MDU4NF8tMS42Njc1MDQwMzgxMzUyOTAxXzEwMDAwJnJlYWxfZXN0YXRlX3R5cGU9MiZwcmljZT1taW4tMjUwJnNxdWFyZT01MC1tYXg=
```

Répétez cette opération pour les sites SeLoger et PAP.

### Configuration Spécifique pour PAP

Pour PAP, vous devrez également ajouter une liste de villes. Lorsque vous recherchez une ville comme "Rennes" sur PAP, cela peut également signifier "Paris" ou "Marseille". Séparez les villes par des virgules et un espace, par exemple : `paris, marseille`.

Pour déterminer le bon orthographe à utiliser, effectuez une recherche sur PAP.fr pour un appartement dans la ville cible et copiez-collez le nom de la ville à partir de l'annonce à Rennes. Cela garantira que vous utilisez la bonne orthographe sans majuscules, accents ou autres erreurs.

### Configuration des Adresses Email

Dans les sections `receiver` et `receiver2` du fichier de configuration, saisissez votre adresse email ainsi que l'adresse email OPTIONNELLE d'une personne de confiance.

### Configuration de l'Email GMAIL

Pour recevoir les notifications par email, assurez-vous d'utiliser une adresse Gmail et activez le POP/IMAP en suivant [ces instructions](https://support.google.com/a/answer/105694).

### Date de Fin d'Exécution

Enfin, spécifiez une date de fin d'exécution pour le programme en respectant le format de l'exemple par défaut.

## Utilisation

Une fois que vous avez configuré Scrappart selon vos préférences, laissez le bot fonctionner. Il rassemblera automatiquement les nouvelles annonces chaque jour et les enverra par email.

## Remarque

Veuillez noter que les sites LeBonCoin et SeLoger peuvent changer leur structure de page de temps en temps. Scrappart pourrait nécessiter des ajustements si cela se produit. Nous ne fournissons pas de support pour de tels changements, il vous appartient de maintenir et d'adapter le bot si nécessaire.

Merci d'utiliser Scrappart et bonne recherche d'appartement !

**Fin de la documentation - Bonne recherche !**
