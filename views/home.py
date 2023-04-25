from tkinter import Frame, Label, Button, Entry


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        px = 5
        py = 2

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
        self.e_avarage_odd_per_match.insert(0, 0.9)

        self.category_settings_lab = Label(self, text="Sekwencje procenty")
        self.category_settings_lab.grid(row=3, column=0, padx=px, pady=py)  # sticky="ew"

        self.cat_1_lab = Label(self, text="Sekwencja 1")
        self.cat_1_lab.grid(row=4, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_1 = Entry(self)
        self.e_cat_1.grid(row=4, column=1, padx=px, pady=py)
        self.e_cat_1.insert(0, 1)

        self.cat_2_lab = Label(self, text="Sekwencja 2")
        self.cat_2_lab.grid(row=5, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_2 = Entry(self)
        self.e_cat_2.grid(row=5, column=1, padx=px, pady=py)
        self.e_cat_2.insert(0, 1.1)

        self.cat_3_lab = Label(self, text="Sekwencja 3")
        self.cat_3_lab.grid(row=6, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_3 = Entry(self)
        self.e_cat_3.grid(row=6, column=1, padx=px, pady=py)
        self.e_cat_3.insert(0, 1.2)

        self.cat_4_lab = Label(self, text="Sekwencja 4")
        self.cat_4_lab.grid(row=7, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_4 = Entry(self)
        self.e_cat_4.grid(row=7, column=1, padx=px, pady=py)
        self.e_cat_4.insert(0, 1.3)

        self.cat_5_lab = Label(self, text="Sekwencja 5")
        self.cat_5_lab.grid(row=8, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_cat_5 = Entry(self)
        self.e_cat_5.grid(row=8, column=1, padx=px, pady=py)
        self.e_cat_5.insert(0, 1.40)

        self.cat_6_lab = Label(self, text="Sekwencja 6")
        self.cat_6_lab.grid(row=9, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_6 = Entry(self)
        self.e_cat_6.grid(row=9, column=1, padx=px, pady=py)
        self.e_cat_6.insert(0, 1.5)

        self.cat_7_lab = Label(self, text="Sekwencja 7")
        self.cat_7_lab.grid(row=10, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_7 = Entry(self)
        self.e_cat_7.grid(row=10, column=1, padx=px, pady=py)
        self.e_cat_7.insert(0, 1.60)

        self.cat_8_lab = Label(self, text="Sekwencja 8")
        self.cat_8_lab.grid(row=11, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_8 = Entry(self)
        self.e_cat_8.grid(row=11, column=1, padx=px, pady=py)
        self.e_cat_8.insert(0, 1.7)

        self.cat_9_lab = Label(self, text="Sekwencja 9")
        self.cat_9_lab.grid(row=12, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_9 = Entry(self)
        self.e_cat_9.grid(row=12, column=1, padx=px, pady=py)
        self.e_cat_9.insert(0, 1.8)

        self.cat_10_lab = Label(self, text="Sekwencja 10")
        self.cat_10_lab.grid(row=13, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_10 = Entry(self)
        self.e_cat_10.grid(row=13, column=1, padx=px, pady=py)
        self.e_cat_10.insert(0, 1.9)

        self.cat_11_lab = Label(self, text="Sekwencja 11")
        self.cat_11_lab.grid(row=14, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_11 = Entry(self)
        self.e_cat_11.grid(row=14, column=1, padx=px, pady=py)
        self.e_cat_11.insert(0, 2)

        self.cat_12_lab = Label(self, text="Sekwencja 12")
        self.cat_12_lab.grid(row=15, column=0, padx=px, pady=py)  # sticky="ew"
        self.e_cat_12 = Entry(self)
        self.e_cat_12.grid(row=15, column=1, padx=px, pady=py)
        self.e_cat_12.insert(0, 2.1)

        self.make_backtest_btn = Button(self, text="Make backtest")
        self.make_backtest_btn.grid(row=16, column=0, padx=px, pady=py)

        self.plot_result_btn = Button(self, text="Plot Result")
        self.plot_result_btn.grid(row=17, column=0, padx=px, pady=py)

        self.plot_graphs_btn = Button(self, text="Plot graphs")
        self.plot_graphs_btn.grid(row=18, column=0, padx=px, pady=py)

        self.show_pandas_table_btn = Button(self, text="Show pandas table")
        self.show_pandas_table_btn.grid(row=19, column=0, padx=px, pady=py)


