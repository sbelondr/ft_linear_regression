# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: samuel <samuel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 17:17:58 by samuel            #+#    #+#              #
#    Updated: 2020/05/02 23:23:14 by samuel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pandas import DataFrame, read_csv

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
display point and trace
'''
def display_graph(df, X, Y, t):
    x_min = min(X)
    x_max = max(X)
    predict_min = t[0] + (t[1] * x_min)
    predict_max = t[0] + (t[1] * x_max)
    new_x = np.array([x_min, x_max])
    new_y = np.array([predict_min, predict_max])

    plt.grid()
    plt.scatter(X, Y)
    plt.plot(new_x, new_y, c="green")
    plt.xlabel('price')
    plt.ylabel('km')
    plt.title("ft_linear_regression")
    plt.show()

'''
calc theta
return t0 and t1
'''
def gradiant(x, y):
    m = len(x)
    iteration = 10000
    learning_rate = 0.01
    t0 = 0
    t1 = 0
    # nan when keep x
    x_avg = sum(x) / len(x)
    x = x / x_avg
    for it in range(0, iteration):
        predict = t0 + (t1 * x)
        tmp_t0 = (1 / m) * sum(predict - y)
        tmp_t1 = (1 / m) * sum((predict - y) * x)
        t0 = t0 - learning_rate * tmp_t0
        t1 = t1 - learning_rate * tmp_t1
    t1 = t1 / x_avg
    # print(t1)
    # print(t0)
    return (t0, t1)

'''
Open csv and launch gradiant and display_graph
X = Km
Y = price
t = t0 and t1
'''
def open_csv():
    df = pd.read_csv("data.csv")
    X = df.iloc[0:len(df),0]
    Y = df.iloc[0:len(df),1]
    t = gradiant(X, Y)
    display_graph(df, X, Y, t)

def main():
    open_csv()

if __name__ == "__main__":
    main()