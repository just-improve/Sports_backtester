import pandas as pd


def get_sekw_all_season(list_of_obj_teams):
    count = 0
    first_sekw = None

    for obj_team in list_of_obj_teams:
        if count == 0:
            first_sekw = obj_team.sekw_count
        else:
            first_sekw = pd.concat([first_sekw, obj_team.sekw_count])
        count += 1
    grouped_series = first_sekw.groupby(level=0).sum()

    return grouped_series


def get_season_win_loss(pandas_series):
    missed_times = pandas_series.loc[0]
    hit_times = 0
    count = 0

    for num in range(len(pandas_series)):
        if count == 0:
            count += 1
            continue
        hit_times += pandas_series.iloc[num]

    return missed_times, hit_times