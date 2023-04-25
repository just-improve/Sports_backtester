from calculations.first_round import calc_round_only_loss
from calculations.first_round import calc_round_result
import math



'''Calculating all season stats - main method'''
def calculate_all_season_results(list_of_obj, modelSeason, modelSettings):
    count = 0
    '''iteracja kolejek'''
    for x in range(modelSeason.round_count):

        '''we skip first round '''
        if count == 0:
            count += 1
            continue

        '''calculating stake for next round for all teams'''
        modelSeason.df_season_stats['Cum_loss'] = modelSeason.df_season_stats['Round_loss_only'].cumsum()
        previous_round_loss = modelSeason.df_season_stats['Round_loss_only'][x-1]
        # stake_for_round = previous_round_loss * modelSettings.calc_stake_for_next_round
        # stake_for_round = modelSeason.df_season_stats['Cum_loss'][x-1]
        stake_for_round = 200
        modelSeason.df_season_stats['Stake_for_round'][x] = stake_for_round

        '''kalkulacja stawek na kategorie'''
        stawki_na_kategorie_dict = calculate_stake_for_team_based_on_category(modelSeason, modelSettings, x)

        '''zapisanie stawki w drużynach w zależności od kategorii na której jest drużyna'''
        for team in list_of_obj:
            team_sekw = team.df['sekw'][x]
            team.df.loc[x,'stake'] = stawki_na_kategorie_dict[team_sekw]

        '''kalkulacja wyniku - działa poprawnie'''
        calc_team_result(list_of_obj, x, modelSettings)

        '''kalkulacja modelSeason.df_season_stats['Round_loss_only']'''
        modelSeason.df_season_stats.loc[x, 'Round_result'] = calc_round_result(list_of_obj, x)
        modelSeason.df_season_stats.loc[x, 'Round_loss_only'] = calc_round_only_loss(list_of_obj, x)

        # modelSeason.df_season_stats['Cum_result'] = modelSeason.df_season_stats['Round_result'].cumsum()
    '''after season stats'''
    modelSeason.df_season_stats['Cum_result'] = modelSeason.df_season_stats['Round_result'].cumsum()
    calc_every_team_result(list_of_obj)



'''jak jest obliczana stawka na kolejkę'''
'''w zależności od sekwencji znając stawkę na kolejkę obliczamy ile postawić na każdą drużynę'''

def calculate_stake_for_team_based_on_category(modelSeason, model_settings, round):
    kategoria_rundy = modelSeason.categories_by_round_all_season_dict[str(round)]
    stawka_na_runde = modelSeason.df_season_stats['Stake_for_round'][round]
    mpk = model_settings.category_progression_dict
    sum_kategorii = 0
    stawka_na_team_wedlug_kategorii_kolejki = {}
    for key, value in kategoria_rundy.items():
        if math.isnan(value):
            continue
        else:
            sum_kategorii += (value * mpk[key])
    for key, value in kategoria_rundy.items():
        stawka_na_team_wedlug_kategorii_kolejki[key] = abs((value*model_settings.category_progression_dict[key]/sum_kategorii) * stawka_na_runde / value)

    return stawka_na_team_wedlug_kategorii_kolejki


def calc_team_result(list_of_obj, num_round, modelSettings):
    for x in list_of_obj:
        if x.df['even'][num_round] == 0:
            x.df.loc[num_round, 'zysk_netto'] = - x.df.loc[num_round, 'stake']

        elif x.df['even'][num_round] == 1:
            x.df.loc[num_round, 'zysk_netto'] = x.df.loc[num_round, 'stake'] * modelSettings.avarage_odd

def calc_every_team_result(list_of_team_obj):
    for team in list_of_team_obj:
        team.df['CumResult'] = team.df['zysk_netto'].cumsum()