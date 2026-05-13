def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff_tree, parent_path=''):
    lines = []

    for key, node in diff_tree.items():
        path = key if parent_path == '' else f'{parent_path}.{key}'
        status = node['status']

        if status == 'nested':
            lines.extend(format_plain(node['children'], path))

        elif status == 'added':
            lines.append(
                f"Property '{path}' was added with value:"
                f" {format_value(node['value'])}"
            )

        elif status == 'removed':
            lines.append(
                f"Property '{path}' was removed"
            )

        elif status == 'updated':
            lines.append(
                f"Property '{path}' was updated. From {format_value(
                    node['old_value'])} to {format_value(node['new_value'])}"
            )

        elif status == 'same':
            pass

    return lines