from gendiff.scripts.gendiff import generate_diff

path_1 = './src/file1.json'
path_2 = './src/file2.json'
path_1_y, path_2_y = './src/file1.yaml', './src/file2.yaml'

def test_gendiff_json():
    assert generate_diff(path_1, path_2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50cd
  + timeout: 20
  + verbose: True
}"""

def test_gendiff_yaml():
    assert generate_diff(path_1_y, path_2_y) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""


def test_gendiff_plain():
    assert generate_diff(new_path_1, new_path_2, 'plain') == """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""
