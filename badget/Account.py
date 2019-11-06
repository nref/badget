import json
from . import util

class Account:
    
    def __init__(self, name, budgeted, credit, closed):
        self.name = name
        self.budgeted = budgeted
        self.credit = credit
        self.closed = closed

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'name': self.name,
            'budgeted': self.budgeted,
            'credit': self.credit,
            'closed': self.closed
        }

    @staticmethod
    def from_dict(account_name, d):
        return Account(account_name,
                    d.get('budgeted', True), 
                    d.get('credit', False), 
                    d.get('closed', False))

    @staticmethod
    def get_all_in_dir(path):

        accounts = []
        
        util.for_each_json_file_in_dir(path, lambda filename, json_dict: 
            accounts.append(Account.from_dict(util.get_stem(filename), json_dict)))

        return accounts