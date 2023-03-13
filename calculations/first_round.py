
def calc_first_round_get_results(list_of_obj, modelSettings, modelSeason):

    '''w pierwszej kolejce zapisujemy stawkę
    startową w każdym teamie i
    zapisujemy różniej zysk netto'''

    modelSeason.df_season_stats = modelSeason.df_season_stats.reindex(range(len(list_of_obj[0].df)))
    modelSeason.round_count = len(list_of_obj[0].df)
    for x in list_of_obj:
        x.df.loc[0, 'stake'] = modelSettings.stake_per_team
        if x.df['even'][0] == 0:
            x.df.loc[0,'zysk_netto'] = - modelSettings.stake_per_team
        elif x.df['even'][0] == 1:
            x.df.loc[0,'zysk_netto'] = modelSettings.stake_per_team * modelSettings.avarage_odd

    zysk_netto_1kolejka = calc_round_result(list_of_obj, 0)
    loss_only_1kolejka = calc_round_only_loss(list_of_obj, 0)

    modelSeason.df_season_stats['Round_result'][0] = zysk_netto_1kolejka
    modelSeason.df_season_stats['Round_loss_only'][0] = loss_only_1kolejka


def calc_round_result(list_of_obj, num_round):
    round_result = 0
    for x in list_of_obj:
        round_result += x.df['zysk_netto'][num_round]
    return round_result

def calc_round_only_loss(list_of_obj, num_round):
    round_result = 0
    for x in list_of_obj:
        if x.df['zysk_netto'][num_round]<0:
            round_result += x.df['zysk_netto'][num_round]
    return round_result