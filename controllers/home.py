from calculations.creator_list_of_obj_teams import *
from calculations.creator_additional_season_stats import *
from calculations.first_round import *
from calculations.creator_category import *
from calculations.all_season_calculation import calculate_all_season_results
from plots.plot_result import plot_df_column, sub_plots, show_pandas_table_plots

class HomeController:
    def __init__(self, modelSeason, modelSettings, view):
        self.modelSeason = modelSeason
        self.modelSettings = modelSettings
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()


    def _bind(self):
        self.frame.make_backtest_btn.config(command=self.controller_method_organizer)
        self.frame.plot_result_btn.config(command=self.plot_result)
        self.frame.plot_graphs_btn.config(command=self.plot_graphs)
        self.frame.show_pandas_table_btn.config(command=self.show_pandas_table)

    def controller_method_organizer(self):
        self.frame.make_backtest_btn.configure(bg='green')
        self.store_settings()
        self.modelSeason.list_of_obj_teams = orgnizer_csv_formatter(self.modelSeason.csv_file_name)
        self.modelSeason.all_season_sekw = get_sekw_all_season(self.modelSeason.list_of_obj_teams)
        self.modelSeason.season_looses, self.modelSeason.season_wins = get_season_win_loss(self.modelSeason.all_season_sekw)
        calc_first_round_get_results(self.modelSeason.list_of_obj_teams, self.modelSettings, self.modelSeason)
        create_category_round(self.modelSeason.list_of_obj_teams, self.modelSeason)
        calculate_all_season_results(self.modelSeason.list_of_obj_teams, self.modelSeason, self.modelSettings)
        print('')

    def store_settings(self):
        self.modelSeason.csv_file_name = self.frame.e_csv_file.get()
        self.modelSettings.avarage_odd = float(self.frame.e_avarage_odd_per_match.get())
        self.modelSettings.stake_per_team = float(self.frame.e_stake_per_team.get())
        self.modelSettings.category_progression_dict = {1: float(self.frame.e_cat_1.get()), 2: float(self.frame.e_cat_2.get()),
                                                        3: float(self.frame.e_cat_3.get()), 4: float(self.frame.e_cat_4.get()),
                                                        5: float(self.frame.e_cat_5.get()), 6:float(self.frame.e_cat_6.get()),
                                                        7: float(self.frame.e_cat_7.get()), 8:float(self.frame.e_cat_8.get()),
                                                        9: float(self.frame.e_cat_9.get()), 10:float(self.frame.e_cat_10.get()),
                                                        11:float(self.frame.e_cat_11.get()), 12:float(self.frame.e_cat_12.get())
                                                        }

    def plot_result(self):
        plot_df_column(self.modelSeason.all_season_sekw)

    def plot_graphs(self):
        sub_plots(self.modelSeason.df_season_stats['Stake_for_round'], self.modelSeason.df_season_stats['Round_result'],
                  self.modelSeason.df_season_stats['Round_loss_only'], self.modelSeason.df_season_stats['Cum_result'],
                  self.modelSeason.all_season_sekw, self.modelSeason.season_wins, self.modelSeason.season_looses)

    def show_pandas_table(self):
        show_pandas_table_plots(self.modelSeason)
        print('das')



