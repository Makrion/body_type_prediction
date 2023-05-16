# imports
import numpy as np
import pandas as pd
import pickle
from sklearn.impute import SimpleImputer

# helper functions
'''
    constants
'''
MODEL_PATH = 'model.pkl'
TEST_FILE_PATH = 'test.csv'
OUT_PATH = 'preds.txt'
CATEGORAL_COLUMNS = ['Gender', 'H_Cal_Consump', 'Alcohol_Consump', 'Smoking', 'Food_Between_Meals', 'Fam_Hist', 'H_Cal_Burn', 'Transport']
POSSIBLE_COLUMNS = ['Gender', 'Age', 'Height', 'Weight', 'H_Cal_Consump', 'Veg_Consump', 'Water_Consump', 'Alcohol_Consump', 'Smoking', 'Meal_Count',
               'Food_Between_Meals', 'Fam_Hist', 'H_Cal_Burn', 'Phys_Act',
               'Time_E_Dev', 'Transport']
CATEGORICAL_COLUMNS_MAPPING = {
    'Gender': ['Female', 'Male'],
    'H_Cal_Consump': ['yes', 'no'],
    'Alcohol_Consump': ['no', 'Sometimes', 'Frequently', 'Always'],
    'Smoking': ['no', 'yes'],
    'Food_Between_Meals': ['Frequently' ,'Sometimes' ,'no' ,'Always'],
    'Fam_Hist': ['yes', 'no'],
    'H_Cal_Burn': ['no' ,'yes'],
    'Transport': ['Public_Transportation' ,'Automobile', 'Walking' ,'Bike' ,'Motorbike']
}

'''
    apply label decoding for y
'''
def label_decoding(y):
    map_hash = { '0': 'Body Level 1', '1': 'Body Level 2', '2': 'Body Level 3', '3': 'Body Level 4'}
    y_decoded  = [map_hash[str(label)] for label in y]
    return y_decoded

'''
    apply categorical values encoding for x
'''
def categorical_values_encoding(x):
    x_encoded = x.copy()
    mapping = {}
    for column in CATEGORAL_COLUMNS:
        unique_values = CATEGORICAL_COLUMNS_MAPPING[column]
        mapping[column] = {value: index for index, value in enumerate(unique_values)}
    for column, values_map in mapping.items():
        x_encoded[column] = x_encoded[column].map(values_map)


    #reorder
    x_encoded = x_encoded.reindex(columns=POSSIBLE_COLUMNS)

    return x_encoded


# load data
test_file = TEST_FILE_PATH
test_df = pd.read_csv(test_file)


# encode categorical cols  
x_test = categorical_values_encoding(test_df)

# remove nans if there is any
imputer = SimpleImputer(strategy='median')
x_imputed = imputer.fit_transform(x_test)
x_test_imputed = pd.DataFrame(x_imputed, columns=POSSIBLE_COLUMNS)


# load the feature models
model = pickle.load(open(MODEL_PATH, 'rb'))



# get the predictions
out = model.predict(x_test_imputed)


# out_df = pd.DataFrame({'Body_Level': out})

# # decode classes
out_df_labels = label_decoding(out)

# # save the predictions in text file
with open(OUT_PATH, 'w') as file:
    # Write the list elements to the file
    for item in out_df_labels:
        file.write(str(item) + '\n')
