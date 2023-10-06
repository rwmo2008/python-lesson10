import shelve
db_file = shelve.open('letters', 'c')
db_file ['vowels'] = ['a','e','i','o','u']
db_file ['end'] = ['x','y','z']
db_file.close()
