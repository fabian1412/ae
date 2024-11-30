import streamlit as st

# Título de la app
st.title("Aplicación de Videojuegos")

# Descripción
st.write("Bienvenido a la aplicación de videojuegos. Selecciona tu videojuego favorito y obtén estadísticas e información adicional.")

# Crear una lista de videojuegos populares
videojuegos = [
    'The Legend of Zelda',
    'Minecraft',
    'Fortnite',
    'Call of Duty',
    'Among Us'
]

# Selector para elegir un videojuego
eleccion = st.selectbox('Selecciona tu videojuego favorito:', videojuegos)

# Mostrar detalles del videojuego seleccionado
def mostrar_detalles(eleccion):
    if eleccion == 'The Legend of Zelda':
        st.write("**The Legend of Zelda** es una serie de videojuegos de aventura desarrollada por Nintendo. Es conocida por su exploración en mundo abierto y su innovador diseño de rompecabezas.")
        st.image("(link unavailable)", width=300)
        st.write("¡Juega como Link y salva a la Princesa Zelda del malvado Ganon!")
    elif eleccion == 'Minecraft':
        st.write("**Minecraft** es un videojuego de construcción y aventura donde los jugadores exploran un mundo generado proceduralmente, construyen estructuras y luchan contra criaturas.")
        st.image("(link unavailable)", width=300)
        st.write("¡Construye, explora y sobrevive en un mundo hecho completamente de bloques!")
    elif eleccion == 'Fortnite':
        st.write("**Fortnite** es un videojuego de batalla real donde 100 jugadores compiten para ser el último en pie en una isla llena de armas y recursos.")
        st.image("(link unavailable)", width=300)
        st.write("¡Lucha, construye y sobrevive en una intensa batalla por la victoria!")
    elif eleccion == 'Call of Duty':
        st.write("**Call of Duty** es una franquicia de videojuegos de disparos en primera persona conocida por sus intensos combates, gráficos realistas y modos multijugador competitivos.")
        st.image("(link unavailable)", width=300)
        st.write("¡Prepárate para el combate con una de las sagas más populares de la historia de los videojuegos!")
    elif eleccion == 'Among Us':
        st.write("**Among Us** es un juego multijugador de deducción social donde los jugadores deben descubrir al 'impostor' entre ellos mientras completan tareas en una nave espacial.")
        st.image("(link unavailable)", width=300)
        st.write("¡Colabora con tu equipo para identificar al impostor o embárcate en un sabotaje en una nave espacial!")

mostrar_detalles(eleccion)

# Mostrar recomendaciones basadas en la elección
def mostrar_recomendaciones(eleccion):
    st.write("**Recomendaciones**")
    if eleccion == 'The Legend of Zelda':
        st.write("Si te gusta 'The Legend of Zelda', puedes probar también: 'Super Mario Odyssey', 'Horizon Zero Dawn', o 'The Witcher 3'.")
    elif eleccion == 'Minecraft':
        st.write("Si te gusta 'Minecraft', te recomendamos: 'Terraria', 'Don't Starve', o 'Roblox'.")
    elif eleccion == 'Fortnite':
        st.write("Si te gusta 'Fortnite', podrías probar: 'Apex Legends', 'PUBG', o 'Battlefield V'.")
    elif eleccion == 'Call of Duty':
        st.write("Si te gusta 'Call of Duty', te recomendamos: 'Battlefield', 'Halo', o 'Rainbow Six Siege'.")
    elif eleccion == 'Among Us':
        st.write("Si te gusta 'Among Us', puedes probar: 'Mafia', 'Secret Hitler', o 'Project Winter'.")

mostrar_recomendaciones(eleccion)

# Mostrar estadísticas del juego
def mostrar_estadisticas(eleccion):
    estadisticas = {
        'The Legend of Zelda': {'Lanzamiento': '1986', 'Plataforma':