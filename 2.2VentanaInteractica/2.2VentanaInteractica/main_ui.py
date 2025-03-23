import tkinter as tk  # Importa la biblioteca Tkinter para crear la interfaz gráfica
from tkinter import Toplevel, messagebox  # Importa clases para ventanas adicionales y cuadros de mensaje
from img_url import pasar_img

# Registro de numero de ventanas abiertas (numero)
ventanas_abiertas = set()
# Variable global para llevar la ventana activa (actualmente abierta)
ventana_activa = None

def obtener_texto(i):
    match i:
        case 1:
            return "Película de Esteno"
        case 2:
            return "Pelicula en Preventa"
        case 3:
            return "Proximo Estreno"
        case _:
            return "Sin Título"

def abrir_ventana(num_ventana):
    global ventana_activa

    # Si ya hay una ventana activa, no se abre otra
    if ventana_activa is not None and ventana_activa.winfo_exists():
        messagebox.showwarning("Aviso", "Ya hay una ventana abierta. Cierre la ventana actual para abrir otra.")
        return

    # Registrar que se abrió esta ventana
    ventanas_abiertas.add(num_ventana)
    # Si ya se abrieron las 3 ventanas, habilitamos el botón para cerrar la principal
    if len(ventanas_abiertas) == 3:
        boton_cerrar_principal.config(state=tk.NORMAL)

    nueva_ventana = tk.Toplevel(ven_principal)
    nueva_ventana.title(f"Nueva Ventana {num_ventana}")
    
    # Deshabilitar el botón de cerrar (la 'X')
    nueva_ventana.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # --- Para hacer que la nueva ventana salga cerca de la princ ---
    # Definir el tamaño deseado para la ventana principal
    window_width = 400
    window_height = 600

    # Obtener el ancho y alto de la pantalla
    screen_width = nueva_ventana.winfo_screenwidth()
    screen_height = nueva_ventana.winfo_screenheight()

    # Calcular la posición x, y para centrar la ventana
    x = (screen_width - window_width) // 4
    y = (screen_height - window_height) // 4

    # Establecer la geometría de la ventana principal
    nueva_ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # -----------------------------------------------------

    # Las img se consiguen de un url
    img_linea = pasar_img(num_ventana)

    # Contenido de la ventana secundaria
    etiqueta = tk.Label(nueva_ventana, image=img_linea)
    etiqueta.image = img_linea # Guardar referencias, para desplegarce
    etiqueta.pack()

    
    # Función para cerrar la ventana y restablecer la variable global
    def cerrar_ventana():
        nueva_ventana.destroy()
        global ventana_activa
        ventana_activa = None

    # Botón para cerrar la ventana, inicialmente deshabilitado; se usa la función cerrar_ventana
    boton_cerrar_ventana = tk.Button(nueva_ventana, text="Cerrar ventana", state=tk.DISABLED,
                                     command=cerrar_ventana)
    boton_cerrar_ventana.pack(padx=20, pady=20)
    
    # Luego de 10 segundos, se habilita el botón para cerrar la ventana
    # 10000 = 10s
    nueva_ventana.after(3000, lambda: boton_cerrar_ventana.config(state=tk.NORMAL))

    # Asignar la ventana recién creada como la activa
    ventana_activa = nueva_ventana

ven_principal = tk.Tk()
ven_principal.title("Cine")
ven_principal.minsize(width= 300, height=400)
ven_principal.config(padx= 35, height=45)
ven_principal.protocol("WM_DELETE_WINDOW", lambda: None) #Comando para deshabilitar el X de cerrar

# --- Centrar la ventana principal en la pantalla ---
# Definir el tamaño deseado para la ventana principal
window_width = 300
window_height = 400

# Obtener el ancho y alto de la pantalla
screen_width = ven_principal.winfo_screenwidth()
screen_height = ven_principal.winfo_screenheight()

# Calcular la posición x, y para centrar la ventana
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Establecer la geometría de la ventana principal
ven_principal.geometry(f"{window_width}x{window_height}+{x}+{y}")
# -----------------------------------------------------

# Botones para las ventanas
for i in range(1, 4):
    boton = tk.Button(
        ven_principal,
        text= obtener_texto(i), 
        command=lambda i = i: abrir_ventana(i)
    )
    boton.pack(padx= 10, pady=10)

# Botón para cerrar la ventana principal, inicialmente deshabilitado
boton_cerrar_principal = tk.Button(
    ven_principal,
    text="Cerrar principal",
    command=ven_principal.destroy,
    state=tk.DISABLED
)
boton_cerrar_principal.pack(padx=10, pady=10)

ven_principal.mainloop()