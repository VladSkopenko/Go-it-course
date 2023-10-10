# Робота с файлами

file = open("text.txt", "w", encoding="UTF-8")
file.write("Hello world\n")
file.write("Hello Ukrein\n")
file.writelines(["Hi Vova\n", "Hi Vlad\n", "Hi Milana \n"])
file.close()
