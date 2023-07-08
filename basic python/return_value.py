def total(*listnumber):
    number = 0
    for no in listnumber:
        number = number + no
    # return number #satu variable yang direturn
    # jika lebih dari satu maka bisa dengan TUPLE ()
    return (listnumber, number)


# memanggil nilai dari return yang dimasukan ke dalam TUPLE dipisah dengan koma(,)
listnumber, number = total(10, 20)
print(f"Total {listnumber} = {number}")
