# Avalie músicas
Site voltado para a avaliação de músicas
## Funcionalidades
- Adicionar música, autor, nota e avaliação pessoal
- Deletar posts
- Editar posts
## Como executar
1. Acesse a pasta do projeto pelo terminal
cd src/avalie-musicas
2. Inicialize o ambiente virtual
*Linux*
```bash
python3 -m venv .venv
```
*Windows*
```bash
py -3 -m venv .venv
```
3. Ative o ambiente virtual
*Linux*
```bash
source .venv/Scripts/activate
```
*Windows*
```bash
.venv\Scripts\activate
```
4. Baixe as dependências
```bash
pip install -r requirements.txt
```
5. Execute a aplicação
```bash
flask --app flaskr.app run --debug
```
A aplicação estará disponível em:
```bash
http://127.0.0.1:5000
```