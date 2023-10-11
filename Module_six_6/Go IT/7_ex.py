# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

# Вимоги:

# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write

def sanitize_file(source, output):
    content = ""
    with open(source, "r") as source_file:
        for char in source_file.read():
            if  not char.isdigit():
                content += char
    with open(output, "w") as output_file:
        output_file.write(content)
    
    
        
        