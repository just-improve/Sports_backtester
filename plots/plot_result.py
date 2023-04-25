import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display
import webbrowser
from tempfile import NamedTemporaryFile

def plot_df_column(series_sekw):
    fig, axs = plt.subplots(1, 1, figsize=(10, 6))
    axs.set_title('Histogram')
    axs.set_xlabel('Bins')
    axs.set_ylabel('Frequency')
    plt.show()

def sub_plots(stake_for_round, Round_result, Round_loss_only, Cum_result, series_sekw, season_wins, season_looses):
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))
    stake_for_round.plot(ax=axs[0, 0])
    Round_result.plot(ax=axs[0, 1])
    Round_loss_only.plot(ax=axs[1, 0])
    Cum_result.plot(ax=axs[1, 1])

    axs[0, 2].bar([x for x, y in series_sekw.iteritems()], [y for x, y in series_sekw.iteritems()])
    for i, v in enumerate(axs[0,2].patches):
        axs[0, 2].text(v.get_x() + v.get_width() / 2, v.get_height() + 5, str(int(v.get_height())), ha='center')

    axs[1, 2].bar(['Wins','Losses'],[season_wins, season_looses])
    for i, v in enumerate(axs[1,2].patches):
        axs[1, 2].text(v.get_x() + v.get_width() / 2, v.get_height() + 5, str(int(v.get_height())), ha='center')

    axs[0, 0].set_title('stake_for_round 1')
    axs[0, 1].set_title('Round_result 2')
    axs[1, 0].set_title('Round_loss_only 3', y=-0.3)
    axs[1, 1].set_title('Cum_result 4', y=-0.3)
    axs[0, 2].set_title('Sekw all season')
    axs[1, 2].set_title('Wins / Losses', y=-0.3)
    plt.show()

def show_pandas_table_plots(modelSeason):
    # first file
    df = modelSeason.df_season_stats
    html = df.style.set_table_attributes('style="font-size: 12px"').to_html()
    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        f.write(html.encode())
        filepath = f.name
    webbrowser.open('file://' + filepath)

    # second file
    df = pd.DataFrame(modelSeason.categories_by_round_all_season_dict)
    html = df.style.set_table_attributes('style="font-size: 12px"').to_html()
    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        f.write(html.encode())
        filepath = f.name
    webbrowser.open('file://' + filepath)


    # all teams df
    for x in modelSeason.list_of_obj_teams:
        df_team = x.df
        html = df_team.style.set_table_attributes('style="font-size: 12px"').to_html()

        # Save the HTML output to a temporary file
        with NamedTemporaryFile(delete=False, suffix='.html') as f:
            f.write(html.encode())
            filepath = f.name

        # Open the HTML file in the default web browser
        webbrowser.open('file://' + filepath)



