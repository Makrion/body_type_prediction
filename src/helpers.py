import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
import seaborn as sns 
import warnings

# POSSIBLE_COLUMNS = ['Age', 'Height', 'Weight', 'Veg_Consump', 'Water_Consump', 'Meal_Count',
#        'Phys_Act', 'Time_E_Dev', 'Gender_Female', 'Gender_Male',
#        'H_Cal_Consump_no', 'H_Cal_Consump_yes', 'Alcohol_Consump_Always',
#        'Alcohol_Consump_Frequently', 'Alcohol_Consump_Sometimes',
#        'Alcohol_Consump_no', 'Smoking_no', 'Smoking_yes',
#        'Food_Between_Meals_Always', 'Food_Between_Meals_Frequently',
#        'Food_Between_Meals_Sometimes', 'Food_Between_Meals_no', 'Fam_Hist_no',
#        'Fam_Hist_yes', 'H_Cal_Burn_no', 'H_Cal_Burn_yes',
#        'Transport_Automobile', 'Transport_Bike', 'Transport_Motorbike',
#        'Transport_Public_Transportation', 'Transport_Walking']
CLASS_COULMN = 'Body_Level'
CLASS_LABELS = ['Body Level 1', 'Body Level 2', 'Body Level 3', 'Body Level 4']
CLASS_COLORS = ['blue','orange', 'green', 'red']
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
    a func to draw hists
'''
def draw_hists(features_columns, data, class_column, class_labels, class_colors):
    num_features = len(features_columns)
    num_rows = int(num_features / 2) + (num_features % 2 > 0)
    num_cols = 2
    fig_width = 15
    fig_height = 3 * num_rows
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(fig_width, fig_height))

    for i, column in enumerate(features_columns):
        row = i // num_cols
        col = i % num_cols
        class_data = [data[column][data[class_column] == label] for label in class_labels]
        axs[row, col].hist(class_data, bins='auto', density=True, histtype='bar', alpha=0.5, label=class_labels, color=class_colors)
        axs[row, col].set_title(f"Histogram of {column}")
        axs[row, col].set_xlabel(column)
        axs[row, col].set_ylabel("Frequency")
        axs[row, col].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    plt.show()


'''
    applying class imbalance fix
'''
def class_balance(X, Y, oversampling_only=False, undersampling_only=False):
    #- applying oversampling
    X_encoded = categorical_values_encoding(X)

    smote = SMOTE()
    X_oversampled, Y_oversampled = smote.fit_resample(X_encoded, Y)

    if oversampling_only == True:
        return X_oversampled, Y_oversampled
    
    # - applying undersampling
    undersampler = RandomUnderSampler()
    X_undersampled, Y_undersampled = undersampler.fit_resample(X_encoded, Y)
    if undersampling_only == True:
        return X_undersampled, Y_undersampled

    X_sampled = pd.concat([X_oversampled, X_undersampled], axis=0)
    Y_sampled = pd.concat([Y_oversampled, Y_undersampled], axis=0)

    return X_sampled, Y_sampled

'''
    drawing correlations heat map
'''
def draw_corr_heatmap(x_train, y_train, numeric_columns):
    # Calculate the correlation matrix
    y_train_encodede = label_encoding(y_train)
    x_train_temp = x_train[numeric_columns].copy()
    x_train_temp.loc[:, CLASS_COULMN] = y_train_encodede
    correlation_matrix = x_train_temp.corr()

    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", square=True)

    # Set plot title
    plt.title("Correlation Matrix")

    # Show the plot
    plt.show()

'''
    apply label encoding for y
'''
def label_encoding(y):
    map_hash = {'Body Level 1': 0, 'Body Level 2': 1, 'Body Level 3': 2, 'Body Level 4': 3}
    y_encoded  = [map_hash[label] for label in y]
    return y_encoded

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

'''
    apply categorical values encoding for x
'''
def categorical_values_decoding(x):
    x_decoded = x.copy()
    mapping = {}
    for column in CATEGORAL_COLUMNS:
        unique_values = CATEGORICAL_COLUMNS_MAPPING[column]
        mapping[column] = {index: value for index, value in enumerate(unique_values)}
    for column, values_map in mapping.items():
        x_decoded[column] = x_decoded[column].map(values_map)


    #reorder
    x_decoded = x_decoded.reindex(columns=POSSIBLE_COLUMNS)

    return x_decoded


'''
    calc acc and f1
'''
def predict(classifier, x_test_encoded, y_test_encoded):
    predictions = classifier.predict(x_test_encoded)

    if type(predictions[0]) is not int:
        predictions = np.round(predictions).clip(0, 3).astype(int)

    classifier_accuracy = accuracy_score(y_test_encoded, predictions)
    classifier_f1_score = f1_score(y_test_encoded, predictions, average='weighted')

    return classifier_accuracy*100.0 , classifier_f1_score*100.0 


'''
    test a classifier
'''
def test_model(classifier, x_train, y_train, x_test, y_test):
    y_train_encoded = label_encoding(y_train)
    y_test_encoded = label_encoding(y_test)
    x_test_encoded = categorical_values_encoding(x_test)


    classifier.fit(x_train, y_train_encoded)

    classifier_accuracy, classifier_f1_score = predict(classifier, x_test_encoded, y_test_encoded)
    print("     out of sample ( predict(test) ):")
    print("         accuracy:", classifier_accuracy)
    print("         weighted F1 score:", classifier_f1_score)
    doc = [ [f'{str(classifier.__class__.__name__)} fot test', str(round(classifier_accuracy, 4)), str(round(classifier_f1_score, 4))] ]

    classifier_accuracy, classifier_f1_score = predict(classifier, x_train, y_train_encoded)
    print("\n     in sample ( predict(train) ):")
    print("         accuracy:", classifier_accuracy)
    print("         weighted F1 score:", classifier_f1_score)
    doc.append([f'{str(classifier.__class__.__name__)} fot train', str(round(classifier_accuracy, 4)), str(round(classifier_f1_score, 4))])

    return classifier, doc

'''
    output the performance report in a md file
'''
def performance_document(docs, balanced_docs, notes=None, file_path=None):
    if file_path is None:
        file_path = 'out/docs/dummy_out.md'

    # Open the file in write mode
    with open(file_path, 'w') as f:
        # Write the table headers
        if notes is not None:
            f.write("####Notes")
            f.write(notes)

        # Write the data rows
        f.write("#### when tested on row baised test data:-\n")
        f.write("|          Classifier          | Accuracy | F1 Score |\n")
        f.write("|------------------------------|----------|----------|\n")
        for doc in docs:
            for d in doc:
                classifier = d[0]
                accuracy = d[1]
                f1 = d[2]
                f.write(f'| {classifier} | {accuracy} | {f1} |\n')
            f.write("|------------------------------|----------|----------|\n")

        f.write("\n#### when tested on balnced test data:-\n")
        f.write("|          Classifier          | Accuracy | F1 Score |\n")
        f.write("|------------------------------|----------|----------|\n")
        for balanced_doc in balanced_docs:
            for balanced_d in balanced_doc:
                classifier = balanced_d[0]
                accuracy = balanced_d[1]
                f1 = balanced_d[2]
                f.write(f'| {classifier} | {accuracy} | {f1} |\n')
            f.write("|------------------------------|----------|----------|\n")