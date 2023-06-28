# coding: utf-8 

# Come�ando com os imports
import logging
import csv
#import matplotlib.pyplot as plt
import sys
import os
from subprocess import Popen, PIPE

os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/amostra_dados/")

unzip_data = Popen('unzip chicago.csv.zip', shell=True, stdin=None, stdout=PIPE, stderr=PIPE)
out, err = unzip_data.communicate()

print(out)

#sys.path.insert(0, "/Users/ramon/projeto_cerc/projeto_cerc/amostra_dados/")

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas n�s temos
print("N�mero de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# � o cabe�alho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for linha in data_list[0:19]:
    print('linha > %s' % linha)


# Vamos mudar o data_list para remover o cabe�alho dele.
data_list = data_list[1:]

# N�s podemos acessar as features pelo �ndice
# Por exemplo: sample[6] para imprimir g�nero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `g�nero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o g�nero das primeiras 20 amostras")


# �timo! N�s podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por �ndices.
# Mas ainda � dif�cil pegar uma coluna em uma lista. Exemplo: Lista com todos os g�neros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma fun��o para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Voc� pode usar um for para iterar sobre as amostras, pegar a feature pelo seu �ndice, e dar append para uma lista
    return column_list


# Vamos checar com os g�neros se isso est� funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de g�neros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista n�o coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada g�nero. Voc� n�o deveria usar uma fun��o para isso.
male = 0
female = 0


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos n�s encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta n�o bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma fun��o para contar os g�neros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que n�s podemos contar os usu�rios, qual g�nero � mais prevalente?
# TAREFA 6
# TODO: Crie uma fun��o que pegue o g�nero mais popular, e retorne este g�nero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    answer = ""
    return answer


print("\nTAREFA 6: Qual � o g�nero mais popular na lista?")
print("O g�nero mais popular na lista �: ", most_popular_gender(data_list))

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo est� rodando como esperado, verifique este gr�fico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('G�nero')
plt.xticks(y_pos, types)
plt.title('Quantidade por G�nero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gr�fico similar para user_types. Tenha certeza que a legenda est� correta.
print("\nTAREFA 7: Verifique o gr�fico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte quest�o
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condi��o a seguir � Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Escreva sua resposta aqui."
print("resposta:", answer)

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua pr�pria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (dura��o da viagem) agora. N�o conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a dura��o de viagem M�nima, M�xima, M�dia, e Mediana.
# Voc� n�o deve usar fun��es prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.


print("\nTAREFA 9: Imprimindo o m�nimo, m�ximo, m�dia, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "M�dia: ", mean_trip, "Mediana: ", median_trip)

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# G�nero � f�cil porque n�s temos apenas algumas op��es. E quanto a start_stations? Quantas op��es ele tem?
# TODO: Verifique quantos tipos de start_stations n�s temos, usando set()
start_stations = set()

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que voc� documentou suas fun��es. Explique os par�metros de entrada, a sa�da, e o que a fun��o faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Fun��o de exemplo com anota��es.
      Argumentos:
          param1: O primeiro par�metro.
          param2: O segundo par�metro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma fun��o para contar tipos de usu�rios, sem definir os tipos
# para que n�s possamos usar essa fun��o com outra categoria de dados.
print("Voc� vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ N�O MUDE NENHUM C�DIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: H� 3 tipos de g�nero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
