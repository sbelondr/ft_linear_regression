# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 17:17:58 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/04 09:10:43 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pandas import DataFrame, read_csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

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
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("ft_linear_regression")
    plt.show()

def write_file(t0, t1):
    f = open(".data.txt", "w")
    f.write(str(t0))
    f.write("\n")
    f.write(str(t1))
    f.close()

'''
calc theta
return t0 and t1
'''
def train(x, y):
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
    write_file(t0, t1)
    return (t0, t1)

'''
Open csv and launch gradiant and display_graph
X = Km
Y = price
t = t0 and t1
'''
def open_csv():
    try:
        df = pd.read_csv("data.csv")
    except IOError:
        print("File error")
        sys.exit(-1)
    X = df.iloc[0:len(df),0]
    Y = df.iloc[0:len(df),1]
    t = train(X, Y)
    display_graph(df, X, Y, t)

def main():
    open_csv()

if __name__ == "__main__":
    main()
