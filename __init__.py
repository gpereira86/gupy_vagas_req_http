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


file_path = "vagas.xlsx"

if verificar_planilha_aberta(file_path):
    print("A planilha está aberta. Por favor, feche-a e tente novamente.")
    exit()

params = {
    "jobName": "estagio",
    "workplaceType": "remote"
}

vacancies = vagas.fetch_vacancies(params)

plan.update_vacancies_excel(vacancies)

palavras_chave = ['php', 'desenvolvimento', 'desenvolvedor']

kw.formatar_palavras_chave(file_path, palavras_chave)