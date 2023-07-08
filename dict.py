#data dictionary

#{"key":"value"}
# mendefinisikan variable "customer" dengan value data_dictionary
customer = {"Name":"Alghi","Age":29,"Address":"Bogor"} 

# mendefinisikan variable "name" dengan mengambil data dari data_dictionary yang telah dibuat
name = customer["Name"] 
age = customer["Age"]
address = customer["Address"]

# menampilkan value data_dictionary dengan for loop
for key in customer:
    value = customer[key]
    print(f"{key}:{value}")

print("================")

# lebih simple menggunakan items(), mengubah isi data_dictionary menjadi tuple
print(customer.items())
for key in customer.items():
    print(f"{key[0]}:{key[1]}")

print("================")

# menggunakan items() agar value di ekstrak menjadi 2 variable
for key,value in customer.items():
    print(f"{key}:{value}")

#operasi yang dapat dilakukan pada data dictionary
# customer["Add"] = "X" # add dan update 
# del customer['Address'] # hapus
# for key,value in customer.items():
#     print(f"{key}:{value}")
