import requests

resposta = requests.get(
    "https://wger.de/api/v2/exerciseinfo/?limit=1",
    timeout=15
)

resposta.raise_for_status()
dados=resposta.json()


exercicio1 = (dados['results'][0])

for traducao in exercicio1['translations']:
    if traducao['language'] == 7:
        print(traducao['name'])

dicionario={'Hamstrings':'Posterior de coxa','Glutes':'Glúteos'}
for musculo in exercicio1["muscles"]:
    nome_pt = dicionario.get(musculo["name_en"], musculo["name_en"])
    print(nome_pt)
    print(musculo["image_url_main"])

nome_pt= dicionario.get(musculo['name_en'],musculo['name_en'])
