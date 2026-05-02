# 🌦️ Project Previsão Rápida do Tempo

> **Assistente Meteorológico Pessoal:** Um script Python que monitora o clima em tempo real e te avisa via SMS se você vai precisar de um guarda-chuva ou se pode curtir o sol.

---

## 📝 Descrição
O programa realiza requisições HTTP para a API do **OpenWeatherMap**, processando dados em formato JSON. Ele analisa a descrição do tempo e, caso a previsão indique "chuva", utiliza a API do **Telegram** para disparar um SMS automático para o seu celular. Se o dia estiver limpo, ele apenas te deseja um bom dia!

![SMS Recebido](img/Screenshot%202026-05-02%20150947.png)
![Previsão do Tempo](img/Screenshot%202026-05-02%20151225.png)

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

### 1. Instale as dependências
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


| **📅 Roadmap de Desenvolvimento**|

[x] Migração de Twilio para Telegram API.

[ ] Implementação de Webhooks/Polling avançado.

[ ] Deploy e hospedagem 24/7 no Google Cloud Platform (Compute Engine).