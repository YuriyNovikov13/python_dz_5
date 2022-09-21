# Реализуйте RLE алгоритм: реализуйте модуль сжатия и 
# восстановления данных.

def write_file(line:str, name:str):
    '''
    Запись строк в фаил
    '''
    with open(name, 'w', encoding="utf-8") as f:
        f.write(line)

def read_file(name:str):
    '''
    Чтение из файла
    '''
    with open(name, 'r', encoding="utf-8") as f:
        return f.read()


def get_encode(s): 
    encoding = '' 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1 
    return encoding

def get_decode(s): 
    decoding = '' 
    i = 0
    while i < len(s):
        num = ''
        while i + 1 < len(s) and s[i].isdigit() == True:
            num += s[i]
            i += 1
        decoding += int(num)*s[i]
        num = ''
        i += 1 
    return decoding

fail_name = 'file_task_04_05_1.txt'
string_input = read_file(fail_name)
fail_name_encode = 'file_task_05_05_2.txt'
string_input_encode = get_encode(string_input)
write_file(string_input_encode, fail_name_encode)
string_output = read_file(fail_name_encode)
string_output_decode = get_decode(string_output)

print(f'сжатие => {string_input_encode}')
print(f' восстановление => {string_output_decode}')