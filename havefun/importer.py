print('doing something before importing...')

import importee

print('Hello from importer!',__name__)

importee.someFunction()
