import csv
from collections import Counter
from datetime import datetime as dt

from .constants import BASE_DIR, DATETIME_FORMAT, FILE_NAME, RESULT_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        result_dir = RESULT_DIR
        result_dir.mkdir(exist_ok=True)
        self.status_counter = Counter()

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DATETIME_FORMAT)
        file_name = FILE_NAME.format(time)
        file_path = BASE_DIR / 'results' / file_name

        results = [('Cтатус', 'Количество')]
        self.status_counter['Total'] = sum(self.status_counter.values())
        results.extend(self.status_counter.items())

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
