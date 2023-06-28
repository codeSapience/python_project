""" 
Author: Akintade Britto (brittoakintade@gmail.com)
Date: 27-Jun-2023
PyVersion: Python 3.9.7

"""

# High level steps;
# - Read all json dataset from the ./data/ dir and return a python dict obj
# - Sniffs the schema of the JSON file
# - Dumps the output in (./schema/)

import json


def open_data_to_dict(json_datafile: str = "", input_dir: str = "./data"):
    '''
    Reads the content of a json file from a specified directory, into a python dictionary
    or an empty dictionary if file is invalid or empty

    Return: dict
    '''
    file_to_load = f"{input_dir}/{json_datafile}"
    result_dict = dict()

    try:
        with open(file_to_load, "r") as json_data:
            result_dict = json.load(json_data)
        return result_dict

    except Exception as an_error:
        print("An Error Occured While Loading DataFile! \n") # could be replaced with logger.error
        raise (an_error)
    

def sniff_and_dump(data_dict: dict, file_name: str = "", output_dir: str = "./schema"):
    '''
    Receives a dict, marshal the dict items based on pre-defined guidelines 
    then output the result into a json file

    Return: Boolean (the status of the write operation to file)
    '''
    filepath_to_save = f"{output_dir}/{file_name}"
    result_dict = dict()
    subject_dict = data_dict.get("message", {})
    was_successful = False

    for each_key in subject_dict:
        sample_value = {
            "type": "DATATYPE",
            "tag": "",
            "description": "",
            "required": False
        }
        if isinstance(subject_dict[each_key], int):
            sample_value["type"] = "integer"
            result_dict[each_key] = sample_value

        elif isinstance(subject_dict[each_key], str):
            sample_value["type"] = "string"
            result_dict[each_key] = sample_value

        elif isinstance(subject_dict[each_key], list):
            sample_value["type"] = "ENUM"
            result_dict[each_key] = sample_value

        elif isinstance(subject_dict[each_key], dict):
            sample_value["type"] = "ARRAY"
            result_dict[each_key] = sample_value

    try:
        with open(filepath_to_save, 'w') as output_jsonfile:
            json.dump(result_dict, output_jsonfile)
        was_successful = True
        print(f"Successfully saved file! \n {file_name}") # could be replaced with logger.info

    except Exception as a_bad_error:
        print("An Error Occured While Trying To Save SchemaFile! \n") # could be replaced with logger.error
        raise (a_bad_error)
    finally:
        return (was_successful)

def run_program():
    try:
        datafile_name = "sample_data_file.json"
        outputfile_name = "sample_output_file.json"
        sniff_and_dump(open_data_to_dict(datafile_name), outputfile_name)
    except FileNotFoundError as first_err:
        print("The specified filename is invalid, please check one more time.") # could be replaced with logger.error
        raise(first_err)
    except Exception as second_err:
        raise (second_err)
