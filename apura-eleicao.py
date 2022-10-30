import requests
import json
import pandas as pd
import os
from time import sleep
from datetime import datetime

while (True): 

    data = requests.get(
       # 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json') # 1o turno
       'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json') # 2o turno

    data = json.loads(data.content)

    candidato = []
    votos = []
    porcentagem = []
    procentagemUrnas = data['pst']

    for info in data['cand']:

        if info['seq'] == '1' or info['seq']== '2' or info['seq'] =='4':
            candidato.append(info['nm'])
            votos.append(info['vap'])
            porcentagem.append(info['pvap'])

    df = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'N votos', 'Porcentagem'])

    print(df)
    print('TOTAL DE URNAS:', procentagemUrnas,'%','\n', 'Hora da chegagem:', datetime.now().strftime("%H:%M:%S"),'\n')

    sleep(30)