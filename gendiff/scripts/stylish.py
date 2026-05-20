def format_value(value, level=0):
    indent = '    ' * level
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, level + 1)}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def stylish(node, level=0):
    lines = []
    indent = '    ' * level

    for key, item in node.items():
        status = item['status']
        if status == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.extend(stylish(item['children'], level + 1))
            lines.append(f"{indent}    }}")
        elif status == 'same':
            lines.append(f"{indent}    {key}: {format_value(item['value'])}")
        elif status == 'updated':
            lines.append(
                f"{indent}  - {key}: {format_value(
                    item['old_value'], level + 1
                )}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(
                    item['new_value'], level + 1
                )}"
            )
        elif status == 'added':
            lines.append(
                f"{indent}  + {key}: {format_value(item['value'], level + 1)}"
            )
        elif status == 'removed':
            lines.append(
                f"{indent}  - {key}: {format_value(item['value'], level + 1)}"
            )
    return lines

