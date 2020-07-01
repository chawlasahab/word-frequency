import unittest
from WordFrequency import pre_process, count_words, sort_words_by_count


class Test(unittest.TestCase):
    def test_pre_process(self):
        test_string = "This [is] a (sample) 100 @$string's, where we will test-string preprocessing ."
        expected_output = "this is a sample string s where we will test string preprocessing"
        result = pre_process(test_string)
        self.assertEqual(str(result), expected_output)

    def test_count_words(self):
        test_string = "this is a sample string of word frequency this string count word count or frequency of each string"
        expected_output = {'this': 2, 'sample': 1, 'string': 3, 'word': 2, 'frequency': 2, 'count': 2, 'each': 1}
        result = count_words(test_string)
        self.assertEqual(result, expected_output)

    def test_sort_words_by_count(self):
        test_word_count_dict = {'this': 2, 'sample': 1, 'string': 3, 'word': 2, 'frequency': 2, 'count': 2, 'each': 1}
        expected_output = [('string', 3), ('this', 2), ('word', 2), ('frequency', 2), ('count', 2), ('sample', 1), ('each', 1)]
        result = sort_words_by_count(test_word_count_dict)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
