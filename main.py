# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from app.preprocessing import load_file
from pipelines.inference import inference
from pipelines.training import file_loaded
import pandas as pd



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    file = 'C:/Users/kaust/train.csv'
    [df1, f1]=file_loaded(file)
    f2=inference(df1)

    print(df1)
    print(f1[0])
    print(f2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
