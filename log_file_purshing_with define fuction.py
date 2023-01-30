# 03/01/2023

import re
import time
from time import strftime


def main():
    log_file_path = 'sfbios_log.txt'
    # export_file_path=''
    time_now = str(
        strftime(
            '%Y-%m-%d %H-%M-%S',
            time.localtime()
        )
    )
    export_file = f'parsher_output{time_now}.txt'
    regex = '(<property name="(.*?)">(.*?)<\/property>)'
    parshData(log_file_path, export_file, regex, read_line=True)

    def parshData(log_file_path, export_file, regex, read_line=True):
        File = open(log_file_path, 'r')
        match_list = []
        if read_line == True:
            for line in File:
                find = re.finditer(regex, line, re.S)
                for match in find:
                    match_group = match.group()
                    match_list.append(match_group)

                    print(match_group)
        else:
            read_all = File.read()
            find = re.finditer(regex, read_all, re.S)

            for match in find:
                match_group = match.group()
                match_list.append(match_group)

        File.close()

        File = open(export_file, 'w+')
        File.write('This data exported data,created on}')
        clean_file = list(set(match_list))

        for item in range(0, len(clean_file)):
            print(clean_file[item])
            File.write(clean_file[item])
        File.close()
        return clean_file

    if __name__ == '__ main__':
        main()
