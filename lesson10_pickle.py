import pickle
from lesson10_Time import Time

myTime1 = Time(1, 2, 3)
#out_file = open('C:/Users/rwmo2/Documents/Python Scripts/data.txt','wb')
pickled_time = pickle.dumps(myTime1)
#pickled_time = pickle.dump(myTime1, out_file)
#print(pickled_time)
#out_file.close()
unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()

in_file = open('data.txt', 'rb')
unpickled_time = pickle.load(in_file)
unpickled_time.print_time()
