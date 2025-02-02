import unittest

from markdown_extract import extract_markdown_images, extract_markdown_links

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_one_img(self): #pass
        text= "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text),[('rick roll', 'https://i.imgur.com/aKaOqIh.gif')])

    def test_extract_multiple_img(self): #pass
        text= "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    
    def test_no_images(self): #pass
        text = "This is plain text without any markdown images."
        self.assertEqual(extract_markdown_images(text), [])

    def test_malformed_image(self): #pass
        text = "![alt text](missing-a-closing-parenthesis"
        self.assertEqual(extract_markdown_images(text), [])    

    def test_malformed_image_2(self): #pass
        text = "[incorrect](https://not-an-image-no-exclamation-mark.jpg)"
        self.assertEqual(extract_markdown_images(text), [])

    def test_mixed_content_image(self): #pass
        text = "A link [to Boot.dev](https://boot.dev) and an image ![alt](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text), [('alt', 'https://example.com/image.jpg')])   

    def test_mixed_content_link(self):
        text = "A link [to Boot.dev](https://boot.dev) and an image ![alt](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_links(text), [('to Boot.dev', 'https://boot.dev')])     
          
    
if __name__ == "__main__":
    unittest.main()
