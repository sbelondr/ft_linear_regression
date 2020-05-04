# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/03 08:46:59 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/04 09:08:25 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def get_data():
    try:
        f = open(".data.txt", "r")
        s = f.read().split()
    except IOError:
        s = ["0", "0"]
    return s

def ask_input():
    while (True):
        km = input("Enter km: ")
        if (km.isnumeric()):
            return km

def calc_price(data, km):
    t0 = float(data[0])
    t1 = float(data[1])
    kmFloat = float(km)
    result = t0 + (t1 * kmFloat)
    print(result)

def main():
    data = get_data()
    km = ask_input()
    calc_price(data, km)

if __name__ == "__main__":
    main()
