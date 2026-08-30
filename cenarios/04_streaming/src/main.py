import csv

# ==========================================================
# 1. LEITURA DOS ARQUIVOS
# ==========================================================

# Lista de conteúdos
conteudos = []

with open("conteudos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        conteudos.append({
            "id": linha["id_conteudo"],
            "titulo": linha["titulo"],
            "genero": linha["genero"],
            "duracao": int(linha["duracao_min"])
        })


# Lista de visualizações
visualizacoes = []

with open("visualizacoes.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        visualizacoes.append({
            "id": linha["id_visualizacao"],
            "usuario": linha["usuario"],
            "id_conteudo": linha["id_conteudo"],
            "visualizacoes": int(linha["visualizacoes"]),
            "avaliacao": float(linha["avaliacao"])
        })


# ==========================================================
# 2. TUPLA
# ==========================================================

generos = (
    "Tecnologia",
    "Documentário",
    "Drama",
    "Ficção",
    "Comédia",
    "Suspense",
    "Aventura"
)


# ==========================================================
# 3. ESTRUTURA ANINHADA
# ==========================================================

# Junta as informações dos dois arquivos.
# Cada conteúdo possui suas informações e uma lista de
# visualizações relacionadas.

dados = {}

for conteudo in conteudos:
    dados[conteudo["id"]] = {
        "titulo": conteudo["titulo"],
        "genero": conteudo["genero"],
        "duracao": conteudo["duracao"],
        "visualizacoes": []
    }

for visualizacao in visualizacoes:
    id_conteudo = visualizacao["id_conteudo"]

    if id_conteudo in dados:
        dados[id_conteudo]["visualizacoes"].append({
            "usuario": visualizacao["usuario"],
            "quantidade": visualizacao["visualizacoes"],
            "avaliacao": visualizacao["avaliacao"]
        })


# ==========================================================
# 4. SET - ELIMINAR DADOS DUPLICADOS
# ==========================================================

# O arquivo possui alguns IDs de visualização repetidos.
ids_visualizacoes = [
    v["id"] for v in visualizacoes
]

ids_unicos = set(ids_visualizacoes)

duplicados = len(ids_visualizacoes) - len(ids_unicos)


# ==========================================================
# 5. SET - OPERAÇÃO DE INTERSEÇÃO
# ==========================================================

# Usuários que assistiram conteúdos de Drama
usuarios_drama = set()

for v in visualizacoes:
    if v["id_conteudo"] in ["C03", "C08"]:
        usuarios_drama.add(v["usuario"])


# Usuários que assistiram qualquer conteúdo
todos_usuarios = set(
    v["usuario"] for v in visualizacoes
)

# Interseção
usuarios_em_comum = usuarios_drama.intersection(todos_usuarios)


# ==========================================================
# 6. LIST COMPREHENSION - FILTRAGEM
# ==========================================================

# Conteúdos com duração superior a 100 minutos
conteudos_longos = [
    c for c in conteudos
    if c["duracao"] > 100
]


# ==========================================================
# 7. LIST COMPREHENSION - TRANSFORMAÇÃO
# ==========================================================

# Cria uma lista somente com os títulos dos conteúdos
titulos = [
    c["titulo"]
    for c in conteudos
]


# ==========================================================
# 8. DICT COMPREHENSION
# ==========================================================

# Cria um dicionário relacionando ID e título
id_para_titulo = {
    c["id"]: c["titulo"]
    for c in conteudos
}


# ==========================================================
# 9. FUNÇÃO 1 - TOTAL DE VISUALIZAÇÕES
# ==========================================================

def calcular_total_visualizacoes(lista):
    total = sum(
        v["visualizacoes"]
        for v in lista
    )

    return total


# ==========================================================
# 10. FUNÇÃO 2 - MÉDIA DAS AVALIAÇÕES
# ==========================================================

def calcular_media_avaliacoes(lista):
    if len(lista) == 0:
        return 0

    total = sum(
        v["avaliacao"]
        for v in lista
    )

    return total / len(lista)


# ==========================================================
# 11. FUNÇÃO 3 - CONTEÚDO MAIS VISUALIZADO
# ==========================================================

def encontrar_mais_visualizado(lista):
    totais = {}

    for v in lista:
        id_conteudo = v["id_conteudo"]

        if id_conteudo not in totais:
            totais[id_conteudo] = 0

        totais[id_conteudo] += v["visualizacoes"]

    maior_id = max(
        totais,
        key=totais.get
    )

    return maior_id, totais[maior_id]


# ==========================================================
# 12. FUNÇÃO 4 - CONTEÚDOS POR GÊNERO
# ==========================================================

def filtrar_por_genero(lista, genero):
    return [
        c for c in lista
        if c["genero"] == genero
    ]


# ==========================================================
# 13. EXECUÇÃO DAS ANÁLISES
# ==========================================================

total_visualizacoes = calcular_total_visualizacoes(
    visualizacoes
)

media_avaliacoes = calcular_media_avaliacoes(
    visualizacoes
)

mais_visualizado_id, quantidade_maior = encontrar_mais_visualizado(
    visualizacoes
)

conteudo_mais_visualizado = id_para_titulo[
    mais_visualizado_id
]

dramas = filtrar_por_genero(
    conteudos,
    "Drama"
)


# ==========================================================
# 14. RESULTADOS NO TERMINAL
# ==========================================================

print("=" * 60)
print("          ANÁLISE DOS CONTEÚDOS")
print("=" * 60)

print()

# ANÁLISE 1
print("1. QUANTIDADE DE DADOS")
print("-" * 60)

print("Total de conteúdos:", len(conteudos))
print("Total de registros de visualização:", len(visualizacoes))
print("Usuários diferentes:", len(todos_usuarios))

print()

# ANÁLISE 2
print("2. VISUALIZAÇÕES")
print("-" * 60)

print("Total de visualizações:", total_visualizacoes)

print(
    "Conteúdo mais visualizado:",
    conteudo_mais_visualizado
)

print(
    "Quantidade de visualizações:",
    quantidade_maior
)

print()

# ANÁLISE 3
print("3. AVALIAÇÕES")
print("-" * 60)

print(
    "Média geral das avaliações:",
    round(media_avaliacoes, 2)
)

print()

# ANÁLISE 4
print("4. CONTEÚDOS COM MAIS DE 100 MINUTOS")
print("-" * 60)

for conteudo in conteudos_longos:
    print(
        "-",
        conteudo["titulo"],
        "(",
        conteudo["duracao"],
        "minutos)"
    )

print()

# ANÁLISE 5
print("5. CONTEÚDOS DO GÊNERO DRAMA")
print("-" * 60)

for conteudo in dramas:
    print(
        "-",
        conteudo["titulo"]
    )

print()

# ANÁLISE 6
print("6. DADOS DUPLICADOS")
print("-" * 60)

print(
    "Registros duplicados encontrados:",
    duplicados
)

print(
    "Registros únicos após o uso de SET:",
    len(ids_unicos)
)

print()

# ANÁLISE 7
print("7. USUÁRIOS EM COMUM")
print("-" * 60)

print(
    "Usuários que assistiram conteúdos de Drama:",
    len(usuarios_drama)
)

print(
    "Usuários em comum:",
    len(usuarios_em_comum)
)

print()

# ANÁLISE 8
print("8. TÍTULOS DOS CONTEÚDOS")
print("-" * 60)

for titulo in titulos:
    print("-", titulo)

print()

print("=" * 60)
print("             FIM DA ANÁLISE")
print("=" * 60)
