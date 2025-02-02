from textnode import TextNode , TextType
from htmlnode import HTMLNode, LEAFNode, ParentNode
from markdown_extract import extract_markdown_images,extract_markdown_links
# import TextNode and TextType class

#main func
def main():
    # Create a TextNode with some test values
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # When you print the node, Python automatically calls __repr__
    print(node)

def text_node_to_html(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Text type unknown")
    if text_node.text_type == TextType.TEXT:
       return LEAFNode(tag =None, value=text_node.text)
    
    tag_map = {
    TextType.BOLD: "b",
    TextType.ITALIC: "i",
    TextType.CODE: "code",}

    if text_node.text_type in tag_map:
        return LEAFNode(tag=tag_map[text_node.text_type], value=text_node.text)
    
    if text_node.text_type == TextType.LINK:
         if not text_node.url:  # Check if the URL is absent or None
           raise Exception("Missing 'url' for TextType.LINK")
         return LEAFNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    if text_node.text_type== TextType.IMAGE:
        if not text_node.url:  # Check if the URL is absent or None
           raise Exception("Missing 'url' for TextType.IMG")
        return LEAFNode(tag="img",value="",props={"src": text_node.url,
                                                  "alt": text_node.text})




#make sure it only run in main
if __name__ == "__main__":
    main()    