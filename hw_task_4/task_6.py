import numpy as np
import re


class DataAnalysis:
    content = []

    def __init__(self, file_path):
        self.file_path = file_path

    def file_reading(self):
        with open(self.file_path) as file:
            self.content = file.read().splitlines()
            return self.content

    def text_searching(self, pattern):
        match_list = []
        self.pattern = pattern
        for line in self.content:
            match_list.append(re.findall(self.pattern, line))
        return list(np.concatenate(match_list).flat)  # concatenate(list).flat - убирает вложенность


analysis = DataAnalysis('task_6.csv')
print(analysis.file_reading())
print(analysis.text_searching(r'@\w{1,30}'))
