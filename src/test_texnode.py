import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text1", TextType.BOLD)
        self.assertEqual(node, node2)     

    def test_not_eq_different_text(self):
         # Test when only text is different
        node1 = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
         # Test when only text_type is different
        node1 = TextNode("same text", TextType.BOLD)
        node2 = TextNode("same text", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
         # Test when only url is different
        node1 = TextNode("same text", TextType.BOLD, "url1")
        node2 = TextNode("same text", TextType.BOLD, "url2")
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_missing(self):
        node = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text1", TextType.BOLD, "url1")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()