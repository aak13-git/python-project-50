from gendiff.scripts.gendiff import generate_diff

path_1 = './tests/test_data/file1.json'
path_2 = './tests/test_data/file2.json'
path_1_y = './tests/test_data/file1.yaml'
path_2_y = './tests/test_data/file2.yaml'
new_path_1 = './tests/test_data/new_file1.yaml'
new_path_2 = './tests/test_data/new_file2.yaml'


def test_gendiff_json():
    assert generate_diff(path_1, path_2) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_gendiff_yaml():
    assert generate_diff(path_1_y, path_2_y) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_gendiff_yaml_new():
    assert generate_diff(new_path_1, new_path_2, 'stylish') == """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_gendiff_plain():
    assert generate_diff(new_path_1, new_path_2, 'plain') == (
        """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    )


def test_gendiff_format_json():
    assert generate_diff(new_path_1, new_path_2, 'json') == """[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting1",
        "type": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "type": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "type": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "type": "nested",
        "children": [
          {
            "key": "doge",
            "type": "nested",
            "children": [
              {
                "key": "wow",
                "type": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "type": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "type": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "type": "nested",
    "children": [
      {
        "key": "baz",
        "type": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "type": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "type": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]"""


def test_gendiff():
    assert generate_diff(new_path_1, new_path_2) == """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_gendiff_none():
    assert generate_diff(new_path_1, new_path_2, 'unknown') is None
