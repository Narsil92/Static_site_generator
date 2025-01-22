import unittest

from textnode import TextNode, TextType
from split_delimiter_func import split_nodes_delimiter, process_all_delimiters

class TestSplitDelimiterFunc(unittest.TestCase):
    def test_basic_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_no_delimiter(self):
        node = TextNode("This is just plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is just plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_basic_code_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
    
    def test_missing_closing_delimiter(self):
        node = TextNode("This is **bold text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_multiple_bold_delimiters(self):
        node = TextNode("This is **bold** and more **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)       
        self.assertEqual(len(nodes), 5)  # Should have 5 nodes
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " and more ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "bold")
        self.assertEqual(nodes[3].text_type, TextType.BOLD)
        self.assertEqual(nodes[4].text, " text")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

    def test_multiple_italic_delimiters(self):
        node = TextNode("This is *italic* and more *italic* text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)       
        self.assertEqual(len(nodes), 5)  # Should have 5 nodes
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " and more ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " text")
        self.assertEqual(nodes[4].text_type, TextType.TEXT) 

    def test_non_text_node(self):
        node = TextNode("**bold text**", TextType.BOLD)  # Note this is already BOLD type
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(len(nodes), 1)  # Should remain as one node
        self.assertEqual(nodes[0].text, "**bold text**")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)       

    def test_process_all_delimiters(self):
        node = TextNode("This is **bold** and *italic* and `code` text", TextType.TEXT)
        nodes = process_all_delimiters([node])
    
        self.assertEqual(len(nodes), 7)  # Should have 7 nodes
        
        # Check each node's text and type
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        
        self.assertEqual(nodes[4].text, " and ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        
        self.assertEqual(nodes[5].text, "code")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        
        self.assertEqual(nodes[6].text, " text")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)

        
        