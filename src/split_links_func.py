from textnode import TextType,TextNode
from markdown_extract import extract_markdown_links


# [Link text Here](https://link-url-here.org)

def split_nodes_links(old_nodes):
    
    
    new_nodes=[]

    for node in old_nodes:
        # Check if no images are found in the text
        matches = extract_markdown_links(node.text)  # Pass `node.text` to extract the images

        if not matches: # If the list is empty, no images are found
            new_nodes.append(node)  # Add the original node as-is
            continue   # Skip to the next iteration of the loop

        for link_text,url in matches:
                link_markdown = f"[{link_text}]({url})"
                idx = node.text.find(link_markdown) # Find where the match begins
                before_link_markdown = node.text[:idx] # Text before the match

                if before_link_markdown:
                     new_nodes.append(TextNode(before_link_markdown, TextType.TEXT)) 

                new_nodes.append(TextNode(link_text, TextType.LINK, url))      

                after_idx = idx + len(link_markdown)  # Calculate where the image markdown ends    
                after_link_markdown = node.text[after_idx:]  # Remaining text after image markdown  
                if after_link_markdown:
                # Recursively process remaining text to handle more images
                    remaining_nodes = split_nodes_links([TextNode(after_link_markdown, TextType.TEXT)])
                    new_nodes.extend(remaining_nodes)

    return new_nodes

