import unittest
from core.main import main
from .fixtures import results

class TestGendiff(unittest.TestCase):
    def test_json_pretty(self):
        res = main(
            first='./tests/fixtures/before.json',
            second='./tests/fixtures/after.json'
            )
        self.assertEqual(res, results.pretty_json)

    def test_yaml_pretty(self):
        res = main(
            first='./tests/fixtures/before.yaml',
            second='./tests/fixtures/after.yaml'
            )
        self.assertEqual(res, results.pretty_yaml)

    def test_json_plain(self):
        res = main(
            first='./tests/fixtures/before.json',
            second='./tests/fixtures/after.json',
            format_='plain'
            )
        self.assertEqual(res, results.plain_json)

    def test_yaml_plain(self):
        res = main(
            first='./tests/fixtures/before.yaml',
            second='./tests/fixtures/after.yaml',
            format_='plain'
            )
        self.assertEqual(res, results.plain_yaml)
