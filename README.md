# badget
Simple transactional budget app. The primary use case is to have a transactional record of budget category changes. Contrast this to e.g. YNAB which does not keep a log of budget category allocations.

## Example:

```
➜  python3 badget.py "./budgets/2019" -w "2019-12-01 12:30:00" -sc -sa -v 
{
    "name": "2019",
    "accounts": [
        {
            "name": "Mortgage",
            "budgeted": false,
            "credit": false,
            "closed": false
        },
        {
            "name": "Discover",
            "budgeted": true,
            "credit": true,
            "closed": false
        },
        {
            "name": "HSA",
            "budgeted": true,
            "credit": false,
            "closed": true
        },
        {
            "name": "Cash",
            "budgeted": true,
            "credit": false,
            "closed": false
        },
        {
            "name": "Checking",
            "budgeted": true,
            "credit": false,
            "closed": false
        }
    ],
    "account_transactions": [
        {
            "when": "2019-12-01 11:30:00",
            "accountName": "Checking",
            "payee": "",
            "isTransfer": false,
            "memo": "",
            "value": 2000.0,
            "category": {
                "name": "Starting Balance",
                "split_transactions": null
            }
        },
        {
            "when": "2019-12-01 12:30:00",
            "accountName": "Checking",
            "payee": "Example Inc",
            "isTransfer": false,
            "memo": "",
            "value": 2000.0,
            "category": {
                "name": null,
                "split_transactions": [
                    {
                        "payee": "Example Inc",
                        "category": "Unbudgeted",
                        "memo": "paycheck",
                        "value": 3000.0
                    },
                    {
                        "payee": "Example Inc",
                        "category": "Deductions/Taxes",
                        "memo": "paycheck",
                        "value": -1000.0
                    }
                ]
            }
        },
        {
            "when": "2019-12-01 13:30:00",
            "accountName": "Checking",
            "payee": "Cash",
            "isTransfer": true,
            "memo": "",
            "value": -2000.0,
            "category": {
                "name": "",
                "split_transactions": null
            }
        },
        {
            "when": "2019-12-01 16:30:00",
            "accountName": "Checking",
            "payee": "Discover",
            "isTransfer": true,
            "memo": "",
            "value": -500.0,
            "category": {
                "name": "",
                "split_transactions": null
            }
        }
    ],
    "category_groups": [
        {
            "name": "Medical",
            "categories": [
                {
                    "name": "Qualified",
                    "note": "Expenses using HSA card"
                }
            ]
        },
        {
            "name": "Deductions",
            "categories": [
                {
                    "name": "Taxes",
                    "note": "Paycheck taxes"
                }
            ]
        },
        {
            "name": "Savings",
            "categories": [
                {
                    "name": "Car Maintenance",
                    "note": "includes preventative and repairs"
                }
            ]
        }
    ],
    "budget_transactions": [
        {
            "when": "2019-12-01 11:30:00",
            "toCategory": "Savings/Car Maintenance",
            "fromCategory": "Medical/Qualified",
            "memo": "",
            "value": -100.0
        },
        {
            "when": "2019-12-01 12:30:00",
            "toCategory": "Savings/Car Maintenance",
            "fromCategory": "Unbudgeted",
            "memo": "",
            "value": 100.0
        }
    ]
}
Accounts:
{'Mortgage': 0, 'Discover': 0, 'HSA': 0, 'Cash': 0, 'Checking': 2000.0}
Categories:
{'Medical/Qualified': 100.0, 'Deductions/Taxes': 0, 'Savings/Car Maintenance': -100.0, 'Unbudgeted': 0}
```