import unittest
from textnode import TextNode,TextType
from split_links_func import split_nodes_links

class TestSplitLinksFunc(unittest.TestCase):
    def test_split_nodes_links_basic(self):
        node = TextNode("This is text with a [link](https://boot.dev)", TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 2
        assert result[0].text == "This is text with a "  # Note the space at the end
        assert result[1].text == "link"
        assert result[1].url == "https://boot.dev"  # The actual URL from input
        
    def test_multiple_links(self):
        node = TextNode("This has [link1](https://boot.dev) and [link2](https://youtube.com)",TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 4  # Should have 4 nodes: text, link1, text, link2
        assert result[0].text == "This has "
        assert result[1].text == "link1"
        assert result[1].url == "https://boot.dev"
        assert result[2].text == " and "
        assert result[3].text == "link2"
        assert result[3].url == "https://youtube.com"    

    def test_no_links(self):
        node = TextNode("This is plain text with no links", TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 1
        assert result[0].text == "This is plain text with no links"
        assert result[0].text_type == TextType.TEXT    

    def test_just_a_link(self):
        node = TextNode("[only link](https://boot.dev)", TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 1
        assert result[0].text == "only link"
        assert result[0].text_type == TextType.LINK
        assert result[0].url == "https://boot.dev"    

    def test_text_between_links(self):
        node = TextNode("[link1](https://boot.dev) middle text [link2](https://youtube.com)",TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 3
        assert result[0].text == "link1"
        assert result[0].url == "https://boot.dev"
        assert result[1].text == " middle text "
        assert result[2].text == "link2"
        assert result[2].url == "https://youtube.com" 

    def test_empty_link_text(self):
        node = TextNode("[](https://boot.dev)", TextType.TEXT)
        result = split_nodes_links([node])
        assert len(result) == 1
        assert result[0].text == ""
        assert result[0].text_type == TextType.LINK
        assert result[0].url == "https://boot.dev"       