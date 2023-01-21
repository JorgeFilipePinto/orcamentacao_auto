
from data_base_manager.data_base_manager import DataBaseManager
from data_base_orcamentos.data_base_orcamentos import DataBaseOrcamentos


db = DataBaseOrcamentos()

store_db = DataBaseManager('base_de_dados\dados.json')
store_db.import_dados()
quantity = 12
db.insert("3332", quantity, store_db)
db.calcutate_totals()
db.save()
if not db.is_empty():
    print(db)
