import unittest
import challenges


class NamesTestCase(unittest.TestCase):
    """Tests for 'numIdenticalPairs' function."""

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