# quickWeather.py – Exibe a previsão do tempo para uma localidade obtida na linha de comando e envia um SMS.
import datetime
import requests # Request muito importante para consumo de APIs
import sys # usada aqui para ler argumentos passadas pelo terminal (sys.argv)
from dotenv import load_dotenv # Biblioteca para carregar variáveis de ambiente de um arquivo .env
import os # Biblioteca para acessar variáveis de ambiente do sistema operacional

load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
weather_key = os.getenv('WEATHER_API_KEY')
# --- FASE 1: ENTRADA DE DADOS ---
# sys.argv armazena o nome do script e os argumentos passados no console.
# Se você digitar: python quickWeather.py "Itapecerica da Serra"
# sys.argv[0] é o nome do script, sys.argv[1:] é a cidade.
if len(sys.argv) < 2: 
    print("Usage: quickWeather.py  Itapecerica da Serra, BR")
    sys.exit()

location = ' '.join(sys.argv[1:]).strip()


# marca tempo de consulta

agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")


# --- FASE 2: COMUNICAÇÃO COM API (OPENWEATHER) ---
# Montamos a URL dinâmica usando f-strings para injetar a cidade e a chave enviando um pedido ao servidor
# Adicionado &units=metric para trazer em Celsius

url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={weather_key}&lang=pt_br&units=metric'
 
 

try:  # Verifica se o servidor respondeu com sucesso ou erro, # Se der erro 404 ou 500, ele pula para o 'except'
    response = requests.get(url)
    response.raise_for_status()
except Exception as exc:
    print(f"Houve um problema com o download: {exc}")   
    sys.exit() 

# --- FASE 3: TRANSFORMAÇÃO DE DADOS ---
# O response.text é apenas uma string longa. json.loads() transforma isso 
# em um DICIONÁRIO Python, permitindo acessar dados por chaves: weatherData['list']
weatherData = response.json()

# A API retorna uma lista de previsões (de 3 em 3 horas).
# w[0] = Agora, w[1] = Próximo período, w[2] = Depois.
w = weatherData['list']

# --- FASE 4: LÓGICA DE NEGÓCIO (ANÁLISE DO TEMPO) ---
# Guarda a descrição de hoje em minúsculas para facilitar a verificação 
dados_atuais  = w[0]
main = dados_atuais['main']
temp = round(main['temp'] , 1)
feels_like = round(main['feels_like'] , 1)
humidity = main['humidity']
descricao_hoje = dados_atuais['weather'][0]['description'].lower()


#Logica Dinâmica
conselho = "Tenha um ótimo dia de estudos! 💻"
if "chuva" in descricao_hoje or "rain" in descricao_hoje:
    conselho = "⛈️ Pegue o guarda-chuva! Evite mexer com drywall ou pintura hoje."
elif temp > 28:
    conselho = "🔥 Hidratação redobrada no treino hoje!"
elif humidity > 80:
    conselho = "🧴 Umidade alta: Abra as portas dos guarda-roupas periodicamente para circular o ar."    




# Impressão no Terminal (Para conferência rápida)
print(f"\n--- RELATÓRIO TERMINAL: {location.upper()} ({agora}) ---")
print(f"Agora: {descricao_hoje.title()} | {temp}°C")
print(f"Próximas horas: {w[1]['weather'][0]['description']} -> {w[2]['weather'][0]['description']}")


def enviar_telegram(mensagem):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_ID')
    url_base = f"https://api.telegram.org/bot{token}/sendMessage"

    params = {
        'chat_id': chat_id,
        'text': mensagem,
        'parse_mode': 'Markdown' # Permite usar negrito e emojis melhor
    }
    
    resp = requests.post(url_base, data=params)
    return resp



# 1. Criamos a STRING com o conteúdo (Corpo da mensagem)
corpo_da_mensagem = (
    f"*🌤️ Previsão {location}*\n"
    f"_{agora}_\n\n"
    f"🌡️ *Temp:* {temp}°C (Sente {feels_like}°C)\n"
    f"💧 *Umidade:* {humidity}%\n"
    f"📝 *Condição:* {descricao_hoje.title()}\n\n"
    f"💡 *Dica:* {conselho}"
)

#


envio = enviar_telegram(corpo_da_mensagem)

if envio.status_code == 200:
    print("Mensagem enviada com sucesso para o Telegram!")
else:
    print(f"Erro ao enviar: {envio.status_code} - {envio.text}")