import unittest

from htmlnode import HTMLNode, LEAFNode

class TestLEAFNode(unittest.TestCase):
    def test_to_html_tag_values(self):
        leaf = LEAFNode("p", "bla bla bla")
        self.assertEqual(leaf.to_html(), "<p>bla bla bla</p>")

    def test_to_html_no_tag_just_text(self):
        leaf = LEAFNode(None, "Martynka")
        self.assertEqual(leaf.to_html(), "Martynka")    
    
    def test_to_html_missing_values(self):
        with self.assertRaises(ValueError) as context:
            LEAFNode("p",None)
        self.assertEqual(str(context.exception), "No value provided !")

        # LeafNode with tag, value, and attributes 
    def test_tag_attribute_value(self):
        props= {"href": "https://www.google.com"}
        leaf = LEAFNode("a","Click me!", props)
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    




if __name__ == "__main__":
    unittest.main()     