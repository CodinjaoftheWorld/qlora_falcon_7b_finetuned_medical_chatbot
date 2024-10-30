
import pandas as pd
import os
import json


file_path = "/Users/GauravSaini/Documents/Gaurav/Extra/GenAI/finetuning/falcon/train.csv"
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

