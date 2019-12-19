import unittest
import number


class AllTestCase(unittest.TestCase):

    def test_is_file_exists(self):
        is_exists = False
        try:
            with open('shofiqul.txt') as f:
                is_exists = True
        except IOError:
            is_exists = False

        self.assertTrue(is_exists)

    def test_sample_count(self):
        cs = 0
        with open('shofiqul.txt', 'r') as f:
            line = f.readline()
            while line:
                # print(line.strip(), type(line))
                line = f.readline()
                cs += 1

        self.assertTrue(100 == cs)

    def test_is_half(self):
        self.assertTrue(50 == number.console_half())


if __name__ == '__main__':
    unittest.main()
