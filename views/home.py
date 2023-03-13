from tkinter import Frame, Label, Button, Entry


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        px = 5
        py = 5

        # self.grid_columnconfigure(0, weight=1)
        self.csv_lab = Label(self, text="Csv file name")
        self.csv_lab.grid(row=0, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_csv_file = Entry(self)
        self.e_csv_file.grid(row=0, column=1, padx=px, pady=py)
        self.e_csv_file.insert(0, 'premier21.csv')

        self.stake_per_team_lab = Label(self, text="Stawka na drużyne")
        self.stake_per_team_lab.grid(row=1, column=0, padx=px, pady=py)   #sticky="ew"

        self.e_stake_per_team = Entry(self)
        self.e_stake_per_team.grid(row=1, column=1, padx=px, pady=py)
        self.e_stake_per_team.insert(0, 10)

        ##
        self.avarage_odd_per_match = Label(self, text="Kurs")
        self.avarage_odd_per_match.grid(row=2, column=0, padx=px, pady=py)   #sticky="ew"

        self.e_avarage_odd_per_match = Entry(self)
        self.e_avarage_odd_per_match.grid(row=2, column=1, padx=px, pady=py)
        self.e_avarage_odd_per_match.insert(0, 1.9)

        self.category_settings_lab = Label(self, text="Kategorie procenty")
        self.category_settings_lab.grid(row=3, column=0, padx=px, pady=py)  # sticky="ew"

        self.cat_1_lab = Label(self, text="Kategoria 1")
        self.cat_1_lab.grid(row=4, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_1 = Entry(self)
        self.e_cat_1.grid(row=4, column=1, padx=px, pady=py)
        self.e_cat_1.insert(0, 1)

        self.cat_2_lab = Label(self, text="Kategoria 2")
        self.cat_2_lab.grid(row=5, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_2 = Entry(self)
        self.e_cat_2.grid(row=5, column=1, padx=px, pady=py)
        self.e_cat_2.insert(0, 1.1)

        self.cat_3_lab = Label(self, text="Kategoria 3")
        self.cat_3_lab.grid(row=6, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_3 = Entry(self)
        self.e_cat_3.grid(row=6, column=1, padx=px, pady=py)
        self.e_cat_3.insert(0, 1.2)

        self.cat_4_lab = Label(self, text="Kategoria 4")
        self.cat_4_lab.grid(row=7, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_4 = Entry(self)
        self.e_cat_4.grid(row=7, column=1, padx=px, pady=py)
        self.e_cat_4.insert(0, 1.3)


        self.make_backtest_btn = Button(self, text="Make backtest")
        self.make_backtest_btn.grid(row=20, column=0, padx=px, pady=py)


