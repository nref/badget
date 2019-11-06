import json
import os

from .Account import Account
from .AccountTransaction import AccountTransaction
from .BudgetTransaction import BudgetTransaction
from .Category import Category
from .CategoryGroup import CategoryGroup
from . import util

def filter_by_date(transactions, when = None):

    if when is not None:
        transactions = filter(lambda t: t.when < when, transactions)

    return transactions

def get_budget_dir(budget_name, dir_name):
    return os.path.join(budget_name, dir_name)

class Budget:

    def __init__(self, path):
        self.load(path)

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'name': self.name,
            'accounts': [o.to_dict() for o in self.accounts],
            'account_transactions': [o.to_dict() for o in self.account_transactions],
            'category_groups': [o.to_dict() for o in self.category_groups],
            'budget_transactions': [o.to_dict() for o in self.budget_transactions]
        }

    def load(self, path):
        accounts_dir = get_budget_dir(path, 'accounts')
        account_transactions_dir = get_budget_dir(path, 'account_transactions')
        category_groups_dir = get_budget_dir(path, 'category_groups')
        budget_transactions_dir = get_budget_dir(path, 'budget_transactions')

        self.name = util.get_stem(path)
        self.accounts = Account.get_all_in_dir(accounts_dir)
        self.account_transactions = AccountTransaction.get_all_in_dir(account_transactions_dir)
        self.category_groups = CategoryGroup.get_all_in_dir(category_groups_dir)
        self.budget_transactions = BudgetTransaction.get_all_in_dir(budget_transactions_dir)

        self.account_transactions.sort(key=lambda x: x.when)
        self.budget_transactions.sort(key=lambda x: x.when)

    def sum_account_transactions(self, when = None):
        transactions = filter_by_date(self.account_transactions, when)
        valid_transactions = filter(lambda t: self.is_valid_account_transaction(t), transactions)

        sums = {account.name: 0 for account in self.accounts}

        for transaction in valid_transactions:

            if transaction.isTransfer:
                sums[transaction.payee] -= transaction.value
            sums[transaction.accountName] += transaction.value
        
        return sums


    def sum_budget_transactions(self, when = None):
        transactions = filter_by_date(self.budget_transactions, when)
        valid_transactions = filter(lambda t: self.is_valid_budget_transaction(t), transactions)

        sums = {category: 0 for category in self.get_categories()}

        for transaction in valid_transactions:

            sums[transaction.fromCategory] -= transaction.value
            sums[transaction.toCategory] += transaction.value

        return sums

    def is_valid_account_transaction(self, transaction):
        accounts = [account.name for account in self.accounts]

        if transaction.accountName not in accounts:
            print(f'Error: account \'{transaction.accountName}\' does not exist')
            return False

        if transaction.isTransfer:
            if transaction.payee not in accounts:
                print(f'Error: account \'{transaction.payee}\' does not exist')
                return False

        return True
        
    def is_valid_budget_transaction(self, transaction):
        categories = self.get_categories()

        if transaction.toCategory not in categories:
            print(f'Error: category \'{transaction.toCategory}\' does not exist')
            return False

        if transaction.fromCategory not in categories:
            print(f'Error: category \'{transaction.fromCategory}\' does not exist')
            return False

        return True

    def get_categories(self):
        categories = [category_group.name + '/' + category.name for category_group in self.category_groups 
                                        for category in category_group.categories]
        categories.append('Unbudgeted')    
        
        return categories
