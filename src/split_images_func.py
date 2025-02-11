from textnode import TextType,TextNode
from markdown_extract import extract_markdown_images


def split_nodes_images(old_nodes, text_type):
    if text_type not in TextType:
        raise ValueError("Invalid text type provided!")
    
    new_nodes = []

    for node in old_nodes:
        # Check if no images are found in the text
        matches = extract_markdown_images(node.text)  # Pass `node.text` to extract the images

        if not matches:  # If the list is empty, no images are found
            new_nodes.append(node)  # Add the original node as-is
            continue   # Skip to the next iteration of the loop

        for alt_text, url in matches:
            image_markdown = f"![{alt_text}]({url})"
            idx = node.text.find(image_markdown)  # Find where the match begins
            before_img_markdown = node.text[:idx]  # Text before the match
            if before_img_markdown:
                new_nodes.append(TextNode(before_img_markdown, TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))           

            after_idx = idx + len(image_markdown)  # Calculate where the image markdown ends
            after_img_markdown = node.text[after_idx:]  # Remaining text after image markdown

            # Check for remaining text after the current match
            if after_img_markdown:
                # Recursively process remaining text to handle more images
                remaining_nodes = split_nodes_images([TextNode(after_img_markdown, TextType.TEXT)], TextType.IMAGE)
                new_nodes.extend(remaining_nodes)

    return new_nodes
           