from textnode import TextType,TextNode
from markdown_extract import extract_markdown_links




def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Check if no images are found in the text
        matches = extract_markdown_links(node.text)  # Pass `node.text` to extract the images

        if not matches: # If the list is empty, no images are found
            new_nodes.append(node)  # Add the original node as-is
            continue   # Skip to the next iteration of the loop

        # Keep track of where we are in the text
        current_idx = 0

        for link_text, url in matches:
            link_markdown = f"[{link_text}]({url})"
            idx = node.text.find(link_markdown, current_idx) # Added current_idx parameter here

            if idx > current_idx:    
                before_link_markdown = node.text[current_idx:idx] # Changed to use current_idx
                new_nodes.append(TextNode(before_link_markdown, TextType.TEXT)) 
                 
            new_nodes.append(TextNode(link_text, TextType.LINK, url)) 
            
            # Update current_idx to after this link
            current_idx = idx + len(link_markdown)     
        
        # This part stays outside the for loop because it handles text after all links
        if current_idx < len(node.text):
            remaining_text = node.text[current_idx:]
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))   

    return new_nodes
