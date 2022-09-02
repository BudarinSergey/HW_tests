import unittest
import main
import requests


class Test_funk(unittest.TestCase):
    def setUp(self) -> None:
        print("setup START")


    def test_create_folder(self):
        self.assertEqual(main.create_folder(path='test'), 201 )

    def test_create_folder_created(self):
        self.assertEqual(main.create_folder(path='test1'), 409 )

    def tearDown(self) -> None:
        requests.delete(f'{main.URL}?path={"test"}', headers=main.headers)
        print('tearDown  STOP')



