# import pickle

# l=[1,2,3,4,5,6,7,8]
# files="pickle.txt"
# file_obj=open(files,"wb")
# pickle.dump(l, file_obj)
# file_obj.close()




print("hello world")
import pickle
l=["Upendra","Aditya","Gaurav"]
o="Pickle1.txt"
file_obj=open(o,"wb")
files=pickle.dump(l,file_obj)
file_obj.close()

