def dict_to_xml(data, root_tag='root', indent=0):
    """Конвертация Python словаря в XML с использованием формального подхода"""

    def escape_xml(text):
        """Экранирование XML специальных символов"""
        if not isinstance(text, str):
            text = str(text)
        return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&apos;'))

    def serialize_value(value, tag_name, current_indent):
        """Сериализация значения в XML"""
        spaces = '  ' * current_indent

        if value is None:
            return f"{spaces}<{tag_name} type='null'/>"
        elif isinstance(value, bool):
            return f"{spaces}<{tag_name} type='boolean'>{str(value).lower()}</{tag_name}>"
        elif isinstance(value, (int, float)):
            return f"{spaces}<{tag_name} type='number'>{value}</{tag_name}>"
        elif isinstance(value, str):
            escaped_value = escape_xml(value)
            return f"{spaces}<{tag_name} type='string'>{escaped_value}</{tag_name}>"
        elif isinstance(value, dict):
            return serialize_dict(value, tag_name, current_indent)
        elif isinstance(value, list):
            return serialize_list(value, tag_name, current_indent)
        else:
            escaped_value = escape_xml(value)
            return f"{spaces}<{tag_name} type='string'>{escaped_value}</{tag_name}>"

    def serialize_dict(obj, tag_name, current_indent):
        """Сериализация словаря в XML"""
        spaces = '  ' * current_indent
        result = [f"{spaces}<{tag_name} type='object'>"]

        for key, value in obj.items():
            # Создаем валидное имя тега из ключа
            safe_key = ''.join(c if c.isalnum() else '_' for c in str(key))
            result.append(serialize_value(value, safe_key, current_indent + 1))

        result.append(f"{spaces}</{tag_name}>")
        return '\n'.join(result)

    def serialize_list(arr, tag_name, current_indent):
        """Сериализация массива в XML"""
        spaces = '  ' * current_indent
        result = [f"{spaces}<{tag_name} type='array'>"]

        for i, item in enumerate(arr):
            result.append(serialize_value(item, f'item_{i}', current_indent + 1))

        result.append(f"{spaces}</{tag_name}>")
        return '\n'.join(result)

    return serialize_value(data, root_tag, indent)