import unittest
from textnode import TextNode,TextType
from split_images_func import split_nodes_images

class TestSplitImagesFunc(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("Text before ![alt](image_url) text after", TextType.TEXT)
        result = split_nodes_images([node], TextType.IMAGE)
        assert len(result) == 3
        assert result[0].text == "Text before "
        assert result[1].text == "alt"
        assert result[1].url == "image_url"
        assert result[2].text == " text after"

    def test_multiple_images(self):
        node = TextNode("Before ![alt1](img1) middle text ![alt2](img2) after text", TextType.TEXT)
        result = split_nodes_images([node], TextType.IMAGE)
        assert len(result) == 5
        assert result[0].text == "Before "
        assert result[1].text == "alt1"
        assert result[1].url == "img1"
        assert result[2].text == " middle text "
        assert result[3].text == "alt2"
        assert result[3].url == "img2"
        assert result[4].text == " after text"    

    def test_no_images(self):
        node = TextNode("This is plain text with no images", TextType.TEXT)
        result = split_nodes_images([node], TextType.IMAGE)
        assert len(result) == 1  # Only one node since no images were found
        assert result[0].text == "This is plain text with no images"
        assert result[0].text_type == TextType.TEXT    