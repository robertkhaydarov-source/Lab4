def parse_schedule_json(json_string: str) -> dict:
    """Парсинг JSON файла с расписанием"""
    # Заменяем JSON значения на Python эквиваленты
    json_string = (json_string
                   .replace('null', 'None')
                   .replace('true', 'True')
                   .replace('false', 'False'))

    # Парсим с помощью eval
    data = eval(json_string)
    return data
def get_student_info(data: dict) -> dict:
    """Получить основную информацию о студенте"""
    return {
        'university': data['university'],
        'group': data['group'],
        'id': data['id'],
        'name': data['name'],
        'surname': data['surname']
    }
def get_lessons_by_day(data: dict, day_name: str) -> list:
    """Получить занятия по дню недели"""
    for day in data['schedule']:
        if day['week_day'].lower() == day_name.lower():
            return day['lessons']
    return []
def get_all_teachers(data: dict) -> list:
    """Получить список всех преподавателей"""
    teachers = set()
    for day in data['schedule']:
        for lesson in day['lessons']:
            teachers.add(lesson['teacher'].strip())
    return sorted(list(teachers))


def get_lessons_count(data: dict) -> dict:
    """Посчитать количество занятий"""
    total_lessons = 0
    lessons_by_type = {}

    for day in data['schedule']:
        total_lessons += len(day['lessons'])
        for lesson in day['lessons']:
            lesson_type = lesson['lesson_type']
            lessons_by_type[lesson_type] = lessons_by_type.get(lesson_type, 0) + 1

    return {
        'total': total_lessons,
        'by_type': lessons_by_type
    }