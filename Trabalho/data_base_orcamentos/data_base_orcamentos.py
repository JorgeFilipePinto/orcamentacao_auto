import json
import datetime

class DataBaseOrcamentos:
    
    def __init__(self, ficheiro=None):
        if ficheiro is None:
            self.ficheiro_db_orcamento = self.new_name()
        else:
            self.ficheiro_db_orcamento = ficheiro
        # Convenção para propriedades e métodos privados (python não tem metodos privados)
        self._max_name_size = 10
        self.total = 0
        self.total_impostos = 0
        self._dados_orcamento = {}

    def new_name(self):
        time = datetime.datetime.now()
        return 'orcamentos\\' + time.strftime('%Y-%m-%d_%Hh-%Mm-%Ss') + '.json'
        

    def import_dados(self):
        with open(self.ficheiro_db_orcamento, encoding='utf-8') as data_base:    #Importação do ficheiro dados.json e codificação dos caracteres
            self._dados_orcamento = json.load(data_base)
        self._update_max_name_size()


    def check_code(self, code):
        if code in self._dados_orcamento:
            return True
        return False        


    def get_elem_as_str(self, code):
        if not self.check_code(code):
            print(f"O código {code} não existe.")
            return ""
        
        return self._elem_to_str(code, self._dados_orcamento[code], True)


    def insert(self, code, quantity, store_db):
        if self.check_code(code):
            print(f"O código {code} já existe, vamos substituir pela nova quantidade.")

        if not store_db.check_code(code):
            print('O código não exite em loja!')
            return False

        item = store_db.get_item(code)
        self._dados_orcamento[code] = {
                                        'Name': item['Name'],
                                        'Quantity': quantity,
                                        'Price': item['Price']
                                        }
        self._max_name_size = max(len(store_db.get_item(code)["Name"]), self._max_name_size)
        return True


    def remove(self, code):
        if not self.check_code(code):
            print(f"O código {code} não existe.")
            return
        
        del self._dados_orcamento[code]
        self._update_max_name_size()


    def save(self):
        with open(self.ficheiro_db_orcamento, "w") as json_file:
            json.dump(self._dados_orcamento, json_file, indent=4)


    def is_empty(self):
        return not self._dados_orcamento.keys()




#periféricos do código

    def _elem_to_str(self, code, item, use_name_length=False):
        name_size = self._max_name_size
        if use_name_length:
            name_size = len(item["Name"])

        return f' {code:8s}  |  {item["Name"]:{name_size}s}  |  {item["Quantity"]:8d}  |  {item["Price"]:8.2f}€\n'


    def calcutate_totals(self):
        self.total = 0
        self.total_impostos = 0
        for code, item in self._dados_orcamento.items():
            self.total += item['Quantity'] * item['Price']

        self.total_impostos = self.total * 0.23

    def _update_max_name_size(self):
        self._max_name_size = max([len(elem["Name"]) for elem in self._dados_orcamento.values()])

 
    def __str__(self):
        string = f' {"Code":8s}  |  {"Name":{self._max_name_size}s}  |  {"Quantity":8s}  |  {"Price":6s}\n'
        string += '-'*(43+self._max_name_size)+'\n'
        for key, value in self._dados_orcamento.items():
            string += self._elem_to_str(key, value)
        string += f'\n{"IVA":6}= {self.total_impostos:.2f}€\n'
        string += f'{"Total":6s}= {self.total:.2f}€\n'
        return string




    
