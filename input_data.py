
import pandas as pd
import os
import json

# download train.csv file from this kaggle dataset - https://www.kaggle.com/datasets/thedevastator/comprehensive-medical-q-a-dataset
file_path = "<<input train.csv file path from Kaggle>>"
def read_and_process_data(file_path):
    df = pd.read_csv(file_path)
    questions = []
    for row in df.iterrows():
        dd = { 
            "question": row[1][1],
            "answer": row[1][2]
        }
        questions.append(dd)

    with open('question_data.json', 'w') as f:
        json.dump(questions, f)
    
    return questions

    



read_and_process_data(file_path)

