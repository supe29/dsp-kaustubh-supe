import pandas as pd
from sklearn.preprocessing import LabelEncoder
def load_file(filename):
    df = pd.read_csv(filename)
    #print(pd.DataFrame(file))
    #df= pd.DataFrame
    #print(df.head())
    df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())
    df.drop(['Alley'], axis=1, inplace=True)
    df['BsmtCond'] = df['BsmtCond'].fillna(df['BsmtCond'].mode()[0])
    df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])
    df['FireplaceQu'] = df['FireplaceQu'].fillna(df['FireplaceQu'].mode()[0])
    df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
    df.drop(['GarageYrBlt'], axis=1, inplace=True)
    df['GarageFinish'] = df['GarageFinish'].fillna(df['GarageFinish'].mode()[0])
    df['GarageQual'] = df['GarageQual'].fillna(df['GarageQual'].mode()[0])
    df['GarageCond'] = df['GarageCond'].fillna(df['GarageCond'].mode()[0])
    df.drop(['PoolQC', 'Fence', 'MiscFeature'], axis=1, inplace=True)
    df.drop(['Id'], axis=1, inplace=True)
    df['MasVnrType'] = df['MasVnrType'].fillna(df['MasVnrType'].mode()[0])
    df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mode()[0])
    df['BsmtExposure'] = df['BsmtExposure'].fillna(df['BsmtExposure'].mode()[0])
    df.dropna(inplace=True)
    df.drop(['LotFrontage', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1',
             'BsmtFinSF2', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'EnclosedPorch',
             '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition',
             'Neighborhood', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
             'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
             'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'FullBath', 'HalfBath', 'BedroomAbvGr',
             'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'LowQualFinSF',
             'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
             'RoofStyle', 'RoofMatl', 'GarageType', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
             'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF'], axis=1, inplace=True)
    #encoding
    df = pd.get_dummies(df, columns=['MSZoning', 'BsmtQual'])
    return df
