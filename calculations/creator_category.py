import pandas as pd

def create_category_round(list_obj, modelSeason):
    columns_round = []
    df_categories_by_round_outer = pd.DataFrame()
    for x in range(modelSeason.round_count):
        columns_round.append(str(x))

    for y in range(modelSeason.round_count):  #len(list_obj[0].df)
        df_round_category = pd.DataFrame()
        for team in list_obj:
            '''tutaj pokazuje aktualną kategorię danej drużyny i iteruje po każdej drużynie więc mamy całą kolejkę i trzeba teraz zapisać to do df i później zgrupować żeby było widać count'''
            df_round_category = pd.concat([df_round_category, pd.Series([team.df['sekw'][y]])], axis=1)
            # print('')

        counts = df_round_category.iloc[0].value_counts()
        df_categories_by_round_outer = pd.concat([df_categories_by_round_outer, counts], axis=1)

    df_categories_by_round_outer.columns = columns_round
    modelSeason.categories_by_round_all_season_dict = df_categories_by_round_outer.to_dict(orient='dict')