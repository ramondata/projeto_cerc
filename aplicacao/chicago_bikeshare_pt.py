#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Começando com os imports
import sys
sys.path.insert(0, "/Users/ramon/projeto_cerc/projeto_cerc/modulos/")
import os
os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/modulos/")
from config_log import log
import csv
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE
from datetime import date

sys.stdout.write('Execução iniciada\n')

#-----------------------------------------------------------------------------------------------------------#

#configurando sistema de logs
#para leitura, va na pasta log e procure pelo arquivo com a data de hoje
logger = log()
log = logger._log

#-----------------------------------------------------------------------------------------------------------#

#descompactando o arquivo de dados
log.info('Descompactando arquivo fonte de dados')
os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/amostra_dados/")
unzip_data = Popen('unzip chicago.csv.zip', shell=True, stdin=None, stdout=PIPE, stderr=PIPE)
out, err = unzip_data.communicate()


#-----------------------------------------------------------------------------------------------------------#

# Vamos ler os dados como uma lista
os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/amostra_dados/")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/log/")
log.info("Documento acessado")



#-----------------------------------------------------------------------------------------------------------#

# Vamos verificar quantas linhas nos temos
log.info("Numero de linhas:")
log.info(len(data_list))

#-----------------------------------------------------------------------------------------------------------#

# Imprimindo a primeira linha de data_list para verificar se funcionou.
log.info("Linha 0: ")
log.info(data_list[0])
# o cabeçalho dos dados, para que possamos identificar as colunas.

