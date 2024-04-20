import telebot

bot = telebot.TeleBot('7196861055:AAFN74XNc_oP7Qx3TYl6r0Ii57JjfIG6JC4')
recopilar_info = False
#posibles_escenarios = {"1" : "3", "2": "3","3": "4", "4" : "5", "5" : "3", "6" : "4", "7" : "4"}
posibles_escenarios = ["1","2","3","4","5","6","7"]
informacion_incidencia = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    guardar_txt()
    posibles_escenarios.clear()
    recopilar_info = False

@bot.message_handler(func=lambda message : True)
def message(message):
    global recopilar_info
    if not recopilar_info: #si aun no recopila informacion verifica si ya ingreso un valor del 1 al 7
        bot.reply_to(message, """Hola en que te puedo ayudar: 
                    1- Trafico
                    2- Accidente
                    3- Gasolina
                    4- 5 Asaltos
                    5- Clima
                    6- Falla mecanica
                    7- Documentacion 
                    Porfavor seleccione la opcion deseada con un valor valido (1 - 7)""")
        for escenario in posibles_escenarios:
            if message.text == escenario:
                recopilar_info = True
                informacion_incidencia.append(message.text)
    else:
        informacion_incidencia.append(message.text)

def guardar_txt():
    with open('informacion.txt', 'w') as file:
        for info in informacion_incidencia:
            file.write(info + '\n')

bot.polling()
