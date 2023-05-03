import turtle
import pandas

screen = turtle.Screen()
# screen.bgcolor("black")
# screen.setup(700, 700)
imagen = "blank_states_img.gif"
screen.title("Adivinar provincias")
screen.addshape(imagen)
turtle.shape(imagen)
escritor = turtle.Turtle()
escritor.hideturtle()
total_de_estados = 50

# def get_mouse_click_coor(x, y): # Nos va a imprimir los datos de X e Y que pasemos
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) # Funciona con la funcion anteriormente creada, aca pasa los datos de X e Y
#
estados_adivinados = []
data_estados = pandas.read_csv("50_states.csv")
todos_los_estados = data_estados.state.to_list()
puntuacion_max = len(todos_los_estados)
puntuacion_jugador = 0
print(todos_los_estados)
estados_faltantes = []


while puntuacion_jugador < 50:
    respuesta_de_estado = screen.textinput(title=f"Puntuacion {puntuacion_jugador}/{puntuacion_max}", prompt="Otro nombre de estado?").title()
    if respuesta_de_estado.lower() == "exit":
        for estado in todos_los_estados:
            if estado not in estados_adivinados:
                estados_faltantes.append(estado)
        data_estados_faltantes = {
            "Estados faltantes": estados_faltantes,
        }
        data_estados_faltantes_dataframe = pandas.DataFrame(data_estados_faltantes)
        data_estados_faltantes_dataframe.to_csv("datos_estados_faltantes.csv")
        break
    if respuesta_de_estado in todos_los_estados and not respuesta_de_estado in estados_adivinados:
        estados_adivinados.append(respuesta_de_estado)
        puntuacion_jugador += 1
        check = data_estados[data_estados.state == respuesta_de_estado]
        escritor.penup()
        escritor.goto(int(check.x), int(check.y))
        escritor.write(respuesta_de_estado)
    if puntuacion_jugador == 50:
        escritor.goto(-50, 250)
        escritor.write("Ganaste!", font=("Arial", 33, "normal"))



# turtle.mainloop()  # La pantalla se queda abierta aunque nuestro codigo haya terminado de ejecutarse
# # screen.exitonclick()
