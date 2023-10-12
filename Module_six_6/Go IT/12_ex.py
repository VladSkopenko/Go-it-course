# Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data 
#зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із 
#закодованими парами username:password у вигляді:

# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bw

import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
def encode_data_to_base64(data):
    data_as_str = ", ".join(map(str,data))
    data_bytes = data_as_str.encode("utf-8")
    base64_bytes = base64.b64encode(data_bytes)
    base64_data = base64_bytes.decode('utf-8')
    return  base64_data 


print(encode_data_to_base64(data))
    