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

