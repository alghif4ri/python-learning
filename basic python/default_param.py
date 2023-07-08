#def say_hello(first_name, last_name): #method tanpa default parameter
def say_hello(first_name="abudzar", last_name=""): #method dengan default parameter
    print(f"hallo {first_name} - {last_name}")

#say_hello("alghi") # error karena memiliki 2 parameter yang wajib diisi
#say_hello("alghi", "abu") # menampilkan value alghi dan abu
#say_hello() # menampilkan default parameter dengan value abudzar alghi
say_hello("aiman") # menampilkan value aiman dan default parameter alghi
say_hello() # menampilkan default parameter pada parameter pertama dan value fauzan pada parameter kedua
