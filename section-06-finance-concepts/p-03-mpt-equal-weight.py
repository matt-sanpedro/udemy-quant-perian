'''
Modern Portfolio Theory (MPT): a mean variance analysis mathematical framework introduced by 
economist Harry Markowitz in 1952 that helps investors build optimal asset mix.
    - maximizes expected returns for a chosen level of risk
    - if the returns are equal, investors would rather choose lower volatility
    - in other words, investors would choose the better Sharpe ratio

Monte Carlo Simulation: computational technique that predicts the probability of different 
outcomes by running a model thousands or millions of times with randomly generated inputs.
    - can be used to simulate random combinations of different holdings
    - then, calculate the historic return and volatility

Minimization search process: mathematical or computational procedure used to find the 
input values that produce lowest possible output value of an objective function.
    - in context with defining optimal stock holding, can find the efficient frontier

Efficient Frontier: holding combination that maximizes the return for a desired volatility
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, gc

def read_stocks(stock_list):
    csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DATA"))
    frames = []

    for stock in stock_list:
        csv_path = os.path.join(csv_dir, f'{stock}.csv')
        frames.append(pd.read_csv(csv_path, index_col='Date', parse_dates=True)['Adj Close'])

    return frames

def concat_data(frames,stock_list):
    retail = pd.concat(frames,axis=1)
    retail.columns = stock_list
    return retail

stock_list = ['COST', 'WMT', 'TGT', 'DG']
dfs = read_stocks(stock_list)
retail = concat_data(dfs,stock_list)
del dfs
gc.collect()
print(retail)
