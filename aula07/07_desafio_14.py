import sys
import requests
import json

# Crie uma aplicação que permita ao usuário obter informações sobre um feitiço determinado.
# O usuário deve digitar o nome de um feitiço como entrada para a nossa aplicação através da
#linha de comando. Por exemplo:
# python 07_desafio_14.py Feitiço de Desaparecimento
# Você deve melhorar os dados sobre o feitiço diretamente do JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Utilize uma biblioteca requests para ler o JSON.
# Ao final do programa, imprima os dados sobre o feitiço que ele solicita.
# Se o feitiço não foi encontrado, lance uma exceção.
URL = "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json"
resposta = requests.get(URL)
conteudo = resposta.text
print('Código da resposta:', resposta.status_code)
print('Tipo da resposta:', resposta.headers['Content-Type']) # text/html
print('Conteúdo:')
print(conteudo)
print('--------------------------------------------------')
print()

