import unittest
from features import proportion,coda

class TestFeatures(unittest.TestCase):

  def test_consonant_proportion(self):
    word = u'z\u016bgusyaa'
    value = proportion.consonant_proportion(word)
    self.assertEqual(value, 0.375)

  def test_consonant_proportion_empty_word(self):
    word = u''
    value = proportion.consonant_proportion(word)
    self.assertEqual(value, 0)

  def test_consonant_coda_0(self):
    word = u'lasso'
    value = coda.consonant_coda(word)
    self.assertEqual(value, 0)

  def test_consonant_coda_1(self):
    word = u'lysoon'
    value = coda.consonant_coda(word)
    self.assertEqual(value, 1)

if __name__ == '__main__':
	unittest.main()

