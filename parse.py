def convert(json_string: str) -> dict:
    """Ускоренная версия с работой через список символов"""
    chars = list(json_string)
    pos = 0

    def skip_whitespace():
        nonlocal pos
        while pos < len(chars) and chars[pos] in (' ', '\n', '\r', '\t'):
            pos += 1

    def skip_chars():
        nonlocal pos
        skip_whitespace()
        while pos < len(chars) and chars[pos] in (',', ':'):
            pos += 1
            skip_whitespace()

    def parse_value():
        nonlocal pos
        skip_chars()

        if pos >= len(chars):
            return None

        if chars[pos] == '{':
            return parse_object()
        elif chars[pos] == '[':
            return parse_array()
        elif chars[pos] == '"':
            return parse_string()
        else:
            return parse_simple_value()

    def parse_object():
        nonlocal pos
        pos += 1  # Пропускаем {
        skip_whitespace()
        result = {}

        while pos < len(chars) and chars[pos] != '}':
            key = parse_string()
            skip_chars()  # Пропускаем :
            value = parse_value()
            if value is not None:
                result[key] = value
            skip_chars()  # Пропускаем ,

        if pos < len(chars) and chars[pos] == '}':
            pos += 1  # Пропускаем }
        return result

    def parse_array():
        nonlocal pos
        pos += 1  # Пропускаем [
        skip_whitespace()
        result = []

        while pos < len(chars) and chars[pos] != ']':
            value = parse_value()
            if value is not None:
                result.append(value)
            skip_chars()  # Пропускаем ,

        if pos < len(chars) and chars[pos] == ']':
            pos += 1  # Пропускаем ]
        return result

    def parse_string():
        nonlocal pos
        skip_whitespace()

        if pos >= len(chars) or chars[pos] != '"':
            return ""

        pos += 1  # Пропускаем "
        start = pos
        result_chars = []

        while pos < len(chars) and chars[pos] != '"':
            result_chars.append(chars[pos])
            pos += 1

        if pos < len(chars) and chars[pos] == '"':
            pos += 1  # Пропускаем закрывающую кавычку

        return ''.join(result_chars)

    def parse_simple_value():
        nonlocal pos
        skip_whitespace()
        start = pos

        while pos < len(chars) and chars[pos] not in (',', '}', ']', ' ', '\n', '\r', '\t'):
            pos += 1

        value_str = ''.join(chars[start:pos])

        if not value_str:
            return None
        elif value_str == 'true':
            return True
        elif value_str == 'false':
            return False
        elif value_str == 'null':
            return None
        elif value_str.isdigit():
            return int(value_str)
        else:
            # Для числовых значений с точкой
            try:
                return float(value_str)
            except ValueError:
                return value_str

    # Начинаем парсинг с корневого объекта
    skip_whitespace()
    if pos < len(chars) and chars[pos] == '{':
        return parse_object()
    else:
        return {}