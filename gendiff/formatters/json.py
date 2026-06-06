import json


def format_json(diff_tree):
    def to_json(node):
        result = []

        for key, item in node.items():
            status = item['status']

            if status == 'nested':
                result.append({
                    'key': key,
                    'type': 'nested',
                    'children': to_json(item['children'])
                })
            elif status == 'added':
                result.append({
                    'key': key,
                    'type': 'added',
                    'value': item['value']
                })
            elif status == 'removed':
                result.append({
                    'key': key,
                    'type': 'removed',
                    'value': item['value']
                })
            elif status == 'updated':
                result.append({
                    'key': key,
                    'type': 'changed',
                    'old_value': item['old_value'],
                    'new_value': item['new_value']
                })
            elif status == 'same':
                result.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': item['value']
                })

        return result

    return json.dumps(to_json(diff_tree), indent=2)