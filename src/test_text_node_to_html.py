import unittest

from textnode import TextNode , TextType
from htmlnode import HTMLNode, LEAFNode, ParentNode
from main import text_node_to_html

#testing text_node_to_html() function

class TestTextNodeToHtml(unittest.TestCase):
    def test_invalid_text_type(self):
        text_node=TextNode("Hello!", "Text type unknown")
        with self.assertRaises(Exception):
            text_node_to_html(text_node)
    
    def test_basic_conversion(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html(text_node)    
        self.assertIsInstance(html_node,LEAFNode)
        #Should not have tag since it's TextType
        self.assertIsNone(html_node.tag)
        #Should return pure string
        self.assertEqual(html_node.value, "Hello, world!")

    def test_bold_conversion(self):
        text_node = TextNode("Hello, World!", TextType.BOLD)
        html_node = text_node_to_html(text_node)
        self.assertIsInstance(html_node,LEAFNode)
        #Check if it's adding Bold Tag
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "Hello, World!")

    def test_italic_conversion(self):
        text_node = TextNode("Hello, World!", TextType.ITALIC)
        html_node = text_node_to_html(text_node)
        self.assertIsInstance(html_node,LEAFNode)
        #Check if it's adding Bold Tag
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "Hello, World!") 

    def test_code_conversion(self):
        text_node = TextNode("Hello, World!", TextType.CODE)
        html_node = text_node_to_html(text_node)
        self.assertIsInstance(html_node,LEAFNode)
        #Check if it's adding Bold Tag
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value, "Hello, World!")   

    def test_link_conversion(self):   
        text_node = TextNode("CLICK ME!", TextType.LINK, url="https://www.example.com")
        html_node = text_node_to_html(text_node)
        self.assertIsInstance(html_node,LEAFNode)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"CLICK ME!")
        self.assertEqual(html_node.props,{"href": text_node.url})
    
    def test_img_conversion(self):   
        text_node = TextNode("Cute Seal", TextType.IMAGE, url="https://www.example.com")
        html_node = text_node_to_html(text_node)
        self.assertIsInstance(html_node,LEAFNode)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value,"")
        self.assertEqual(html_node.props,{"src": text_node.url,
                                          "alt": text_node.text})

if __name__ == "__main__":
    unittest.main()