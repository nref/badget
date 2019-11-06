import json

from datetime import datetime

from .AccountTransactionCategory import AccountTransactionCategory
from . import util

class AccountTransaction:

    def __init__(self, when, accountName, payee, isTransfer, memo, value, category):
        self.when = when
        self.accountName = accountName
        self.payee = payee
        self.isTransfer = isTransfer
        self.memo = memo
        self.value = value
        self.category = category

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'when': self.when,
            'accountName': self.accountName,
            'payee': self.payee,
            'isTransfer': self.isTransfer,
            'memo': self.memo,
            'value': self.value,
            'category': self.category.to_dict()
        }

    @staticmethod
    def from_dict(d):
        return AccountTransaction(
                    datetime.strptime(d.get('when'), util.time_format),
                    d.get('account'),
                    d.get('payee'),
                    d.get('isTransfer', False),
                    d.get('memo'),
                    float(d.get('value')),
                    AccountTransactionCategory.from_dict_or_str(d.get('category')))

    @staticmethod
    def get_all_in_dir(path):
        filenames = util.get_json_filenames_in_dir(path)
        
        transactions = []

        util.for_each_json_file_in_dir(path, lambda filename, json_dict: 
            transactions.append(AccountTransaction.from_dict(json_dict)))

        return transactions
