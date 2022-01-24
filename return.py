import pandas as pd
import numpy as np

def get_returns():
    me_m = pd.read_csv("data/EFT_3.csv",
                       header=0, index_col=0, na_values=-99.99)
    rets = me_m.pct_change()
    rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period('M')
    return rets

def compound_returns(rets):
    np.dropna(rets)
    com_rets = np.prod(rets + 1) - 1
    return com_rets

def some_metrics(rets):
    num_obs = rets.shape[0]

    deviation = rets - rets.mean()
    squared_deviations = deviation ** 2
    variance = squared_deviations.sum()/(num_obs - 1)
    volatility = np.sqrt(variance) 
    #volatility = rets.std() 

    pass

def annualization_volatility(rets):

    pass


def get_returns_risk_adjust():
    pass