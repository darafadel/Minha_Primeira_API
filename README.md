# Minha_Primeira_API

# 📺 API de Séries de TV

## Descrição
API desenvolvida com FastAPI para consultar informações sobre séries de televisão populares.

## Autor
[Seu Nome Completo]  <!-- MUDE AQUI -->

## Dataset
Base de dados com 50 séries populares, incluindo:
- Nome da série
- Ano de lançamento  
- Gênero
- Número de temporadas
- Nota de avaliação

## Endpoints Implementados

### 1. Informações da API (Básico)
- **GET /** - Retorna informações sobre a API

### 2. Listar todas as séries (Básico)
- **GET /series** - Retorna todas as 50 séries cadastradas

### 3. Buscar por ID (Intermediário)
- **GET /series/{id}** - Busca uma série específica pelo ID
- Exemplo: `/series/1` retorna "Breaking Bad"

### 4. Buscar por gênero (Intermediário)  
- **GET /genero/{genero}** - Filtra séries por gênero
- Exemplo: `/genero/drama` retorna todas as séries de drama

## Como executar
```bash
pip install -r requirements.txt
python main.py
