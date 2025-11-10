import pandas as pd
import numpy as np


df = pd.read_csv("StudentsPerformance.csv")


print("Pré-visualização do dataset:\n", df.head(), "\n")

# Cria colunas derivadas
df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
df["performance_level"] = pd.cut(
    df["average_score"],
    bins=[0, 60, 80, 100],
    labels=["baixo", "médio", "alto"],
    include_lowest=True
)


colunas = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course",
    "math score",
    "reading score",
    "writing score",
    "average_score",
    "performance_level"
]


def resumo_coluna(col):
    serie = df[col]
    tipo = str(serie.dtype)
    distintos = serie.nunique()
    validos = serie.unique()[:10]  # mostra até 10 exemplos
    moda = serie.mode().iloc[0] if not serie.mode().empty else None


    if pd.api.types.is_numeric_dtype(serie):
        minimo = serie.min()
        maximo = serie.max()
        media = serie.mean()
        mediana = serie.median()
        desvio = serie.std()
    else:
        minimo = maximo = media = mediana = desvio = None

    return {
        "coluna": col,
        "tipo_dado": tipo,
        "valores_validos_exemplo": validos,
        "valores_distintos": distintos,
        "minimo": minimo,
        "maximo": maximo,
        "moda": moda,
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio
    }


resumo = pd.DataFrame([resumo_coluna(c) for c in colunas])


pd.set_option("display.max_columns", None)
print(resumo)

# Salva os resultados num arquivo CSV
resumo.to_csv("resumo_estatistico.csv", index=False)
print("\nResumo salvo em 'resumo_estatistico.csv'")
