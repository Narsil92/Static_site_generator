from textnode import TextType,TextNode
from markdown_extract import extract_markdown_images


def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_images(node.text)

        if not matches:
            new_nodes.append(node)
            continue

        # Keep track of where we are in the text
        current_idx = 0

        for alt_text, url in matches:
            image_markdown = f"![{alt_text}]({url})"
            idx = node.text.find(image_markdown, current_idx)

            if idx > current_idx:
                before_img_markdown = node.text[current_idx:idx]
                new_nodes.append(TextNode(before_img_markdown, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            # Update current_idx to after this image
            current_idx = idx + len(image_markdown)

        # Add any remaining text after the last image
        if current_idx < len(node.text):
            remaining_text = node.text[current_idx:]
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
           