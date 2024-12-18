import re
import csv


#задание 1 
with open('task1-en.txt', encoding='utf-8') as file:
    text1 = file.read()
numbers = re.findall(r'\b(0|[1-9]\d*)(?:\.\d+)?\b', text1)
words = re.findall(r'\b\w{6}\b|\b\w{8}\b', text1)
print("Задание 1:")
print("Числа:", numbers)
print("Слова:", words)


#задание 2
with open('task2.html', encoding='utf-8') as file:
    text2 = file.read()
content = re.findall(r'content="([^"]+)"', text2)
print("Задание 2:", content)


#задание 3
with open('task3.txt', encoding='utf-8') as file:
    text3 = file.read()
site = re.findall(r'https?://[a-zA-Z0-9.-]+/', text3)
text3 = re.sub(r'https?://[a-zA-Z0-9.-]+/', ' ', text3)

date = re.findall(r'\d{4}-\d{2}-\d{2}', text3)
text3 = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', text3)

surname = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', text3)
text3 = re.sub(r'[A-Z][a-z]+(?!\d\d@|@)', ' ', text3)

email = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', text3)
text3 = re.sub(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', ' ', text3)

id = list(range(1, len(surname) + 1))
tabl = [['ID', 'Surname', 'Date', 'Email', 'Site']]
tabl += list(zip(id, surname, date, email, site))
output_file = 'task3_result.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(tabl)
print("Задание 3:")
print(f"Данные сохранены в файл {output_file}")
