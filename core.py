from functools import reduce
import os
import requests


def get_cwd():
    return os.getcwd()


def read_from_file(filename):
    with open(filename) as f:
        result = f.read()
    return result


class MockTester1:

    def __init__(self, url):
        self.url = url

    def get_data_from_url(self):
        try:
            response = requests.get(self.url)
        except Exception as exc:
            print(f'We got an exception: {exc}')
        else:
            return response.json()

class MockTester2:

    def __init__(self):
        self.retriever = MockTester1('AAA')

    def process_data(self):
        data = self.retriever.get_data_from_url()
        return reduce(lambda x, y: x+y, data)

    def some(self):
        return 'WORK {}'.format(self.retriever)


