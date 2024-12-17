# Este es mi primer bot de Telegram

Este repositorio contiene el código para crear un bot utilizando la biblioteca **Telebot** de Python. El bot ofrece la posibilidad de interactuar con usuarios a través de comandos, botones interactivos y enlaces a canciones de diferentes géneros musicales.

## Configuración

1. Clona este repositorio en tu máquina local.
- git clone https://github.com/pabloesteban2712/Telegram-Music-Bot.git

2. Instala las dependencias necesarias con el siguiente comando:
- pip install -r requirements.txt

3. Crea un bot en Telegram a través de BotFather. Sigue los pasos proporcionados por BotFather para obtener el token de tu bot.

4. Abre el archivo main.py y reemplaza "TU_TOKEN" con el token que te dio BotFather.
TOKEN = 'TU_TOKEN'

5. Ejecuta el bot desde la terminal con:
python main.py

6. Funcionalidades
El bot ofrece las siguientes funcionalidades:
- Comando /start: Responde con un mensaje de bienvenida.
- Comando /help: Responde con información sobre cómo usar el bot.
- Comando /menu: Presenta botones interactivos para elegir si deseas escuchar música.

7. Botones interactivos:
- Elige entre diferentes géneros musicales (Rap, Pop, Electrónica, RnB, Reggaeton, Rock).
- Una vez que selecciones un género, el bot te enviará un enlace aleatorio a una canción de ese género.
- Si no deseas escuchar música, el bot te lo preguntará y responderá amablemente.
