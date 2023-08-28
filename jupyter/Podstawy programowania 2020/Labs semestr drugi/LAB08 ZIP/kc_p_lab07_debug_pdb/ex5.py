#!/usr/bin/env python3

import lab7w


def get_file_info(full_fname):
    file_path = lab7w.get_path(full_fname)
    return file_path


filename = __file__
filename_path = get_file_info(filename)
print(f'path = {filename_path}')