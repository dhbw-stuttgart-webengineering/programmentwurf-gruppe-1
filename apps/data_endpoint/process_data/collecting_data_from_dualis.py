"""Module for reading the data from dualis"""
from apps.data_endpoint.process_data.save_to_database import save_data

def save_data_in_dictionary(collected_data, email_id) -> None:
    """reading the data from dualis and give it to the save_dates function"""
    for data_not_dict in collected_data:
        #Refactor collected_data to a dictionary
        data = data_not_dict.to_dict()
        id_module = data["id"] + data["semester"]

        for unit in data["units"]:
            #Permit to save the data in the database
            save_data(email_id,
                      id_module,
                      data["id"],
                      data["name"],
                      data["credits"],
                      data["semester"],
                      unit)
