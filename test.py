import unittest
from main import degree_format

class Test_Format(unittest.TestCase):

  def test_degree_format(self):
    formatted = degree_format('44')
    self.assertEqual(formatted, '44°C')

if __name__ == '__main__':
  unittest.main()