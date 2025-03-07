# Usar a imagem base do Python
FROM python:3.12

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar o Poetry globalmente
RUN pip install --no-cache-dir poetry

# Copiar apenas os arquivos do Poetry primeiro (para otimizar cache)
COPY pyproject.toml poetry.lock* ./

# Instalar dependências do projeto
RUN poetry install --no-root --no-interaction --no-ansi

# Copiar o restante dos arquivos do projeto
COPY . .

# Comando para rodar a aplicação
CMD ["poetry", "run", "python", "mitmproxy.py"]