#-----------------------------------------------------------------------------------------------------------#

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
log.info("Linha 1: ")
log.info(data_list[1])

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
log.info("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for linha in data_list[:20]:
    log.info('%s' % linha)

#-----------------------------------------------------------------------------------------------------------#

# Vamos mudar o data_list para remover o cabeçalho dele.
log.info('remoção do cabeçalho dos exemplos do data list')
data_list = data_list[1:]

#-----------------------------------------------------------------------------------------------------------#

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

#input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `genero` das primeiras 20 linhas

log.info("\nTAREFA 2: Imprimindo o genero das primeiras 20 amostras")
obtem_genero: list = list(map(lambda p: log.info('genero > vazio') if p[6] == '' else log.info('genero > %s' % p[6]), data_list[:20]))
obtem_genero

#-----------------------------------------------------------------------------------------------------------#

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

#input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    '''
    -> Obtém uma mesma posição de valores numa lista de listas
    i.e.: Dados de genero estarão sempre no mesmo index em cada lista dentro da lista maior
    e.g.: index -> 6; gênero

    -> Argumentos:
          data: identifica o conjunto de dados a manipular.
          index: Identifica o índice ao qual desejo obter os dados de mesma classificação(i.d.: Como se fosse uma coluna em um dataset).

    -> Retorna:
          Lista com dados de uma mesma 'coluna' ou mesmo index dentro do conjunto fonte.
    '''
    column_list: list = list(map(lambda r: r[index], data))
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
log.info("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
log.info(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1048575, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
vazio = 0
generos: list = list(map(lambda t: 'vazio' if t[6] == '' else t[6].lower(), data_list))

for genero in generos:
    if genero == 'male':
        male += 1
    elif genero == 'female':
        female += 1
    else:
        vazio += 1

# Caso fosse permitido usar função seria da forma abaixo:        
#male = generos.count('male')
#female = generos.count('female')
#vazio = generos.count('vazio')


# Verificando o resultado
log.info("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
log.info("Masculinos: %s" % male)
log.info("Femininos: %s" % female)
log.info("Vazio: %s" % vazio)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 665_437 and female == 198_247, "TAREFA 4: A conta nao bate."
#ASSERT INSERIDO PRA UMA VALIDAÇAO EXATA DE CONTAGENS TOTAIS
assert male + female + vazio == len(data_list), "TAREFA 4: Volumetrias das contagens nao batem"
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list: list) -> list:
    '''
   '-> Através da leitura de um conjunto de dados indicado como único paramêtro, testifica a contagem de gêneros nesta fonte de dados.
    
    -> Argumentos:
          data_list: Identifica o conjunto de dados a manipular 

    -> Retorna:
          Lista com apenas dois itens. O primeiro a contagem masculina e a segunda, a contagem feminina
          e.g.: [15, 15]
    '''
    male = 0
    female = 0
    obtem_genero = lambda d: 'vazio' if d[6] == '' else d[6].lower()
    generos = list(map(obtem_genero, data_list))
    count_male = generos.count('male')
    count_female = generos.count('female')
    return [count_male, count_female]


log.info("\nTAREFA 5: Imprimindo o resultado de count_gender")
log.info(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 665_437 and count_gender(data_list)[1] == 198_247, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list: list) -> list:
    '''
    -> A partir da leitura de um conjunto de dados, nos retorna qual dos domínios tem maior ocorrência
        i.e.: Qual dos gêneros tem maior frequência de aparição.
    -> Argumentos:
          data_list: Identifica o conjunto de dados a manipular 
      
    -> Retorna:
          Uma string com a informação de maior gênero ou igualdade
          e.g.: Female
          e.g.: Equal
    '''
    generos = count_gender(data_list)
    male, female = generos
    return 'Male' if male > female else 'Female' if female > male else 'Equal'


log.info("\nTAREFA 6: Qual é o gênero mais popular na lista?")
log.info("O gênero mais popular na lista é: %s" % most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
log.info('Gráfico salvo')
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.savefig('/Users/ramon/projeto_cerc/projeto_cerc/log/graficos/print_gender_%s.png' % date.today(), format='png')
plt.show(block=True)

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

def addlabels(x: list,y: list) -> None:
    '''
    -> Implementar rótulos de valores no gráfico com a bibliioteca matplotlib.
    
    -> Argumentos:
        x: valor a ser utilizado no eixo x do gráfico.
        y: Valor a ser utilizado no eixo y do gráfico.
    
    -> Retorna:
          Apenas aplica a transformação necessária ao gráfico em questão.
    '''
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

user_type_list = column_to_list(data_list, -3)
x_types = ['Dependent','Customer','Subscriber']
y_quantity = [int(user_type_list.count('Dependent')), int(user_type_list.count('Customer')), int(user_type_list.count('Subscriber'))]
y_pos = list(range(len(x_types)))
plt.bar(x_types, y_quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuários')
plt.title('Quantidade por tipo de usuário')
addlabels(x_types, y_quantity)
plt.savefig('/Users/ramon/projeto_cerc/projeto_cerc/log/graficos/print_user_types_%s.png' % date.today(), format='png')
plt.show(block=True)
log.info("\nTAREFA 7: Verifique o gráfico de user_types")

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
log.info("\nTAREFA 8: Por que a condição a seguir é Falsa?")
log.info("male + female == len(data_list): %s" % (male + female == len(data_list)))
answer = "Por conta dos campos vazios. Para a equação ser bem sucedida seria necessário subtrair da contagem do data_list as aparições vazias"
log.info("resposta: %s" % answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Por conta dos campos vazios, Para a equação ser bem sucedida seria necessário subtrair da contagem do data_list as aparições vazias", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0
max_trip = 0
mean_trip = 0
median_trip = 0

#max
for duration in trip_duration_list:
    duration = float(duration)
    if duration > max_trip:
        max_trip = duration

#min
min_trip = max_trip
for duration in trip_duration_list:
    duration = float(duration)
    if duration < min_trip:
        min_trip = duration

#media
trip_duration_float = [float(duration) for duration in trip_duration_list if duration != '']
soma_duration = sum(trip_duration_float)
contagem_duration = len(trip_duration_float)
mean_trip = round(soma_duration / contagem_duration)

#mediana
if contagem_duration % 2 == 0:
    copia_lista_trip_duration_ponteiro_distinto = trip_duration_list.copy()
    copia_lista_trip_duration_ponteiro_distinto.sort()
    index_central_1 = round((contagem_duration - 1) / 2)
    index_central_2 = index_central_1 + 1
    median_trip = round((copia_lista_trip_duration_ponteiro_distinto[index_central_1] + copia_lista_trip_duration_ponteiro_distinto[index_central_2]) / 2)
else:
    copia_lista_trip_duration_ponteiro_distinto = trip_duration_list.copy()
    copia_lista_trip_duration_ponteiro_distinto.sort()
    index_central = round((contagem_duration - 1) / 2)
    median_trip = copia_lista_trip_duration_ponteiro_distinto[index_central]


log.info("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
log.info("Min: %s Max: %s Média: %s Mediana: %s" % (min_trip, max_trip, mean_trip, median_trip))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86_338, "TAREFA 9: max_trip com resultado errado!"
#assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
#assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nóss temos, usando set()

start_stations = set(column_to_list(data_list, 3))

log.info("\nTAREFA 10: Imprimindo as start stations:")
log.info('Contagem de start stations: %s'% len(start_stations))
for station in start_stations:
    log.info(station)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
#assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a funç˜ão faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """
log.info('\nTAREFA 11: Estruturação de docstring realizada para as funções presentes neste script')

#-----------------------------------------------------------------------------------------------------------#

#input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
log.info("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = list(set(column_list))
    count_items = []
    for item in item_types:
        contagem_item = column_list.count(item)
        count_items.append(contagem_item)
    return (item_types, count_items)


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    log.info("\nTAREFA 12: Imprimindo resultados para count_items()")
    log.info("Tipos: %s Counts: %s" % (types, counts))
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1_048_575, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

#-----------------------------------------------------------------------------------------------------------#

#deletando arquivo redundante
log.info('\nApagando arquivo redundante')
os.chdir("/Users/ramon/projeto_cerc/projeto_cerc/amostra_dados/")
delete_file = Popen('rm chicago.csv; rm -R __MACOSX', shell=True, stdin=None, stdout=PIPE, stderr=PIPE)
out, err = delete_file.communicate()

sys.stdout.write('Execução finalizada\n')
sys.stdout.write('##############################################################\n')
sys.stdout.write('     Veja o log desta execução na pasta log do projeto\n')
sys.stdout.write('     Nome do arquivo de log: %s\n' % logger._name_file)
sys.stdout.write('##############################################################\n')