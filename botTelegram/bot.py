import telebot

bot = telebot.TeleBot('7196861055:AAFN74XNc_oP7Qx3TYl6r0Ii57JjfIG6JC4')
recopilar_info = False
#posibles_escenarios = {"1" : "3", "2": "3","3": "4", "4" : "5", "5" : "3", "6" : "4", "7" : "4"}
posibles_escenarios = ["1","2","3","4","5","6","7"]
informacion_incidencia = []
preguntas_trafico = ["¿Cual es tu ubicacion actual?", "¿Describe la intensidad del trafico del 1 al 3?", "¿Cuanto tiempo llevas atorado en el trafico? (redondea a la hora mas cercana)"] 
preguntas_accidente = ["¿Donde te encuentras?", "¿Que tan grave es el accidente del 1 al 3?"]
preguntas_gasolina = ["¿Cuanto porcentaje de gasolina te queda del 1 al 100?", "¿Cuanto dinero tienes?", "¿Donde te encuentras?"]
preguntas_asalto = ["donde estas", "¿Calcula el daño de la unidad?"]
preguntas_clima = ["¿Donde te encuentras?", "¿Cual es el clima en el lugar?"]
preguntas_FallaMecanica = ["¿Donde te encuentras?", "¿Describe la falla? descuida la ayuda ya va en camino"]
preguntas_documentacion = ["¿Que documentacion te falta?"]
preguntas = []
preguntas = preguntas_trafico
i = 0
final = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global recopilar_info
    global i
    guardar_txt()
    informacion_incidencia.clear()
    recopilar_info = False
    i = 0

@bot.message_handler(func=lambda message : True)
def message(message):
    global i
    global recopilar_info
    global final
    global preguntas
    if not recopilar_info: #si aun no recopila informacion verifica si ya ingreso un valor del 1 al 7
        bot.reply_to(message, """Hola en que te puedo ayudar: 
                    1- Trafico
                    2- Accidente
                    3- Gasolina
                    4- Asaltos
                    5- Clima
                    6- Falla mecanica
                    7- Documentacion 
                    Porfavor seleccione la opcion deseada con un valor valido (1 - 7)""")
        for escenario in posibles_escenarios:
            if message.text == escenario:
                recopilar_info = True
                informacion_incidencia.append(message.text)
                
                if message.text == "1":
                        preguntas = preguntas_trafico
                if message.text == "2":
                    preguntas = preguntas_accidente
                if message.text == "3":
                    preguntas = preguntas_gasolina
                if message.text == "4":
                    preguntas = preguntas_asalto
                if message.text == "5":
                    preguntas = preguntas_clima
                if message.text == "6":
                    preguntas = preguntas_FallaMecanica
                if message.text == "7":
                    preguntas = preguntas_documentacion
    else:# se ejecutara cuando el usuario empieze a reporta informacion relevante
        informacion_incidencia.append(message.text)
        if not final:
            bot.reply_to(message, preguntas[i])
        if i<len(preguntas)-1: #solo se suma cuando no es la ultima
            i = i +1
        else:
            final = True

def guardar_txt():
    with open('informacion.txt', 'w') as file:
        for info in informacion_incidencia:
            file.write(info + '\n')

bot.polling()
