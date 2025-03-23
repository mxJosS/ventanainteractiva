import tkinter as tk
from PIL import Image, ImageTk
import requests
import io


def pasar_img(num):
    # URL de la imagen
    match num:
        case 1:
            url = "https://statics.cinemex.com/movie_posters/4iS7qSgNyjmvAuo-360x540.jpg" 
        case 2: 
            url = "https://statics.cinemex.com/movie_posters/Dc4YkI5yPpDvsV6-360x540.jpg"
        case 3: 
            url = "https://statics.cinemex.com/movie_posters/TlLXCncPHH3gQiS-360x540.jpg"
            
    response = requests.get(url)
    img_data = response.content

    # Abre la imagen con PIL
    imagen = Image.open(io.BytesIO(img_data))

    # Crea la imagen compatible con Tkinter (ya existe la ventana raíz)
    tk_imagen = ImageTk.PhotoImage(imagen)

    return tk_imagen
    # Muestra la imagen en una etiqueta
    #etiqueta = tk.Label(root, image=tk_imagen)
    #etiqueta.pack()
