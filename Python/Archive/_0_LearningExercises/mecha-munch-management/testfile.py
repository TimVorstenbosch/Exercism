
from dict_methods import update_store_inventory

dict1 = {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
                          'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}

dict2 = {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False],
                          'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}

expected =  {'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False],
                         'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]},

print( update_store_inventory(dict1, dict2) )