#!/usr/bin/python3
import sys
import re

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_dict = {}
count, file_size = 0, 0

try:
    for line in sys.stdin:
        count += 1
        regex = r"[\d{1,3}\s\[:\]\.-]*\"[A-Z\s\/a-z]"
        regex += r"*\d{3}\s[A-Z]*\/1.1\" ([\w\d]*) ([\d]*)"
        data = re.search(regex, line)

        s_code, f_size = data.groups()
        file_size += int(f_size)
        if status_dict.get(s_code):
            status_dict[s_code] += 1
        elif s_code in status_codes:
            status_dict[s_code] = 1
        if count == 10:
            count = 0
            res = "File size: {}".format(file_size)
            for status_code in sorted(status_dict.keys()):
                res += "\n{}: {}".format(status_code, status_dict[status_code])
            print(res)

except KeyboardInterrupt:
    res = "File size: {}".format(file_size)
    for status_code in sorted(status_dict.keys()):
        res += "\n{}: {}".format(status_code, status_dict[status_code])
    print(res)
    raise KeyboardInterrupt
