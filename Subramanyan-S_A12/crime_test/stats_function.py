import pandas as pd

crime_data = pd.read_csv('/mnt/scratch/FA24_CS131_Jessica/ssubramanyanfa24/mini-assignments-singaram-subramanyan/Subramanyan-S_A12/crime_test/Crime_Data_from_2020_to_Present.csv')


def mean_vict_age():
    return crime_data['Vict Age'].mean()

def median_vict_age():
    return crime_data['Vict Age'].median()
