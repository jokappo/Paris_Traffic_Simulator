import streamlit as st
import osmnx as ox
import networkx as nx
import numpy as np
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Paris Traffic Simulator", layout="wide")
st.title("🚗 Paris Traffic Simulator")


@st.cache_resource
def load_map():
    # Chargement unique de la carte
    G = ox.graph_from_place("Paris, France", network_type='drive')
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    return G


G = load_map()

# --- SIDEBAR ---
st.sidebar.header("🕹️ Contrôles")
heure = st.sidebar.slider("Choisir l'heure", 0, 23, datetime.now().hour)
depart_addr = st.sidebar.text_input("Départ", "Place de la Bastille, Paris")
arrivee_addr = st.sidebar.text_input("Arrivée", "Arc de Triomphe, Paris")


# --- CALCUL DU TRAFIC ---
def get_factors(h):
    f_h = 0.5 + 0.4 * np.cos((h - 13) * np.pi / 10)
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&current_weather=true"
        r = requests.get(url).json()
        f_m = 0.7 if r['current_weather']['weathercode'] >= 51 else 1.0
    except:
        f_m = 1.0
    return f_h * f_m


fluidite = get_factors(heure)

# 1. BOUCLE DE TRAFIC 
for u, v, data in G.edges(data=True):
    vitesse_base = data.get("speed_kph", 30)
    vitesse_reelle = vitesse_base * fluidite
    data["travel_time_traffic"] = data["length"] / (vitesse_reelle / 3.6)

# 2. CALCUL ET AFFICHAGE 
try:
    # Géocodage et calcul
    dep_coords = ox.geocode(depart_addr)
    arr_coords = ox.geocode(arrivee_addr)
    node_dep = ox.nearest_nodes(G, X=dep_coords[1], Y=dep_coords[0])
    node_arr = ox.nearest_nodes(G, X=arr_coords[1], Y=arr_coords[0])

    route = nx.shortest_path(G, node_dep, node_arr, weight="travel_time_traffic")
    temps_sec = nx.shortest_path_length(G, node_dep, node_arr, weight="travel_time_traffic")

    # Metrics
    col1, col2 = st.columns(2)
    col1.metric("Fluidité globale", f"{fluidite * 100:.0f}%")
    col2.metric("Temps estimé", f"{int(temps_sec / 60)} min")

    # Graphique
    fig, ax = ox.plot_graph_route(
        G, route, route_color="red", node_size=0,
        bgcolor="#061529", edge_color="#1f77b4",
        show=False, close=False
    )
    st.pyplot(fig)
    plt.close(fig)  

except Exception as e:
    st.error(f"Oups ! Impossible de trouver ce trajet. Précisez l'adresse (ex: 'Bastille, Paris').")