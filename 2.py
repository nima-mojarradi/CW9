import pickle
class Person():
    def __init__(self,
                name,
                age,
                address):
            self.name = name
            self.age = age
            self.address = address

def pickling(obj_list):
    picle_list = open('list.pickle', "wb")
    pickle.dump(obj_list,picle_list)
    picle_list.close()

def unpickling(pickle_list_file):
    picle_file = open(pickle_list_file, "rb")
    obj_list = pickle.load(picle_file)
    return(obj_list)
    
