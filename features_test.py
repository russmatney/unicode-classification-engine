import unittest
import features

class TestFeatures(unittest.TestCase):

  def test_consonant_proportion(self):
    word = u'z\u016bgusyaa'
    proportion = features.consonant_proportion(word)
    self.assertEqual(proportion, 0.375)

  def test_consonant_proportion_empty_word(self):
    word = u''
    proportion = features.consonant_proportion(word)
    self.assertEqual(proportion, 0)

  def test_consonant_coda_0(self):
    word = u'lasso'
    coda = features.consonant_coda(word)
    self.assertEqual(coda, 0)

  def test_consonant_coda_1(self):
    word = u'lysoon'
    coda = features.consonant_coda(word)
    self.assertEqual(coda, 1)

if __name__ == '__main__':
	unittest.main()

