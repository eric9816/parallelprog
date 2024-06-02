import threading as th
from glob import glob
from pathlib import Path
from time import perf_counter, sleep
import random


class EricThread(th.Thread):
    def __init__(self, file):
        super().__init__()
        self.source_file = file

        source_path = Path(self.source_file)
        result_path = source_path.parent / 'result'
        new_name = source_path.stem + '_new.txt'
        self.new_file = result_path / new_name
        self.warning_text = "!!! WARNING INFECTED !!!"

    def run(self) -> None:
        sleep(1)
        with open(self.source_file, 'r', encoding='utf-8') as source, open(self.new_file, 'w', encoding='utf-8') as new:
            for line in source:
                if self.find_anton(line):
                    #content = line.replace(line, self.warning_text)
                    new.write(self.warning_text)
                else:
                    new.write(line)

    @staticmethod
    def find_anton(line:  str) -> bool:
        line = line.replace(' ', '')
        line = line.strip()

        name = 'anton'
        result = []

        for letter in line:
            letter = letter.lower()
            if letter in name:
                result.append(letter)
        result_str = ''.join(result)

        if name in result_str:
            return True

        return False

start = perf_counter()
threads = [
    EricThread(file) for file in glob(r'C:\Users\PC\PycharmProjects\parallelprog\thead\class_threads\anton\*.txt')
]

for thread in threads:
    thread.start()
end = perf_counter() - start

print(end)
