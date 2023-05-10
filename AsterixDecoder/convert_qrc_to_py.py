import sys
from PyQt5.QtCore import QResource

def convert_qrc_to_py(qrc_file, py_file):
    with open(qrc_file, 'r') as qrc:
        with open(py_file, 'w') as py:
            resource_data = qrc.read()
            resource = QResource()
            resource.loadFromData(resource_data.encode('utf-8'))
            py.write(resource.data().decode('utf-8'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python convert_qrc_to_py.py <input.qrc> <output.py>')
        sys.exit(1)

    qrc_file = sys.argv[1]
    py_file = sys.argv[2]
    
    convert_qrc_to_py(qrc_file, py_file)
