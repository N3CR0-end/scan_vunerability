# Scanner de Vulnerabilidades

Um scanner de vulnerabilidades simples desenvolvido com Flask para detectar possíveis vulnerabilidades em websites. Este projeto é destinado a fins educacionais e para ajudar a compreender os conceitos básicos de um scanner de vulnerabilidades.

## Funcionalidades

- Iniciar um Scan: Permite iniciar uma varredura em um site fornecido.
- **Verificar Status do Scan**: Consulta o status de um scan específico.
- **Obter Resultados do Scan**: Recupera os resultados da varredura concluída.

## Tecnologias Utilizadas

- Python 3.x
- **Flask**: Framework web para criar a API.
- **Requests**: Biblioteca para realizar requisições HTTP.

## Instalação

1. Clone o Repositório
   git clone https://github.com/usuario/nome-do-repositorio.git
Navegue até o Diretório do Projeto


Copiar código
cd nome-do-repositorio
Crie e Ative um Ambiente Virtual


Copiar código
python -m venv venv
source venv/bin/activate  # Para Windows: venv\Scripts\activate
Instale as Dependências


Copiar código
pip install -r requirements.txt
Configuração
Crie um Arquivo .env (opcional, se necessário para variáveis de ambiente).

Execute a Aplicação


Copiar código
set FLASK_APP=app  # Para Windows
flask run
ou
Copiar código
export FLASK_APP=app  # Para macOS/Linux
flask run
A aplicação estará disponível em http://127.0.0.1:5000.

Testando a API com Postman
Iniciar um Scan:

Método: POST
URL: http://127.0.0.1:5000/api/scan/
Body:
json
Copiar código
{
  "url": "http://example.com"
}
Verificar Status do Scan:

Método: GET
URL: http://127.0.0.1:5000/api/scan/<scan_id>/status
Obter Resultados do Scan:

Método: GET
URL: http://127.0.0.1:5000/api/scan/<scan_id>/results
Estrutura do Projeto
markdown
Copiar código
ScannerDeVulnerabilidades/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── scanner.py
│   ├── models.py
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── README.md
Contribuição
Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie pull requests com melhorias ou correções.

Licença
Este projeto é livre para modificações.

### Notas Adicionais