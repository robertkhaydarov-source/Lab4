def dict_to_yaml(data, indent=0):
    """Конвертация Python словаря в YAML с использованием формальной грамматики"""

    def serialize_value(value, current_indent):
        """Сериализация значения по грамматике YAML"""
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            return serialize_string(value)
        elif isinstance(value, dict):
            return serialize_dict(value, current_indent)
        elif isinstance(value, list):
            return serialize_list(value, current_indent)
        else:
            return str(value)

    def serialize_string(s):
        """Сериализация строки по грамматике YAML"""
        # Если строка содержит специальные символы, заключаем в кавычки
        if any(char in s for char in ':[]{}",&*#?|-<>=!%@\\'):
            return f'"{s}"'
        return s

    def serialize_dict(obj, current_indent):
        """Сериализация словаря по грамматике YAML"""
        if not obj:
            return "{}"

        lines = []
        spaces = '  ' * current_indent

        for key, value in obj.items():
            key_str = str(key)

            if isinstance(value, (dict, list)) and value:
                # Сложное значение - многострочный формат
                lines.append(f"{spaces}{key_str}:")
                nested_yaml = serialize_value(value, current_indent + 1)
                lines.append(nested_yaml)
            else:
                # Простое значение - однострочный формат
                value_str = serialize_value(value, current_indent)
                lines.append(f"{spaces}{key_str}: {value_str}")

        return '\n'.join(lines)

    def serialize_list(arr, current_indent):
        """Сериализация массива по грамматике YAML"""
        if not arr:
            return "[]"

        lines = []
        spaces = '  ' * current_indent

        for item in arr:
            if isinstance(item, (dict, list)) and item:
                # Сложный элемент массива
                lines.append(f"{spaces}-")
                item_yaml = serialize_value(item, current_indent + 1)
                # Добавляем отступ для многострочных элементов
                item_lines = item_yaml.split('\n')
                for i, line in enumerate(item_lines):
                    if not line.startswith('  ' * (current_indent + 1)):
                        item_lines[i] = '  ' + line
                lines.append('\n'.join(item_lines))
            else:
                # Простой элемент массива
                item_str = serialize_value(item, current_indent)
                lines.append(f"{spaces}- {item_str}")

        return '\n'.join(lines)

    return serialize_value(data, indent)