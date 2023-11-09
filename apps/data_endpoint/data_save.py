from ..data_endpoint.save_to_bank import save_dates

def search_data(data, email_id):
    for item_not_dict in data:
        item = item_not_dict.to_dict()
        abk = item["id"]
        bezeichnung = item["name"]
        semester = item["semester"]
        credits_ = item["credits"]
        id_module = abk + semester

        for unit in item["units"]:
            unit_id = unit["id"]
            unit_name = unit["name"]
            unit_credits = unit["credits"]
            unit_grade_first_attempt = unit["grade_first_attempt"]
            unit_grade_second_attempt = unit["grade_second_attempt"]
            save_dates(email_id,id_module, abk, bezeichnung, unit_id, unit_name, credits_, unit_credits, unit_grade_first_attempt, unit_grade_second_attempt, semester)


