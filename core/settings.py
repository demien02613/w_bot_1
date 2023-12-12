
import sys
import os
import configparser
# ============================================================================
sys.stdout.reconfigure(encoding='utf-8')
envF = 'input.env'  # название файла с конфигурацией
# ============================================================================


def exists(path):  # проверяем, есть ли файл с конфигураци
    try:
        os.stat(path)
    except OSError:
        return False
    return True
# ============================================================================


if exists(envF) == False:  # если файл с конфигурацией не существует, create
    print(f'{envF} не найден, создаем...')
    with open(envF, 'w') as file:
        file.write('[Bot]\nTOKEN = 12345678:AaBbCcDdEeFf \nADMIN_ID =')
# ============================================================================
config = configparser.ConfigParser()  # создаём объекта парсера
config.read(envF)  # читаем конфиг
sss = config.sections()
for ss in sss:
    # print(f'[{ss}]')
    for key, value in config.items(ss):
        # generate new dynamic values
        code = f"{ss.upper()+'_'+key.upper()} = '{value}'"
        # print(code)
        exec(code)
        # print('', key, ' --> ', value)
# ============================================================================
