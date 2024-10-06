import unittest
from typing import List

class Solution:
    """
    Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailhash: set[str] = set()
        for e in emails:
            local_name, domain_name = e.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            email = local_name + '@' + domain_name
            emailhash.add(email)
        return len(emailhash)

class TestNumUniqueEmails(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)

    def test_example_2(self):
        emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 3)

    def test_single_email(self):
        emails = ["test.email+alex@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_all_same_email(self):
        emails = ["a@leetcode.com", "a@leetcode.com", "a@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_max_length_email(self):
        local = "a" * 99
        domain = "b.com"
        emails = [f"{local}@{domain}"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_max_number_of_emails(self):
        emails = [f"a{i}@leetcode.com" for i in range(100)]
        self.assertEqual(self.solution.numUniqueEmails(emails), 100)

    def test_multiple_dots(self):
        emails = ["a.b.c@leetcode.com", "abc@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_multiple_plus_signs(self):
        emails = ["a+b+c@leetcode.com", "a@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_dots_and_plus_combined(self):
        emails = ["a.b+c@leetcode.com", "ab@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_different_domains(self):
        emails = ["test@a.com", "test@b.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)

    def test_local_name_edge_cases(self):
        emails = ["a@leetcode.com", ".a@leetcode.com", "a.@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_domain_name_with_dots(self):
        emails = ["test@leetcode.com", "test@lee.tcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)

if __name__ == '__main__':
    unittest.main()
