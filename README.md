# CRM-IA para Consultório de Psicologia

Este projeto demonstra um fluxo de CRM com IA para agendamento, lembretes e integração com WhatsApp, Google Sheets e modelos de linguagem.

## Estrutura
- `run.py`: Inicializa o servidor Flask
- `app/`: Contém os módulos da aplicação
  - `routes.py`: Define as rotas da API
  - `whatsapp.py`: Integração com Twilio WhatsApp
  - `sheets.py`: Integração com Google Sheets
  - `ia.py`: Comunicação com modelo de linguagem
  - `scheduler.py`: Agendamentos e lembretes automáticos
- `.env`: Variáveis de ambiente (tokens, chaves, etc)

## Como rodar localmente

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone https://github.com/seu-usuario/CRM-IA-Broco.git
   cd CRM-IA-Broco
   ```
