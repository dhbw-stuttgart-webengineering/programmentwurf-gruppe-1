"""Module for reading the data from dualis"""
from ..data_endpoint.save_to_bank import save_dates

def search_data(data, email_id):
    """reading the data from dualis and give it to the save_dates function"""
    for dates_not_dict in data:
        dates = dates_not_dict.to_dict()
        id_module = dates["id"] + dates["semester"]

        for unit in dates["units"]:
            save_dates(email_id,
                       id_module,
                       dates["id"],
                       dates["name"],
                       dates["credits"],
                       dates["semester"],
                       unit)
