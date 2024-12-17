import telebot
from telebot import types
import random  # Selecciona enlaces aleatorios

# Conexion con el BOT
TOKEN = 'Tu_token'  # Tu clave unica
bot = telebot.TeleBot(TOKEN)

# Lista de enlaces con música
music_links = {
    "Rap": [
        "https://open.spotify.com/track/6qj71v5MNedTO6UvSzGTr6",  # Travis Scott - HIGHEST IN THE ROOM
        "https://www.youtube.com/watch?v=tvTRZJ-4EyI&pp=ygUVa2VuZHJpY2sgbGFtYXIgaHVtYmxl",  # Kendrick Lamar - HUMBLE.
        "https://open.spotify.com/track/0F0MA0ns8oXwGw66B2BSXm",  # Eminem - Lose Yourself
        "https://soundcloud.com/trapnation/travis-scott-sicko-mode",  # Travis Scott - SICKO MODE
        "https://youtube.com/watch?v=H5v3kku4y6Q",  # Drake - God's Plan
        "https://open.spotify.com/track/7wGoVu4Dady5GV0Sv4UIsx",  # J. Cole - MIDDLE CHILD
        "https://youtube.com/watch?v=bm8pRKUw1X8",  # NF - The Search
    ],
    "Pop": [
        "https://open.spotify.com/track/4h9wh7iOZ0GGn8QVp4RAOB",  # Dua Lipa - Levitating
        "https://youtube.com/watch?v=pRpeEdMmmQ0",  # Shakira - Waka Waka
        "https://open.spotify.com/track/5CtI0qwDJkDQGwXD1H1cLb",  # Lady Gaga - Poker Face
        "https://soundcloud.com/billieeilish/billie-eilish-bad-guy",  # Billie Eilish - Bad Guy
        "https://youtube.com/watch?v=kJQP7kiw5Fk",  # Luis Fonsi - Despacito
        "https://open.spotify.com/track/0RiRZpuVRbi7oqRdSMwhQY",  # Taylor Swift - Shake It Off
        "https://youtube.com/watch?v=1TsVjvEkc4s",  # Katy Perry - Roar
    ],
    "Electronica": [
        "https://open.spotify.com/track/2Z8WuEywRWYTKe1NybPQEW",  # Alan Walker - Faded
        "https://youtube.com/watch?v=YqeW9_5kURI",  # Major Lazer - Lean On
        "https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH",  # Martin Garrix - Animals
        "https://soundcloud.com/odesza/say-my-name",  # ODESZA - Say My Name
        "https://youtube.com/watch?v=f5OMhBuWK7Y",  # The Chainsmokers - Closer
        "https://open.spotify.com/track/5UVzXkeRX8k7bbCZD788K4",  # Zedd - Clarity
        "https://youtube.com/watch?v=5NV6Rdv1a3I",  # Daft Punk - Get Lucky
    ],
    "Rnb": [
        "https://open.spotify.com/track/6l8GvAyoUZwWDgF1e4822w",  # The Weeknd - Blinding Lights
        "https://youtube.com/watch?v=JGwWNGJdvx8",  # Ed Sheeran - Shape of You
        "https://open.spotify.com/track/7e89621JPkKaeDSTQ3avtg",  # SZA - Good Days
        "https://soundcloud.com/jheneaiko/jhene-aiko-spotless-mind",  # Jhene Aiko - Spotless Mind
        "https://youtube.com/watch?v=3tmd-ClpJxA",  # Khalid - Talk
        "https://open.spotify.com/track/2aibwvKHTE2MO1v3m4E8eB",  # Beyoncé - Halo
        "https://youtube.com/watch?v=yR2tlfMSais",  # Alicia Keys - If I Ain't Got You
    ],
    "Reggaeton": [
        "https://open.spotify.com/track/7hV9UizcQTP4pPwIMVqI4v",  # Bad Bunny - Titi Me Preguntó
        "https://youtube.com/watch?v=kJQP7kiw5Fk",  # Luis Fonsi - Despacito
        "https://open.spotify.com/track/4w8niZpiMy6qz1mntFA5uM",  # Daddy Yankee - Con Calma
        "https://youtube.com/watch?v=U7pSvkRFFz4",  # J Balvin - Mi Gente
        "https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb",  # Ozuna - Baila Baila Baila
        "https://youtube.com/watch?v=OSUxrSe5GbI",  # Karol G - Provenza
        "https://youtube.com/watch?v=E1kcqV_NK7U",  # Rauw Alejandro - Todo de Ti
    ],
    "Rock": [
        "https://open.spotify.com/track/3gdewACMIVMEWVbyb8O9sY",  # Nirvana - Smells Like Teen Spirit
        "https://youtube.com/watch?v=vx2u5uUu3DE",  # Linkin Park - Numb
        "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK",  # Green Day - Boulevard of Broken Dreams
        "https://youtube.com/watch?v=tbNlMtqrYS0",  # Queen - Bohemian Rhapsody
        "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf",  # Imagine Dragons - Believer
        "https://youtube.com/watch?v=hTWKbfoikeg",  # Foo Fighters - Everlong
        "https://open.spotify.com/track/3d9DChrdc6BOeFsbrZ3Is0",  # Red Hot Chili Peppers - Californication
    ]
}

