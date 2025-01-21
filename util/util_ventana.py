

def centrar_ventana(ventana, app_ancho, app_alto):
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular la posición x e y para centrar la ventana
    x = (ancho_pantalla // 2) - (app_ancho // 2)
    y = (alto_pantalla // 2) - (app_alto // 2)

    # Establecer la geometría de la ventana
    return ventana.geometry(f'{app_ancho}x{app_alto}+{x}+{y}')
