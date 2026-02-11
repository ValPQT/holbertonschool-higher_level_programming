1️⃣ Expliquer les différences et similitudes entre marshaling et serialization

Points communs :

Les deux consistent à transformer un objet ou une structure de données en un format transmissible.

Les deux permettent d’envoyer des données sur un réseau, de les stocker dans un fichier ou une base de données.

Les deux impliquent une transformation vers un format structuré.

Différences :

Serialization	Marshaling
Convertit un objet en un format stockable ou transmissible (JSON, XML, binaire…).	Prépare les données spécifiquement pour un appel distant (RPC, API, communication inter-processus).
Concept général.	Concept souvent lié aux systèmes distribués.
Exemple : sauvegarder un objet Python en JSON.	Exemple : transformer un objet pour l’envoyer via une API REST ou un service distant.

👉 En résumé :
La serialization est le concept général, le marshaling est une forme spécialisée utilisée pour la communication entre systèmes.

2️⃣ Mettre en place la sérialisation dans une tâche pratique

Exemple simple en Python :

import json

data = {
    "name": "Valentin",
    "age": 25,
    "skills": ["Python", "C", "SQL"]
}

# Sérialisation (Python → JSON string)
json_string = json.dumps(data)

# Désérialisation (JSON string → Python)
python_data = json.loads(json_string)

print(json_string)
print(python_data)


Applications pratiques :

Sauvegarde d’un objet utilisateur dans un fichier

Stockage temporaire de données

Envoi de données via une API

3️⃣ Comment les données sérialisées sont utilisées dans :
🌐 Applications web

Envoi de données entre client et serveur (JSON via HTTP)

API REST utilisent presque toujours JSON

Stockage des sessions utilisateur

🗄 Bases de données

Stockage de documents JSON (MongoDB)

Sauvegarde d’objets convertis en JSON dans SQL

Archivage de données structurées

🌍 Communications réseau

Transmission de données entre microservices

RPC (Remote Procedure Call)

Systèmes distribués

4️⃣ Comparer les performances des formats (JSON, XML, binaire)
Format	Avantages	Inconvénients	Performance
JSON	Lisible, léger, universel	Pas optimal pour très gros volumes	Rapide et efficace
XML	Très structuré, extensible	Plus verbeux (plus lourd)	Plus lent que JSON
Binaire (ex: Protocol Buffers, MessagePack)	Très rapide, compact	Non lisible humainement	⭐ Le plus performant

👉 En pratique :

JSON = meilleur compromis (web, APIs)

XML = legacy / systèmes anciens

Binaire = haute performance (jeux, microservices, systèmes temps réel)

🎯 Résumé clair

Serialization = transformer des objets en format transmissible.

Marshaling = préparer ces données pour communication distante.

JSON est le standard web.

Les formats binaires sont les plus rapides.

XML est plus lourd mais très structuré.
