from enum import Enum

class TextType(Enum):
    TEXT = "text"          # For normal text
    BOLD = "bold"          # For **bold** text
    ITALIC = "italic"      # For *italic* text
    CODE = "code"          # For `code` text
    LINK = "link"          # For [links](url)
    IMAGE = "image"        # For ![images](url)

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
               
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
    
        