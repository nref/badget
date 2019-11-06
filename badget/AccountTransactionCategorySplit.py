import json

class AccountTransactionCategorySplit:

    def __init__(self, payee, category, memo, value):
        self.payee = payee
        self.category = category
        self.memo = memo
        self.value = value

    def __str__(self):
        return f'{json.dumps(self.__dict__, default=str, indent=4)}'

    @staticmethod
    def from_dict(d):
        ret = AccountTransactionCategorySplit(
            d.get('payee'),
            d.get('category'),
            d.get('memo'),
            float(d.get('value')))
        return ret
