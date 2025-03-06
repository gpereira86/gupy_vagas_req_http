import gupy_vagas as vagas
import plan_add_data as plan
import key_words as kw
import os


def verificar_planilha_aberta(file_path):
    if not os.path.exists(file_path):
        return False

    try:
        with open(file_path, 'r+'):
            return False
    except IOError:
        return True


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "vagas.xlsx")

    if verificar_planilha_aberta(file_path):
        print("A planilha está aberta. Por favor, feche-a e tente novamente.")
        exit()

    setParams = {
        "estagioRemoto": {
            "jobName": "estagio",
            "workplaceType": "remote"
        },
        "estagioRJ":{
            "jobName": "estagio",
            "state": "Rio de Janeiro"
        },
        "estagiarioRemoto": {
            "jobName": "estagiario",
            "workplaceType": "remote"
        },
        "estagiarioRJ":{
            "jobName": "estagiario",
            "state": "Rio de Janeiro"
        },
        "estagiariaRemoto": {
            "jobName": "estagiaria",
            "workplaceType": "remote"
        },
        "estagiariaRJ": {
            "jobName": "estagiaria",
            "state": "Rio de Janeiro"
        },
        "phpRemoto": {
            "jobName": "PHP",
            "workplaceType": "remote"
        },
        "phpRJ":{
            "jobName": "PHP",
            "state": "Rio de Janeiro"
        },
        "customerSuccessRemoto": {
            "jobName": "Customer Success",
            "workplaceType": "remote"
        },
        "customerSuccessRJ":{
            "jobName": "Customer Success",
            "state": "Rio de Janeiro"
        },

    }

    all_vacancies = []

    for key, params in setParams.items():
        print(f"Gerando dados de {key} => {params}")
        vacancies = vagas.fetch_vacancies(params)
        all_vacancies.extend(vacancies)

    plan.update_vacancies_excel(all_vacancies)

    palavras_chave = ['php', 'desenvolvimento', 'desenvolvedor', 'junior', 'júnior', 'jr']

    kw.formatar_palavras_chave(file_path, palavras_chave)