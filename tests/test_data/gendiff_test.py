from gendiff.scripts.gendiff import generate_diff

path_1 = './src/file1.json'
path_2 = './src/file2.json'

def test_gendiff():
    assert generate_diff(path_1, path_2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
