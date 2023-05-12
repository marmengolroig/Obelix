import sys
from PyQt5 import uic

def convert_ui_to_py(ui_file, py_file):
    uic.compileUi(ui_file, open(py_file, 'w'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python convert_ui_to_py.py <input.ui> <output.py>')
        sys.exit(1)

    ui_file = sys.argv[1]
    py_file = sys.argv[2]
    
    convert_ui_to_py(ui_file, py_file)
