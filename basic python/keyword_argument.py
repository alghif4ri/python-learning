#keyword argument list
#berfungsi untuk membuat suatu argument yang dinamis

#untuk mendifinisakan suatu keyword argument diawali dengan ** pada parameter
def create_html(tag, text, **attributes): 
    html = f"<{tag}"

#mengakses data keyword argument dengan for loop, disini keyword argumen diakses seperti data_dictionary
    for key, value in attributes.items():
        html = html + f" {key}:'{value}'"

    html = html + f">{text}</{tag}>"
    return html

#pada parameter ke-tiga dan ke-empat adalah value yang disimpan pada keyword argumen
html = create_html("p", "Hallo Alghi", style="underline", href="www.google.com")
print(html)
