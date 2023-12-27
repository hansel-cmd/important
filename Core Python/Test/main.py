# from test_packages import multireader
from test_packages.multireader import MultiReader

reader = MultiReader('text_files/a.txt')
print(reader.read())
reader.close()

import test_packages