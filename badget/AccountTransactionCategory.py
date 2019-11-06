import json

from .AccountTransactionCategorySplit import AccountTransactionCategorySplit

class AccountTransactionCategory:

    def __init__(self, name, split_transactions):
        self.name = name # None if there is a split
        self.split_transactions = split_transactions # None if there is no split

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'name': self.name,
            'split_transactions': None if self.split_transactions is None else [t.__dict__ for t in self.split_transactions]
        }

    @staticmethod
    def from_dict_or_str(o):
        name = None
        split_transactions = None

        if type(o) is str:
            name = o
        else:
            split = o.get('split', None)
            split_transactions = [AccountTransactionCategorySplit.from_dict(s) for s in split]
        
        return AccountTransactionCategory(name, split_transactions)