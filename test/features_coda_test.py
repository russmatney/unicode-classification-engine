import unittest
from features import coda

class TestFeaturesCoda(unittest.TestCase):

  def test_consonant_coda_0(self):
    word = u'lasso'
    value = coda.consonant_coda(word)
    self.assertEqual(value, 0)

  def test_consonant_coda_1(self):
    word = u'lysoon'
    value = coda.consonant_coda(word)
    self.assertEqual(value, 1)

  def test_obstruent_coda_0(self):
    word = u'lysoon'
    value = coda.obstruent_coda(word)
    self.assertEqual(value, 0)

  def test_obstruent_coda_1(self):
    word = u'lysoop'
    value = coda.obstruent_coda(word)
    self.assertEqual(value, 1)

  #TODO: test for generic coda
  #TODO: Mock constants out of tests

if __name__ == '__main__':
	unittest.main()

