import numpy as np

from app.preprocessing import load_file
from app.training_split import split_data
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from pipelines.training import file_loaded
import pandas as pd




def inference(df):
    [lr, X_train_std, X_test_std, Y_train, Y_test]=split_data(df)
    lr.fit(X_train_std, Y_train)
    Y_pred_lr = lr.predict(X_test_std)
    print(Y_pred_lr)
    #make_predictions(Y_pred_lr, Y_test)
    r2 = (r2_score(Y_test, Y_pred_lr))
    mae= (mean_absolute_error(Y_test, Y_pred_lr))
    mse= (np.sqrt(mean_squared_error(Y_test, Y_pred_lr)))
    return r2,mae,mse
