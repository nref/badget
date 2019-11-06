import argparse
import sys
from datetime import datetime

import badget

def parse_args():
    parser = argparse.ArgumentParser(
        description='Simple transactional budget app',
        epilog=f'Example: python3 {sys.argv[0]} "./budgets/2019" -w "2019-12-01 12:30:00" -sc -sa -v')

    parser.add_argument('budget_dir', help='input budget directory')

    parser.add_argument('-w', '--when', nargs='?', 
        type=lambda s: datetime.strptime(s, badget.util.time_format), 
        help='Calculate using the given datetime. Format: ' 
            + badget.util.time_format.replace("%", "%%"))

    parser.add_argument('-sa', '--show_accounts',
        help='Show accounts',
        action="store_true")

    parser.add_argument('-sc', '--show_categories',
        help='Show categories',
        action="store_true")

    parser.add_argument('-v', '--verbose', 
        help='Show extra detail', 
        action="store_true")
    
    return parser.parse_args()

def show_accounts(budget, when):
    print('Accounts:')
    sums = budget.sum_account_transactions(when)
    print(sums)

def show_categories(budget, when):
    print('Categories:')
    sums = budget.sum_budget_transactions(when)
    print(sums)

def main():
    args = parse_args()

    budget = badget.Budget(args.budget_dir)

    if args.verbose:
        print(budget)

    if args.show_accounts:
        show_accounts(budget, args.when)

    if args.show_categories:
        show_categories(budget, args.when)

if __name__ == '__main__':
    main()