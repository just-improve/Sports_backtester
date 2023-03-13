import pandas as pd

class ModelSeason:
    def __init__(self):
        self.csv_file_name = None
        self.list_of_obj_teams = None
        self.all_season_sekw = None
        self.season_wins = None
        self.season_looses = None
        self.df_season_stats = pd.DataFrame(columns=['Stake_for_round', 'Round_result', 'Round_loss_only', 'Cum_loss',
                                                     'Cum_result'])
        self.categories_by_round_all_season_dict = {}
        self.round_count = None

class ModelSettings:
    def __init__(self):
        self.stake_per_team = None
        self.avarage_odd = None
        self.category_progression_dict = {}
