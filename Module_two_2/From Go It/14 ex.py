# Ситуація проста, вам необхідно вирахувати кількість SMS, які треба надсилати в одному пакеті розсилки потенційним покупцям.
# Всього на день виділяється 1000 платних SMS для кампанії маркетингу pool=1000.
# Співробітник відділу маркетингу вводить кількість розсилок quantity, і ви обчислюєте розмір пакета chunk = pool // quantity.
# Опрацюйте помилку поділу на нуль.