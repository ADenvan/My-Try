import os
import sys
import requests

python_path = os.path.dirname(sys.executable)

python_version = sys.version

def main():
  pass
  return requests.get(url='https://google.com')

# В терминал .\main.py
print(f'ПИТЬ К ИНТЕРПРЕТАТОРУ {python_path}. ВЕРСИЯ {python_version}')

if __name__ == '__main__':
  print(main())