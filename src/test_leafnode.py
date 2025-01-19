import unittest

from htmlnode import HTMLNode, LEAFNode

class TestLEAFNode(unittest.TestCase):
    def test_to_html_tag_values(self):
        leaf = LEAFNode("p", "bla bla bla")
        self.assertEqual(leaf.to_html(), "<p>bla bla bla</p>")

    def test_to_html_no_tag_just_text(self):
        leaf = LEAFNode(None, "Martynka")
        self.assertEqual(leaf.to_html(), "Martynka")    
    
    def test_invalid_leaf_node(self):
        with self.assertRaises(ValueError) as context:
            LEAFNode(None, None)
        self.assertEqual(str(context.exception), "Must have either a tag or a value!")

        # LeafNode with tag, value, and attributes 
    def test_tag_attribute_value(self):
        props= {"href": "https://www.google.com"}
        leaf = LEAFNode("a","Click me!", props)
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leaf.to_html(), expected_html)

        #LeafNode test with empty props
    def test_to_html_props_empty(self):
        props ={}
        leaf=LEAFNode("p","some text", props)
        expected_html=("<p>some text</p>")
        self.assertEqual(leaf.to_html(),expected_html)

        #LeafNode test with props having special character
    def test_to_html_props_special_character(self):
        props={"data-info": 'Use <important> info & details'}
        leaf = LEAFNode("div", "Test content", props)
        expected_html = '<div data-info="Use <important> info & details">Test content</div>'
        self.assertEqual(leaf.to_html(), expected_html)

        #LeafNode Value Error test where value is empty 
    def test_to_html_empty_values(self):
        with self.assertRaises(ValueError):
            LEAFNode(None,"")    



if __name__ == "__main__":
    unittest.main()     