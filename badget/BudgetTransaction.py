import json

from datetime import datetime

from . import util

class BudgetTransaction:

    def __init__(self, when, toCategory, fromCategory, memo, value):
        self.when = when
        self.toCategory = toCategory
        self.fromCategory = fromCategory
        self.memo = memo
        self.value = value

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str)}'

    def to_dict(self):
        return {
            'when': self.when,
            'toCategory': self.toCategory,
            'fromCategory': self.fromCategory,
            'memo': self.memo,
            'value': self.value
        }

    @staticmethod
    def from_dict(d):
        return BudgetTransaction(
            datetime.strptime(d.get('when'), util.time_format),
            d.get('toCategory'),
            d.get('fromCategory'),
            d.get('memo'),
            float(d.get('value')))

    @staticmethod
    def get_all_in_dir(path):
        filenames = util.get_json_filenames_in_dir(path)

        budget_transactions = []

        util.for_each_json_file_in_dir(path, lambda filename, json_dict: 
            budget_transactions.append(BudgetTransaction.from_dict(json_dict)))

        return budget_transactions
