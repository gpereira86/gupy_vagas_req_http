import requests
import math

headers = {"accept": "application/json"}
base_url = "https://portal.api.gupy.io/api/v1/jobs"
params = {
    "jobName": "estagio",
    "workplaceType": "remote"
}

response = requests.get(base_url, params=params, headers=headers)

dados = response.json()
pagination = dados['pagination']
vacancies = dados['data']

if pagination and pagination['total'] > 10:

    qtdyCycle = pagination['total']/10
    qtdyCycle = math.ceil(qtdyCycle)

    for page in range(1, qtdyCycle+1):
        params['offset'] = page * 10
        response = requests.get(base_url, params=params, headers=headers)
        vacancies.extend(response.json()['data'])

