from bmn import parse_schedule_json
from dop1 import dict_to_yaml
from dop3 import dict_to_xml
from parse import convert
import time
import json
import yaml
json_content = '''{
    "university": "ITMO",
    "group": "P3118", 
    "id":"501445",
    "name":"Роберт",
    "surname":"Хайдаров",
    "schedule": [
       {  
     "week_day": "Среда",
         "date": "2025-11-19",
         "lessons": [
          {
            "number": 1,
            "time_start": "11:30",
            "time_end": "13:00",
            "subject": "Информатика",
            "lesson_type": "Лекция", 
            "teacher": "Балакшин Павел Валерьевич",
            "classroom": "Актовый зал (1216/0 (усл))",
            "building": "ул.Ломоносова, д.9, лит. М"
          },
          {
            "number": 2,
            "time_start": "13:30", 
            "time_end": "15:00",
            "subject": "Основы профессиональной деятельности",
            "lesson_type": "Лекция",
            "teacher": "Клименков Сергей Викторович",
            "classroom": "Актовый зал (1216/0 (усл))",
            "building": "ул.Ломоносова, д.9, лит. М"
          }
        ]
      },
      {  
     "week_day": "Пятница",
         "date": "2025-11-21", 
         "lessons": [
          {
            "number": 1,
            "time_start": "11:30",
            "time_end": "13:00",
            "subject": "English A2 / Английский язык A2",
            "lesson_type": "Практика",
            "teacher": "Малышева Алёна Андреевна",
            "classroom": "Ауд. 2412",
            "building": "Кронверкский пр., д.49, лит.А"
          },
          {
            "number": 2,
            "time_start": "13:30",
            "time_end": "15:00", 
            "subject": "English A2 / Английский язык A2",
            "lesson_type": "Практика",
            "teacher": "Малышева Алёна Андреевна",
            "classroom": "Ауд. 2412",
            "building": "Кронверкский пр., д.49, лит.А"
          }
        ]
      }
    ]   	
}'''
results = {}

# Тест 1: Самописный JSON + самописный YAML
start = time.time()
for _ in range(100):
    data = convert(json_content)  # твой самописный парсер
    yaml_output = dict_to_yaml(data)  # твой самописный YAML
results['Самописный JSON+YAML'] = time.time() - start

# Тест 2: Самописный JSON + самописный XML
start = time.time()
for _ in range(100):
    data = convert(json_content)
    xml_output = dict_to_xml(data)  # твой самописный XML
results['Самописный JSON+XML'] = time.time() - start

# Тест 3: Библиотечный JSON + библиотечный YAML
start = time.time()
for _ in range(100):
    data = json.loads(json_content)  # библиотечный парсер
    yaml_output = yaml.dump(data, allow_unicode=True)  # библиотечный YAML
results['Библиотечный JSON+YAML'] = time.time() - start

# Вывод результатов
print("📊 РЕЗУЛЬТАТЫ ПРОИЗВОДИТЕЛЬНОСТИ (100 итераций):")
for name, time_taken in results.items():
    print(f"{name}: {time_taken:.4f} сек")

dop2=json.loads(json_content)
dop2Yaml=yaml.dump(dop2, allow_unicode)
#print(parse_schedule_json(json_content))
# print(convert(json_content))
#print(dict_to_yaml(convert(json_content)))
#print(dict_to_xml(convert(json_content)))
#print(dop2Yaml)

