# import semua method/function yang ada dalam file function
import function

# memanggil function yang diimport harus menggunakan prefix nama file jika import tidak spesifik
hello = function.say_hello("alghi")
total = function.total(10, 5, 10)

# import spesifik method/function yang ada dalam file function
from function import say_hello
from function import total

#jika import method/function secara spesifik maka tidak perlu menuliskan prefix file
hello = say_hello("alghi")
total = total(10, 5, 10)
print(hello)
print(total)
