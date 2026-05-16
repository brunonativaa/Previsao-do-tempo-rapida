# 🌦️ Project Previsão Rápida do Tempo

> **Assistente Meteorológico Pessoal:** Um script Python que monitora o clima em tempo real e te avisa via SMS se você vai precisar de um guarda-chuva ou se pode curtir o sol.

---

## 📝 Descrição
O programa realiza requisições HTTP para a API do **OpenWeatherMap**, processando dados em formato JSON. Ele analisa a descrição do tempo e, caso a previsão indique "chuva", utiliza a API do **Telegram** para disparar um SMS automático para o seu celular. Se o dia estiver limpo, ele apenas te deseja um bom dia!



## 🚀 Funcionalidades
- **Consulta Automatizada:** Obtém dados climáticos precisos via linha de comando.
- **Exibição no Terminal:** Interface limpa mostrando as condições para hoje e os próximos dias.
- **Análise Lógica Dinâmica:** Identifica palavras-chave (chuva, sol, nuvens) para personalizar a resposta.
- **Integração direta com bot do Telegram:** (substituindo a antiga integração via Twilio)..
- **Execução manual via terminal local.** 

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Descrição |
| :--- | :--- |
| **Python 3** | Linguagem principal do projeto. |
| **OpenWeatherMap API** | Fonte de dados meteorológicos globais. |
| **Interface: Telegram Bot API** | (via biblioteca python-telegram-bot ou similar) |
| **Versionamento:**| Git & GitHub  |
| **Requests** | Biblioteca para consumo de APIs (HTTP). |
| **JSON/Sys** | Módulos nativos para tratamento de dados e argumentos de sistema. |

## ⚙️ Como Executar

### 1. Instale as dependências Modo Local (Terminal / PC)
Certifique-se de ter o Python instalado e uma chave de API (Token) gerada pelo @BotFather no Telegram.

###  Configure as suas credenciais:

Para proteger credenciais sensíveis (como o Telegram Token e a Weather API Key), este projeto utiliza variáveis de ambiente via arquivo .env. Isso evita a exposição de chaves privadas em repositórios públicos como o GitHub.

Local : As chaves são armazenadas em um arquivo .env na raiz do projeto, que é ignorado pelo Git através do .gitignore.

Loading: A biblioteca python-dotenv carrega essas variáveis para o ambiente de execução do Python.

Access: O código utiliza o módulo os para ler os valores sem nunca exibi-los diretamente no código-fonte.



###  Execute o programa: 

No terminal, navegue até a pasta onde os arquivos estão salvos e execute o script. Lembre-se de passar o nome da cidade e a sigla do país. Dica: Coloque o nome da localidade entre aspas duplas caso ela possua espaços e vírgulas para que o terminal leia o argumento corretamente:

exemplo ->  python quickWeather.py "São Paulo, BR"
Aguarde alguns segundos e o alerta com a previsão chegará diretamente no seu celular!

TODOS RECURSO SÃO GRATUITOS.

link  https://openweathermap.org/


# 🌤️ WeatherQuicker Bot


Um utilitário em Python que consome dados de previsão do tempo em tempo real, aplica regras de negócio customizadas para a minha rotina diária e dispara alertas formatados diretamente no meu Telegram.

## 🚀 Evolução do Projeto (Da Máquina Local para a Nuvem)

O projeto nasceu originalmente como um script procedural executado via terminal (`sys.argv`), utilizando arquivos locais (`.env`) para gerenciar credenciais. 

Para alcançar automação total sem depender do meu computador ligado, refatorei a aplicação para uma **Arquitetura Serverless (Orientada a Eventos)** implantada no **Google Cloud Platform (GCP)**.

### 🏗️ Arquitetura Atual
* **Python 3.11 & Functions Framework:** Código envelopado e otimizado para microsserviços.
* **Google Cloud Functions (2nd Gen):** Execução em contêineres isolados de forma sob demanda (Serverless).
* **Google Cloud Scheduler:** Cronjob em nuvem configurado para acordar a função diariamente às **07:00 AM** (Horário de Brasília).
* **Segurança:** Removido o uso de arquivos `.env` locais. Todas as credenciais sensíveis (`TELEGRAM_TOKEN`, `WEATHER_API_KEY`) são injetadas de forma segura diretamente na infraestrutura do GCP através de variáveis de ambiente do contêiner.

## 🛠️ Tecnologias Utilizadas
* [Python 3.11](https://www.python.org/)
* [Requests](https://requests.readthedocs.io/) (Consumo de APIs HTTP)
* [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-python) (GCP Adapter)
* [OpenWeatherMap API](https://openweathermap.org/) (Dados climáticos)
* [Telegram Bot API](https://core.telegram.org/bots/api) (Interface de entrega)

## 💡 Lógica Dinâmica Implementada
O bot não entrega apenas dados frios, ele analisa as métricas brasileiras (Celsius e Umidade) e gera conselhos práticos para o meu dia a dia:
* **Chuva detectada:** Alerta para evitar mexer com drywall/pintura e pegar o guarda-chuva.
* **Temperatura > 28°C:** Alerta focado em hidratação pesada para os treinos.
* **Umidade > 80%:** Dica de organização doméstica (circular o ar nos guarda-roupas).

---
*Projeto desenvolvido para fins de aprendizado prático em consumo de APIs, refatoração de código e Cloud Computing.*



| **📅 Roadmap de Desenvolvimento**|

[x] Migração de Twilio para Telegram API.

[ ] Implementação de Webhooks/Polling avançado.

[x] Deploy e hospedagem 24/7 no Google Cloud Platform (Compute Engine).