import unittest
import challenges


class NamesTestCase(unittest.TestCase):
    """Tests for all challenges."""

    def test_numIdenticalPairs(self):
        """Will the numIdenticalPairs function return the proper number of correct iterations?"""
        combos_1 = challenges.Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3])
        combos_2 = challenges.Solution().numIdenticalPairs([1, 1, 1, 1])
        combos_3 = challenges.Solution().numIdenticalPairs([1, 2, 3])
        self.assertEqual(combos_1, 4)
        self.assertEqual(combos_2, 6)
        self.assertEqual(combos_3, 0)

    def test_numJewelsInStones(self):
        """Will the test_numJewelsInStones function return the proper solution?"""
        answer_1 = challenges.Solution().numJewelsInStones('aA', 'aAAbbbb')
        answer_2 = challenges.Solution().numJewelsInStones('z', 'ZZ')
        self.assertEqual(answer_1, 3)
        self.assertEqual(answer_2, 0)

    def test_smallerNumbersThanCurrent(self):
        """Will the smallerNumbersThanCurrent function return the proper solution?"""
        answer_1 = challenges.Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3])
        answer_2 = challenges.Solution().smallerNumbersThanCurrent([6, 5, 4, 8])
        answer_3 = challenges.Solution().smallerNumbersThanCurrent([7, 7, 7, 7])
        self.assertEqual(answer_1, [4, 0, 1, 1, 3])
        self.assertEqual(answer_2, [2, 1, 0, 3])
        self.assertEqual(answer_3, [0, 0, 0, 0])

    def test_sortSentence(self):
        """Will the sortSentence function return the proper solution?"""
        answer_1 = challenges.Solution().sortSentence("is2 sentence4 This1 a3")
        answer_2 = challenges.Solution().sortSentence("Myself2 Me1 I4 and3")
        answer_3 = challenges.Solution().sortSentence("over4 moon6 jumped3 the1 the5 cow2")
        self.assertEqual(answer_1, "This is a sentence")
        self.assertEqual(answer_2, "Me Myself and I")
        self.assertEqual(answer_3, "the cow jumped over the moon")

    def test_freqAlphabets(self):
        """Will the freqAlphabets function return the proper solution?"""
        answer_1 = challenges.Solution().freqAlphabets("10#11#12")
        answer_2 = challenges.Solution().freqAlphabets("1326#")
        answer_3 = challenges.Solution().freqAlphabets("25#")
        answer_4 = challenges.Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
        self.assertEqual(answer_1, "jkab")
        self.assertEqual(answer_2, "acz")
        self.assertEqual(answer_3, "y")
        self.assertEqual(answer_4, "abcdefghijklmnopqrstuvwxyz")

    def test_countConsistentStrings(self):
        """Will the countConsistentStrings function return the proper solution?"""
        ans_1 = challenges.Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"])
        ans_2 = challenges.Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
        ans_3 = challenges.Solution().countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
        self.assertEqual(ans_1, 2)
        self.assertEqual(ans_2, 7)
        self.assertEqual(ans_3, 4)


