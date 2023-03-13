import pandas as pd
import matplotlib.pyplot as plt

def plot_df_column(df_season_result):
    plt.plot(df_season_result)
    plt.title('Running stake for round')
    plt.show()


def sub_plots(kolumna1, kolumna2):
    fig, axs = plt.subplots(nrows=2)
    kolumna1.plot(ax=axs[0])
    kolumna2.plot(ax=axs[1])
    plt.show()