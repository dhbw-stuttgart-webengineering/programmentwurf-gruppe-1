import os
from ..utils.dualis.module import Module
from ..data_endpoint.save_to_bank import save_dates

def search_data(data, email_id):
    for item_not_dict in data:
        item = item_not_dict.to_dict()
        semester = item["semester"]
        credits = item["credits"]
        units = item["units"]

        for unit in item["units"]:
            unit_id = unit["id"]
            unit_name = unit["name"]
            unit_credits = unit["credits"]
            unit_grade_first_attempt = unit["grade_first_attempt"]
            unit_grade_second_attempt = unit["grade_second_attempt"]
            save_dates(email_id, unit_id, unit_name, credits, unit_credits, unit_grade_first_attempt, unit_grade_second_attempt, semester, "sebast")


