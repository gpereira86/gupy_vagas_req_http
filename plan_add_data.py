import pandas as pd
import os


def update_vacancies_excel(vacancies, file_path="vagas.xlsx"):
    file_path = os.path.join(os.path.dirname(__file__), "vagas.xlsx")
    print(file_path)

    if os.path.exists(file_path):
        existing_df = pd.read_excel(file_path, engine="openpyxl")
    else:
        existing_df = pd.DataFrame()

    vaga_data = []
    for vaga in vacancies:
        vaga_data.append({
            "Id": vaga["id"],
            "Id Empresa": vaga["companyId"],
            "Nome Empresa": vaga["careerPageName"],
            "URL Empresa": "Not",
            "Nome da Vaga": vaga["name"],
            "Tipo": vaga["type"].replace("vacancy_type_", "") if vaga["type"] else None,
            "Publicado": pd.to_datetime(vaga["publishedDate"], errors='coerce').strftime('%d/%m/%Y') if vaga["publishedDate"] else None,
            "Dead Line": pd.to_datetime(vaga["applicationDeadline"], errors='coerce').strftime('%d/%m/%Y') if vaga["applicationDeadline"] else None,
            "Remoto?": vaga["isRemoteWork"],
            "Cidade": vaga["city"],
            "Estado": vaga["state"],
            "Regime": vaga.get("workplaceType", "Não informado"),
            "URL Vaga": f'=HYPERLINK("{vaga["jobUrl"]}", "{vaga["jobUrl"]}")' if vaga["jobUrl"] else None
        })

    vaga_df = pd.DataFrame(vaga_data)

    if not existing_df.empty:
        new_vagas = vaga_df[~vaga_df["Id"].isin(existing_df["Id"])]
    else:
        new_vagas = vaga_df

    new_vagas["Nova Adição"] = "Sim"

    if not existing_df.empty:
        existing_df["Nova Adição"] = "Não"

    final_df = pd.concat([existing_df, new_vagas], ignore_index=True)

    final_df = final_df.drop_duplicates(subset=["Id"], keep="last")

    final_df["Publicado"] = pd.to_datetime(final_df["Publicado"], format='%d/%m/%Y', errors='coerce')

    final_df = final_df.sort_values(by=["Publicado", "Nova Adição"], ascending=[False, False])

    final_df["Publicado"] = final_df["Publicado"].dt.strftime('%d/%m/%Y')

    final_df.to_excel(file_path, index=False, engine="openpyxl")

    print(f"Planilha criada/atualizada com sucesso!")