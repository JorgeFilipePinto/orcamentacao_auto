from data_base_manager.data_base_manager import DataBaseManager
from menu_manager.menu_manager import CoreApp


if __name__ == "__main__":                      #Verificação se este fecheiro foi corrido diretamento no PYTHON ( _name_ variavel de interpretador)
    store_db = DataBaseManager('base_de_dados/dados.json')
    store_db.import_dados()

    app = CoreApp(store_db)
    app.run()
