import unittest
import tweet_cmd


def mock_raw_input_correct(value):
    return 'y'


def mock_raw_input_incorrect(value):
    return 'n'


class TestTweetCmd(unittest.TestCase):

    def test_validate_answer_1y(self):
        tweet_cmd.raw_input = mock_raw_input_correct
        self.assertEquals(1, tweet_cmd.validate_answer(1))

    def test_validate_answer_1n(self):
        tweet_cmd.raw_input = mock_raw_input_incorrect
        self.assertEquals(0, tweet_cmd.validate_answer(1))

    def test_validate_answer_0y(self):
        tweet_cmd.raw_input = mock_raw_input_correct
        self.assertEquals(0, tweet_cmd.validate_answer(0))

    def test_validate_answer_0n(self):
        tweet_cmd.raw_input = mock_raw_input_incorrect
        self.assertEquals(1, tweet_cmd.validate_answer(0))


if __name__ == '__main__':
    unittest.main()
