import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from app.preprocessing import load_file


def split_data(df):

    #print(df_s.columns)
    X = df.drop('SalePrice', axis=1)
    Y = df['SalePrice']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=101, test_size=0.2)
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)
    lr = LinearRegression()
    lr.fit(X_train_std, Y_train)
    return [lr, X_train_std, X_test_std, Y_train, Y_test]