# Creamos comandos simples
@bot.message_handler(commands=['hola'])  # Es un gestor de mensajes, escucha cuando un usuario envia el comando /start
def send_welcome(message):  # Se ejecuta cuando presionamos /start
    bot.reply_to(message, 'Hola! Soy tu bot! Dime lo que necesites!')

@bot.message_handler(commands=['ayuda'])
def send_help(message):  # Igual que la funcion anterior. Se ejecuta cuando usamos /help
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos como /hola, /ayuda, /menu.')

# Comando con botones interactivos!
@bot.message_handler(commands=['menu'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Botones
    btn_musica = types.InlineKeyboardButton('Me apetece escuchar musica', callback_data='estado_musica')
    btn_no = types.InlineKeyboardButton('No, hoy no me apetece', callback_data='estado_no')

        # Agrega botones
    markup.add(btn_musica,btn_no)

     # Enviar mensaje con el uso de botones
    bot.send_message(message.chat.id, "Hola! ¿Qué te apetece hoy? ¿Quieres escuchar música?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'estado_musica':
        # Mostrar botones con categorías de música
        markup = types.InlineKeyboardMarkup(row_width=2)
        for category in music_links.keys():
            markup.add(types.InlineKeyboardButton(category, callback_data=f'genre_{category}'))
        bot.send_message(call.message.chat.id, 'Elige un género:', reply_markup=markup)
    elif call.data.startswith('genre_'):
        # Obtener categoría seleccionada
        genre = call.data.split('_')[1]
        if genre in music_links:
            # Elegir enlace aleatorio de esa categoría
            random_link = random.choice(music_links[genre])
            genre_messages = {
                "Rap": "🔥 Aquí tienes una dosis de rap para encender tu día:",
                "Pop": "🎉 ¡Es hora de bailar al ritmo del pop! Aquí va una canción:",
                "Electronica": "🔊 Sumérgete en las vibraciones electrónicas con este tema:",
                "Rnb": "🎵 Relájate con este increíble tema de RnB:",
                "Reggaeton": "💃 Dale ritmo a tu día con este reggaetón:",
                "Rock": "🤘 Aquí tienes un clásico de rock para animarte:"
            }
            # Enviar mensaje junto con el enlace
            message = genre_messages.get(genre, "🎶 Disfruta de esta canción:")
            bot.send_message(call.message.chat.id, f'🎶 Aquí tienes algo de {genre}: {random_link}') # Aqui hace un random entre el genero elegido
        else:
            bot.send_message(call.message.chat.id, '¡Ups! No tengo música para esa categoría.')
    elif call.data == 'estado_no':
        bot.send_message(call.message.chat.id, 'De acuerdo, ¡tal vez otro día! 🙂')

if __name__ == "__main__":
    bot.polling(non_stop=True)