import unittest

from htmlnode import HTMLNode, LEAFNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_complex_nested_structure(self):
        node =ParentNode("div",[ParentNode("p", [LEAFNode("b", "Bold text"),LEAFNode(None, "Normal text")]),LEAFNode("br", None)])
        expected_html='<div><p><b>Bold text</b>Normal text</p><br></div>'
        self.assertEqual(node.to_html(),expected_html)
    
    def test_empty_children(self):
        node = ParentNode("div", [])
        expected_html = "<div></div>"
        self.assertEqual(node.to_html(), expected_html)




if __name__ == "__main__":
    unittest.main()     
