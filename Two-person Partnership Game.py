# Two-person partnership game
# 2020-3-6
# TBSI
# ZHX

import sympy as sy
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title('Two-person Partnership Game')


s1, s2, b = sy.symbols('s1, s2, b')  # identify the symbols
profit = 4 * (s1 + s2 + b * s1 * s2)  # the profit of the company
u1 = 0.5 * profit - s1 ** 2  # player 1's payoff
u2 = 0.5 * profit - s2 ** 2  # player 2's payoff

du1_ds1 = sy.diff(u1, s1, 1)
du2_ds2 = sy.diff(u2, s2, 1)

print(du1_ds1)
print(du2_ds2)


def draw_BR():
    fig = plt.figure()

    ax1 = fig.add_subplot(111)  # the fig is on the position 1 of one-by-one figure
    ax1.set(xlim=[0, 4], ylim=[0, 4],
            title='Best Response',
            xlabel='s1',
            ylabel='s2')

    #draw p1's BR line
    b = 0.25  # temp
    s1 = np.array(range(5))
    s2 = np.array(range(5))

    br_s1 = 1 + b * s2  # best response of p1
    br_s2 = 1 + b * s1  # best response of p2

    ax1.plot(s1, br_s1, color='red', label='p1 BR')
    ax1.plot(br_s2, s2, color='blue', label='p2 BR')

    plt.legend(loc=2,ncol=2)
    plt.show()


tk.Button(root, text="Draw BR lines", width=10, command=draw_BR).grid(row=5, column=1, ipadx=30, pady=5)

tk.mainloop()