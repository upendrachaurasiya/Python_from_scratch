# import pickle
# files="pickle.txt"
# file_obj=open(files,"rb")
# number=pickle.load(file_obj)
# print(number)
# file_obj.close()



import pickle
file_obj=open("pickle1.txt","rb")
watch=pickle.load(file_obj)

watch.append("ram")
print(watch)
file_obj.close()

