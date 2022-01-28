from collections import Counter

import collections
data = ['Ginger', 'Willow', 'Scout', 'Roscoe', 'Bear', 'Kobe', 'Baxter', 'Zara', 'Fiona', 'Milo', 'Oakley', 'Dakota', 'Prince', 'Bruno', 'Panda', 'Dexter', 'Ziggy', 'Roscoe', 'Lucy', 'Boomer', 'Fiona', 'Ella', 'Emma', 'Oakley']
counter = collections.Counter(data)

# Transforming into dictionary using dict()
counter_as_dict = dict(counter)

# Printing names in dictionary
print(counter_as_dict)