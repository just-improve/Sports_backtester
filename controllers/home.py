class HomeController:
    def __init__(self, modelSeason, modelSettings, view):
        self.modelSeason = modelSeason
        self.modelSettings = modelSettings
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()


    def _bind(self):
        self.frame.make_backtest_btn.config(command=self.printer)
        self.frame.test_btn.config(command=self.test_method_test_btn)


    def printer(self):
        self.store_settings()

    def test_method_test_btn(self):
        print('jestem test buttonem')
        print(self.modelSettings.cat1_prc)
        print(self.modelSettings.cat2_prc)
        print(self.modelSettings.cat3_prc)

    def store_settings(self):
        self.modelSeason.csv_file_name = self.frame.e_csv_file.get()
        self.modelSettings.avarage_odd = self.frame.e_avarage_odd_per_match.get()
        self.modelSettings.stake_per_team = self.frame.e_stake_per_team.get()
        self.modelSettings.category_progression_dict = {1: float(self.frame.e_cat_1.get()), 2: float(self.frame.e_cat_2.get()),
                                                        3: float(self.frame.e_cat_3.get()), 4: float(self.frame.e_cat_4.get())}


        print('')
