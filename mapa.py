#tentei usar python porém não deu certo
# Importa as bibliotecas necessárias
from flask import Flask, render_template
import folium 

# Cria a instância do aplicativo Flask
app = Flask(__name__)

# Define a rota para a página inicial
@app.route("/")
def home():
    # Renderiza o template HTML da página inicial
    return render_template("mapa.html")

# Define a rota para a página do mapa
@app.route("/mapa")
def mapa():
    # Cria um mapa usando o Folium com localização inicial em São Francisco
    crime_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)  # Localização inicial e zoom
    # Adiciona um marcador no mapa com descrição "Crime Exemplo"
    folium.Marker(
        location=[37.7749, -122.4194],  # Coordenadas do marcador
        popup="Crime Exemplo",  # Texto exibido ao clicar no marcador
        tooltip="Clique para mais detalhes"  # Texto que aparece ao passar o mouse sobre o marcador
    ).add_to(crime_map)
    
    # Salva o mapa gerado em um arquivo HTML dentro da pasta templates
    crime_map.save("templates/map.html")
    
    # Renderiza o template do mapa
    return render_template("map.html")

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == "__main__":
    # Inicia o servidor Flask em modo de depuração
    app.run(debug=True)


# Lista de crimes com suas respectivas localizações e descrições
crimes = [
    {"lat": 37.7749, "lon": -122.4194, "description": "Assalto em San Francisco"},
    {"lat": 37.7849, "lon": -122.4094, "description": "Roubo em Market Street"},
]

# Adiciona um marcador para cada crime na lista no mapa
for crime in crimes:
    folium.Marker(
        location=[crime["lat"], crime["lon"]],  # Coordenadas do crime
        popup=crime["description"],  # Descrição do crime exibida ao clicar
        tooltip="Clique para mais detalhes"  # Texto ao passar o mouse
    ).add_to(crime_map)  # Adiciona o marcador ao mapa

