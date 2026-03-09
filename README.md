🚗 Paris Traffic Simulator & Route Planner
Ce projet est un simulateur dynamique de trafic urbain pour la ville de Paris. Il utilise des données réelles d'OpenStreetMap et une API météo pour calculer l'itinéraire le plus rapide entre deux points en tenant compte des pics de congestion horaires et des conditions climatiques.

🛠️ Outils et Technologies
Le projet a été développé intégralement en Python avec les bibliothèques suivantes :

OSMnx : Extraction des données géographiques d'OpenStreetMap et modélisation du réseau routier sous forme de graphe.

NetworkX : Moteur mathématique pour le calcul du chemin le plus court (algorithme de Dijkstra / A*).

Streamlit : Création de l'interface utilisateur interactive (Dashboard Web).

Scikit-learn : Optimisation spatiale pour le repérage des nœuds GPS (nearest nodes).

Requests : Communication avec l'API Open-Meteo pour les données climatiques en direct.

Matplotlib : Rendu visuel et cartographique.

FPDF : Génération de rapports d'itinéraires au format PDF.

📝 Tâches effectuées et Étapes de développement
1. Acquisition et Modélisation des données
Téléchargement du réseau routier complet de Paris intra-muros.

Transformation des données brutes en un graphe topologique utilisable pour la navigation.

Nettoyage et enrichissement des données (vitesses autorisées, temps de trajet théoriques).

2. Développement du moteur de simulation (Traffic Engine)
Création d'un modèle mathématique cyclique simulant les pics de trafic (08h00 et 18h00).

Intégration d'un facteur météo dynamique : ralentissement automatique de 30% en cas de pluie détectée via l'API.

Développement d'une fonction de mise à jour des poids du graphe en temps réel.

3. Algorithme de recherche de chemin
Implémentation du géocodage pour permettre la saisie d'adresses textuelles (ex: "Bastille").

Mise en place du calcul de l'itinéraire optimal basé sur le poids travel_time_traffic (temps de trajet réel) plutôt que sur la distance physique.

4. Interface Utilisateur (Dashboard)
Développement d'une interface réactive avec Streamlit.

Intégration de curseurs interactifs pour l'heure et de champs de saisie pour les adresses.

Affichage de métriques clés : fluidité globale du réseau et estimation du temps d'arrivée.

Optimisation des performances via la mise en cache (caching) de la carte.

5. Exportation de données
Création d'un module de génération de rapports PDF automatisés incluant les détails du trajet et les conditions de trafic.

🚀 Installation et Lancement
Cloner le projet

Installer les dépendances :

Bash
pip install osmnx networkx streamlit scikit-learn requests matplotlib fpdf
Lancer l'application :

Bash
streamlit run app.py
📸 Aperçu
Carte : Rendu en mode sombre (Midnight Blue).

Trajet : Affichage de l'itinéraire optimal en rouge.

Statistiques : Calcul dynamique du temps de trajet selon la congestion.