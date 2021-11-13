from app.preprocessing import load_file
from app.training_split import split_data
import pandas as pd



def file_loaded(filepath):
    #df = load_file(filepath)
    #print(df.head())
    df1 = load_file(filepath)
    df2 = split_data(df1)
    #print(df1.head())
    #print(df2)
    return [df1,df2]




