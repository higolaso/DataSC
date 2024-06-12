import random # libreria; https://www.w3schools.com/python/ref_random_random.asp

# Definir número de candidatos y votos.
candidatos = [1, 2, 3]

# Votos aleatoriamente: definir el limite de votos (k=200) y repartirlos entre los tres candidatos
votos = random.choices(candidatos, k=200)

# Establecer monto inicial de votos de cada candidato
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

# Sumar los votos a cada candidato
for voto in votos:
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1

# Determinar el ganador por mayoría simple
if votos_candidato_1 > votos_candidato_2 and votos_candidato_1 > votos_candidato_3:
    ganador = "Candidato 1"
elif votos_candidato_2 > votos_candidato_1 and votos_candidato_2 > votos_candidato_3:
    ganador = "Candidato 2"
elif votos_candidato_3 > votos_candidato_1 and votos_candidato_3 > votos_candidato_2:
    ganador = "Candidato 3"
"""else:
    ganador = "Empate" EN CASO DE EMPATE TÉCNICO; NO ESPECIFICADO EN CONSIGNA"""

# Imprimir resultados
print(f"Resultado de la votación:\nCandidato 1 obtuvo {votos_candidato_1} votos.\nCandidato 2 obtuvo {votos_candidato_2} votos.\nCandidato 3 obtuvo {votos_candidato_3} votos.")
print(f"El ganador, por mayoria simple, es el {ganador}.")
