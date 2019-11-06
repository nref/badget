from . import util
from .Category import *

class CategoryGroup:

    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'name': self.name,
            'categories': [o.to_dict() for o in self.categories],
        }

    @staticmethod
    def get_all_in_dir(path):
        filenames = util.get_json_filenames_in_dir(path)

        category_groups = []

        def get_category_group(filename, json_dict):
            category_group = CategoryGroup(util.get_stem(filename), [Category.from_dict(d) for d in json_dict.get('categories')])
            category_groups.append(category_group)

        util.for_each_json_file_in_dir(path, get_category_group)

        return category_groups
