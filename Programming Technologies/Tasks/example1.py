log = '192.168.1.1 - - [11/Apr/2026:10:30:15] "GET /api/data HTTP/1.1" 200 512'
# 1. IP-адрес (от начала до первого пробела)
ip = log.split()[0] #список слов по пробелам и берем 1 элемент
# 2. Дата (находится внутри квадратных скобок)
start = log.find("[") + 1
end = log.find("]")
date_str = log[start:end] # Срез!
# 3. Размер ответа (последнее слово)
size = log.split()[-1] #последний элемент списка
# Форматируем красивый вывод
result = f"""
[ANALYSIS RESULT]
Source IP : {ip}
Event Date: {date_str.split(':')[0]} # Берем только дату без времени
Bytes Sent: {int(size) / 1024:.1f} KB
"""
print(result)