
import json

class DataBaseManager:

    def __init__(self, ficheiro):
        self.ficheiro_db = ficheiro
        # Convenção para propriedades e métodos privados (python não tem metodos privados)
        self._max_name_size = 10
        self._dados = {}

    def get_item(self, code):
        if self.check_code(code):
            return self._dados[code]
        return None

    def __str__(self):
        string = f' {"Code":8s}  |  {"Name":{self._max_name_size}s}  |  {"Price":6s}\n'
        for key, value in self._dados.items():
            string += self._elem_to_str(key, value)
        return string
    
    def _elem_to_str(self, code, value, use_name_length=False):
        name_size = self._max_name_size
        if use_name_length:
            name_size = len(value["Name"])

        return f' {code:8s}  |  {value["Name"]:{name_size}s}  |  {value["Price"]:8.2f}€\n'


    def _update_max_name_size(self):
        self._max_name_size = max([len(elem["Name"]) for elem in self._dados.values()])

    def get_elem_as_str(self, code):
        if not self.check_code(code):
            print(f"O código {code} não existe.")
            return ""
        
        return self._elem_to_str(code, self._dados[code], True)

    def insert(self, code, item_name, price):
        if self.check_code(code):
            print(f"O código {code} já existe, foi impossível adicionar.")
            return False
        
        self._dados[code] = {"Name": item_name, "Price": price}
        self._max_name_size = max(len(item_name), self._max_name_size)
        return True
    
    def remove(self, code):
        if not self.check_code(code):
            print(f"O código {code} não existe.")
            return
        
        del self._dados[code]
        self._update_max_name_size()
    
    def update(self, code, name, price):
        if not self.check_code(code):
            print(f"O código {code} não existe.")
            return False
        
        self._dados[code] = {"Name": name, "Price": price}
        self._update_max_name_size()
        return True
    
    def check_code(self, code):
        if code in self._dados:
            return True
        return False

    def import_dados(self):
        with open(self.ficheiro_db, encoding='utf-8') as data_base:    #Importação do ficheiro dados.json e codificação dos caracteres
            self._dados = json.load(data_base)
        self._update_max_name_size()
    
    def save(self):
        with open(self.ficheiro_db, "w") as json_file:
            json.dump(self._dados, json_file, indent=4)
    