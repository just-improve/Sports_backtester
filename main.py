from models.main import ModelSettings
from models.main import ModelSeason
from views.main import View
from controllers.main import Controller

def main():
    modelSeason = ModelSeason()
    modelSettings = ModelSettings()
    view = View()
    controller = Controller(modelSeason, modelSettings, view)
    controller.start()

if __name__ == "__main__":
    main()