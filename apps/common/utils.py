import csv
from typing import List, Dict

from apps.common.exceptions import NoDataException, ValidationError
from apps.common.models import IntListModel


def export_to_csv(data: List[Dict], filename: str = 'results_group_by_10.csv') -> None:
    csv_writer = csv.writer(open(filename, 'w'))
    if not data:
        raise NoDataException("No data")
    csv_writer.writerow(data[0].keys())
    for row in data:
        csv_writer.writerow([item for item in row.values()])


class MyList:
    def __init__(self, start: int = 28, end: int = 117, step: int = 7):
        try:
            IntListModel(start=start, end=end, step=step)
        except ValueError as err:
            raise ValidationError(str(err))

        self.my_list = list(range(start, end - 1, step))

    @property
    def length(self):
        return len(self.my_list)

    @property
    def average(self) -> float:
        return sum(self.my_list) / self.length

    def get_sum_of_powered_elements(self, pow_range: int = 3) -> int:
        return sum([pow(item, pow_range) for item in self.my_list])
