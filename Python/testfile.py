
# dict1 = {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}
# dict2 = {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}
# palette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}

# result1 = dict( sorted( { key: [dict1[key]] + lst for key,lst in dict2.items() if key in dict1 }.items() ) ) 
# result2 = dict1 | palette_II 

# from itertools import chain

# testlist = [ [5], [1,2], [3,4] ]
# empty = set()
# TESTCONST1 = {"1", "2", "3"}
# TESTCONST2 = {"4", "5", "6"}

# const_list = [TESTCONST1, TESTCONST2]

# example_dishes = [
#                   {'salt', 'breadcrumbs', 'water', 'flour', 'celeriac', 'chickpea flour', 'soy sauce', 'parsley',
#                    'sunflower oil', 'lemon', 'black pepper'},

#                   {'cornstarch', 'salt', 'vegetable oil', 'sugar', 'vegetable stock', 'water', 'tofu', 'soy sauce',
#                    'lemon zest', 'lemon juice', 'black pepper', 'ginger', 'garlic'},

#                   {'salt', 'mixed herbs', 'silken tofu', 'smoked tofu', 'nutritional yeast', 'turmeric', 'soy sauce',
#                    'garlic', 'lemon juice', 'olive oil', 'black pepper', 'spaghetti'},

#                   {'salt', 'mushrooms', 'sugar', 'barley malt', 'nutritional yeast', 'fresh basil', 'olive oil',
#                    'honey', 'yeast', 'red onion', 'bell pepper', 'cashews', 'oregano', 'rosemary', 'garlic powder',
#                    'tomatoes', 'water', 'flour', 'red pepper flakes', 'garlic'},

#                   {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
#                    'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
#                    'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
#                    'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
#                    'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'},

#                   {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
#                    'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
#                    'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
#                    'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
#                    'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'}
#                   ]


# EXAMPLE_INTERSECTION = {'fresh red chili', 'sugar', 'nutritional yeast', 'fresh ginger', 'red chili powder', 'garlic',
#                         'olive oil', 'mashed potatoes', 'garam masala', 'clove powder', 'cumin powder', 'onion',
#                         'chickpea flour', 'water', 'turmeric powder', 'hing', 'black pepper', 'cinnamon powder',
#                         'cilantro', 'salt', 'oil', 'cardamom powder', 'turmeric', 'garlic paste', 'mustard seeds',
#                         'vinegar', 'mangoes', 'nigella seeds', 'serrano chili', 'flour', 'soy sauce', 'coriander seeds',
#                         'coriander powder', 'lemon juice', 'mango powder', 'curry leaves'}

# from collections import ChainMap

# print( set(ChainMap(*example_dishes)).difference(EXAMPLE_INTERSECTION) )

# {'vegetable oil', 'vegetable stock', 'barley malt', 'tofu', 'fresh basil', 'lemon', 'ginger', 'honey', 'spaghetti', 'cornstarch', 'yeast', 'red onion', 'breadcrumbs', 'mixed herbs', 'garlic powder', 'celeriac', 'lemon zest', 'sunflower oil', 'mushrooms', 'silken tofu', 'smoked tofu', 'bell pepper', 'cashews', 'oregano', 'tomatoes', 'parsley', 'red pepper flakes', 'rosemary'}

# {'honey', 'breadcrumbs', 'sunflower oil', 'cornstarch', 'smoked tofu', 'tomatoes', 'yeast', 'celeriac', 'oregano', 'red pepper flakes', 'ginger', 'bell pepper', 'lemon', 'mushrooms', 'barley malt', 'rosemary', 'spaghetti', 'mixed herbs', 'tofu', 'fresh basil', 'cashews', 'vegetable stock', 'vegetable oil', 'lemon zest', 'parsley', 'red onion', 'silken tofu', 'garlic powder'}

print(list({"test": 1}.keys()))