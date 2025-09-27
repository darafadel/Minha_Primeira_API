from fastapi import FastAPI
import uvicorn

app = FastAPI(title="API de Séries de TV", version="1.0.0")

# Dataset completo - 50 séries de TV
series_db = [
    {"id": 1, "nome": "Breaking Bad", "ano": 2008, "genero": "Drama", "temporadas": 5, "nota": 9.5},
    {"id": 2, "nome": "Stranger Things", "ano": 2016, "genero": "Ficção", "temporadas": 4, "nota": 8.7},
    {"id": 3, "nome": "The Office", "ano": 2005, "genero": "Comédia", "temporadas": 9, "nota": 8.9},
    {"id": 4, "nome": "Game of Thrones", "ano": 2011, "genero": "Fantasia", "temporadas": 8, "nota": 9.3},
    {"id": 5, "nome": "Friends", "ano": 1994, "genero": "Comédia", "temporadas": 10, "nota": 8.9},
    {"id": 6, "nome": "The Walking Dead", "ano": 2010, "genero": "Terror", "temporadas": 11, "nota": 8.2},
    {"id": 7, "nome": "Lost", "ano": 2004, "genero": "Mistério", "temporadas": 6, "nota": 8.3},
    {"id": 8, "nome": "House of Cards", "ano": 2013, "genero": "Drama", "temporadas": 6, "nota": 8.7},
    {"id": 9, "nome": "Sherlock", "ano": 2010, "genero": "Mistério", "temporadas": 4, "nota": 9.1},
    {"id": 10, "nome": "The Crown", "ano": 2016, "genero": "Drama", "temporadas": 6, "nota": 8.6},
    {"id": 11, "nome": "Narcos", "ano": 2015, "genero": "Crime", "temporadas": 3, "nota": 8.8},
    {"id": 12, "nome": "Black Mirror", "ano": 2011, "genero": "Ficção", "temporadas": 6, "nota": 8.8},
    {"id": 13, "nome": "Westworld", "ano": 2016, "genero": "Ficção", "temporadas": 4, "nota": 8.6},
    {"id": 14, "nome": "Better Call Saul", "ano": 2015, "genero": "Drama", "temporadas": 6, "nota": 8.9},
    {"id": 15, "nome": "The Mandalorian", "ano": 2019, "genero": "Ficção", "temporadas": 3, "nota": 8.7},
    {"id": 16, "nome": "Ozark", "ano": 2017, "genero": "Crime", "temporadas": 4, "nota": 8.4},
    {"id": 17, "nome": "Peaky Blinders", "ano": 2013, "genero": "Crime", "temporadas": 6, "nota": 8.8},
    {"id": 18, "nome": "The Witcher", "ano": 2019, "genero": "Fantasia", "temporadas": 3, "nota": 8.2},
    {"id": 19, "nome": "La Casa de Papel", "ano": 2017, "genero": "Crime", "temporadas": 5, "nota": 8.3},
    {"id": 20, "nome": "Squid Game", "ano": 2021, "genero": "Drama", "temporadas": 1, "nota": 8.0},
    {"id": 21, "nome": "The Boys", "ano": 2019, "genero": "Ação", "temporadas": 4, "nota": 8.7},
    {"id": 22, "nome": "Euphoria", "ano": 2019, "genero": "Drama", "temporadas": 2, "nota": 8.4},
    {"id": 23, "nome": "Succession", "ano": 2018, "genero": "Drama", "temporadas": 4, "nota": 8.8},
    {"id": 24, "nome": "The Umbrella Academy", "ano": 2019, "genero": "Ficção", "temporadas": 4, "nota": 7.9},
    {"id": 25, "nome": "Bridgerton", "ano": 2020, "genero": "Romance", "temporadas": 3, "nota": 7.3},
    {"id": 26, "nome": "Ted Lasso", "ano": 2020, "genero": "Comédia", "temporadas": 3, "nota": 8.8},
    {"id": 27, "nome": "The Queen's Gambit", "ano": 2020, "genero": "Drama", "temporadas": 1, "nota": 8.5},
    {"id": 28, "nome": "Cobra Kai", "ano": 2018, "genero": "Ação", "temporadas": 6, "nota": 8.5},
    {"id": 29, "nome": "Wednesday", "ano": 2022, "genero": "Mistério", "temporadas": 1, "nota": 8.1},
    {"id": 30, "nome": "The Bear", "ano": 2022, "genero": "Comédia", "temporadas": 3, "nota": 8.6},
    {"id": 31, "nome": "Yellowstone", "ano": 2018, "genero": "Drama", "temporadas": 5, "nota": 8.7},
    {"id": 32, "nome": "Mare of Easttown", "ano": 2021, "genero": "Crime", "temporadas": 1, "nota": 8.4},
    {"id": 33, "nome": "Loki", "ano": 2021, "genero": "Ficção", "temporadas": 2, "nota": 8.2},
    {"id": 34, "nome": "WandaVision", "ano": 2021, "genero": "Ficção", "temporadas": 1, "nota": 7.9},
    {"id": 35, "nome": "The Falcon and the Winter Soldier", "ano": 2021, "genero": "Ação", "temporadas": 1, "nota": 7.2},
    {"id": 36, "nome": "Lupin", "ano": 2021, "genero": "Crime", "temporadas": 3, "nota": 7.5},
    {"id": 37, "nome": "Emily in Paris", "ano": 2020, "genero": "Romance", "temporadas": 4, "nota": 6.8},
    {"id": 38, "nome": "The Good Place", "ano": 2016, "genero": "Comédia", "temporadas": 4, "nota": 8.2},
    {"id": 39, "nome": "Chernobyl", "ano": 2019, "genero": "Drama", "temporadas": 1, "nota": 9.4},
    {"id": 40, "nome": "Band of Brothers", "ano": 2001, "genero": "Guerra", "temporadas": 1, "nota": 9.4},
    {"id": 41, "nome": "True Detective", "ano": 2014, "genero": "Crime", "temporadas": 4, "nota": 8.9},
    {"id": 42, "nome": "Fargo", "ano": 2014, "genero": "Crime", "temporadas": 5, "nota": 8.9},
    {"id": 43, "nome": "The Sopranos", "ano": 1999, "genero": "Crime", "temporadas": 6, "nota": 9.2},
    {"id": 44, "nome": "The Wire", "ano": 2002, "genero": "Crime", "temporadas": 5, "nota": 9.3},
    {"id": 45, "nome": "Mad Men", "ano": 2007, "genero": "Drama", "temporadas": 7, "nota": 8.6},
    {"id": 46, "nome": "Dexter", "ano": 2006, "genero": "Crime", "temporadas": 8, "nota": 8.7},
    {"id": 47, "nome": "How I Met Your Mother", "ano": 2005, "genero": "Comédia", "temporadas": 9, "nota": 8.3},
    {"id": 48, "nome": "Prison Break", "ano": 2005, "genero": "Drama", "temporadas": 5, "nota": 8.3},
    {"id": 49, "nome": "Suits", "ano": 2011, "genero": "Drama", "temporadas": 9, "nota": 8.5},
    {"id": 50, "nome": "Vikings", "ano": 2013, "genero": "Ação", "temporadas": 6, "nota": 8.5}
]

@app.get("/")
def home():
    """Endpoint básico com informações da API"""
    return {
        "projeto": "API de Séries de TV",
        "autor": "Seu Nome Aqui",  # MUDE PARA SEU NOME
        "descricao": "API para consultar informações sobre séries de televisão",
        "total_registros": len(series_db)
    }

@app.get("/series")
def listar_todas_series():
    """Endpoint básico - retorna todas as séries"""
    return {
        "total": len(series_db),
        "series": series_db
    }

@app.get("/series/{serie_id}")
def buscar_serie_por_id(serie_id: int):
    """Endpoint intermediário - busca série por ID"""
    for serie in series_db:
        if serie["id"] == serie_id:
            return serie
    
    return {"erro": f"Série com ID {serie_id} não encontrada"}

@app.get("/genero/{genero}")
def buscar_por_genero(genero: str):
    """Endpoint intermediário - filtra séries por gênero"""
    series_filtradas = []
    for serie in series_db:
        if serie["genero"].lower() == genero.lower():
            series_filtradas.append(serie)
    
    return {
        "genero": genero,
        "total": len(series_filtradas),
        "series": series_filtradas
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
