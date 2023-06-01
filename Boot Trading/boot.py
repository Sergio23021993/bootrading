import random

def obtener_recomendacion(estrategias):
    # Aquí puedes implementar la lógica para generar recomendaciones basadas en las estrategias ingresadas por el usuario
    opciones = ['Comprar', 'Vender', 'Mantener']
    recomendacion = random.choice(opciones)
    return recomendacion

def interactuar_con_usuario():
    print("¡Bienvenido al bot de trading!")
    estrategias = []
    while True:
        pregunta = input("Ingresa una estrategia de análisis (o escribe 'listo' para obtener una recomendación): ")
        if pregunta.lower() == 'listo':
            if estrategias:
                recomendacion = obtener_recomendacion(estrategias)
                print("Recomendación:", recomendacion)
                print()
            else:
                print("No se han ingresado estrategias. Por favor, ingresa al menos una estrategia.")
        else:
            estrategias.append(pregunta)
            print("Estrategia agregada correctamente.")

interactuar_con_usuario()
