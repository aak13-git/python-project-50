from gendiff.scripts.gendiff import generate_diff

path_1 = './src/file1.json'
path_2 = './src/file2.json'
path_1_y, path_2_y = './src/file1.yaml', './src/file2.yaml'
new_path_1, new_path_2 = './src/new_file1.yaml', './src/new_file2.yaml'

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

