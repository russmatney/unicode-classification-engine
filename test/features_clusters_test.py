import unittest
from features import clusters

class TestFeaturesCoda(unittest.TestCase):

  def test_consonant_clusters_0(self):
    word = u'avavirisosh'
    value = clusters.consonant_clusters(word)
    self.assertEqual(value, 0)

  def test_consonant_clusters_1(self):
    word = u'avvirsosh'
    value = clusters.consonant_clusters(word)
    self.assertEqual(value, 2)

  def test_obstruent_clusters_0(self):
    word = u'avavirisosh'
    value = clusters.obstruent_clusters(word)
    self.assertEqual(value, 0)

  def test_obstruent_clusters_1(self):
    word = u'avvirsosh'
    value = clusters.obstruent_clusters(word)
    self.assertEqual(value, 1)

  def test_vowel_clusters_0(self):
    word = u'dd'
    value = clusters.vowel_clusters(word)
    #TODO: this

  def test_vowel_clusters_1(self):
    word = u'haeshi'
    value = clusters.vowel_clusters(word)
    self.assertEqual(value, 1)

  #TODO: test for generic clusters method
  #TODO: Mock constants out of tests

if __name__ == '__main__':
	unittest.main()

