import pandas as pd

sekwencja_aktualna = 'sekw'
sekwencja_wygrana = 'sekw_won'

def orgnizer_csv_formatter(file_name):
    '''it returns list of obj where one obj is one team with own df results'''
    df = create_correct_csv(file_name)
    list_of_teams = get_list_of_teams(df)
    list_of_obj = create_list_obj_teams(list_of_teams, df)
    return list_of_obj

def create_correct_csv(file_name):
    df = pd.read_csv(file_name)
    df = df.loc[:, ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
    df['even'] = df.apply(lambda row: create_odd_even_column(row['FTHG'], row['FTAG']), axis=1)
    return df

def create_odd_even_column(FTHG, FTAG):
    sum = FTHG + FTAG
    if sum % 2 == 1:
        return 0
    else:
        return 1

def get_list_of_teams(df):
    unique_elements = df['HomeTeam'].unique().tolist()
    return unique_elements

def create_list_obj_teams(list_of_teams, df):
    list_of_obj_teams = []
    for team_name in list_of_teams:
        df_arsenal = df.loc[df.eq(team_name).any(axis=1)]
        df_arsenal = df_arsenal.reset_index(drop=True)
        df_arsenal = create_new_col_based_on_value(df_arsenal)
        df_arsenal[sekwencja_aktualna] = df_arsenal[sekwencja_aktualna].astype(int)
        df_arsenal = create_sekw(df_arsenal)
        df_arsenal[sekwencja_wygrana] = df_arsenal[sekwencja_wygrana].astype(int)
        count = df_arsenal[sekwencja_wygrana].value_counts()
        team = Team(team_name, df_arsenal, count)
        list_of_obj_teams.append(team)

    return list_of_obj_teams

#wiaderny
def create_new_col_based_on_value(df):
    count = 0
    for i in range(0, len(df)):
        if df.loc[i, 'even'] == 1:
            count += 1
            df.loc[i, sekwencja_aktualna] = count
            count = 0

        if df.loc[i, 'even'] == 0:
            count += 1
            df.loc[i, sekwencja_aktualna] = count
    return df

def create_sekw(df):
    for i in range(0, len(df)):
        if df.loc[i, 'even'] == 1:
            df.loc[i, sekwencja_wygrana] = df.loc[i, sekwencja_aktualna]
        else:
            df.loc[i, sekwencja_wygrana] = 0
    return df

class Team:
    def __init__(self, name, df, sekw_count):
        self.name = name
        self.df = df
        self.sekw_count = sekw_count