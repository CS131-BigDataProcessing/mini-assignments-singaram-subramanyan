import pandas as pd

crime_data = pd.read_csv('/mnt/scratch/FA24_CS131_Jessica/ssubramanyanfa24/mini-assignments-singaram-subramanyan/Subramanyan-S_A12/crime_test/Crime_Data_from_2020_to_Present.csv')

def null_invalid_value_check_vict_sex():
    if ((crime_data['Vict Sex'] != 'M').any() | (crime_data['Vict Sex'] != 'W').any()):
        return "Invalid value(s) detected"
    elif ((crime_data['Vict Sex'].isna()).any()):
        return "Null value(s) detected"
    else:
        return "No invalid or null values detected"

def null_invalid_value_check_vict_age():
    if ((crime_data['Vict Age'] > 100).any() | (crime_data['Vict Age'] < 1).any()):
        return "Invalid value(s) detected"
    elif ((crime_data['Vict Age'].isna()).any()):
        return "Null value(s) detected"
    else:
        return "No invalid or null values detected"


def valid_datatype():
    if (type(null_invalid_value_check_vict_sex()) != str):
        return False
    elif (type(null_invalid_value_check_vict_age()) != str):
        return False
    else:
        return True
