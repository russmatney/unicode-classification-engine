import unittest
from features import proportion

class TestFeaturesProportion(unittest.TestCase):

  def test_consonant_proportion(self):
    word = u'z\u016bgusyaa'
    value = proportion.consonant_proportion(word)
    self.assertEqual(value, 0.375)

  def test_consonant_proportion_empty_word(self):
    word = u''
    value = proportion.consonant_proportion(word)
    self.assertEqual(value, 0)

  def test_vowel_proporition(self):
    word = u'z\u016bgusyaa'
    value = proportion.vowel_proportion(word)
    self.assertEqual(value, 0.625)

  def test_vowel_proportion_empty_word(self):
    word = u''
    value = proportion.vowel_proportion(word)
    self.assertEqual(value, 0)

  def test_obstruent_proporition(self):
    word = u'z\u016bgusyaa'
    value = proportion.obstruent_proportion(word)
    self.assertEqual(value, 0.375)

  def test_obstruent_proportion_empty_word(self):
    word = u''
    value = proportion.obstruent_proportion(word)
    self.assertEqual(value, 0)

if __name__ == '__main__':
	unittest.main()

