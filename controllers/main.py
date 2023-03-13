from models.main import ModelSeason, ModelSettings
from views.main import View
from .home import HomeController


class Controller:
    def __init__(self, modelSeason: ModelSeason, modelSettings: ModelSettings, view: View):
        self.view = view
        self.modelSeason = modelSeason
        self.modelSettings = modelSettings

        self.home_controller = HomeController(modelSeason, modelSettings, view)

    def start(self):
        self.view.start_mainloop()