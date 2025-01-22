from textnode import TextType, TextNode

#valid delimiter in list and 

valid_delimiters = ["**", "*", "`"]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    #check if text_type is valid for TextType class
    if text_type not in TextType:
       raise ValueError("Invalid text type provided!")
    #check to make sure delimiters passed here are valid

    if delimiter not in valid_delimiters:
        raise ValueError("Invalid delimiter provided! Allowed delimiters are: **, *, `.")
    
    new_nodes =[]

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
           if delimiter not in node.text:
               new_nodes.append(node)     
           else:  
               # Step 1: Find the first index of the delimiter 
               idx = node.text.find(delimiter)
               # Step 2: BEFORE the first delimite
               before_delimiter = node.text[:idx]
               if before_delimiter:
                   new_nodes.append(TextNode(before_delimiter, TextType.TEXT))

               # Step 3: BETWEEN the delimiters 
               # Find the next index of the closing delimiter
               end_idx = node.text.find(delimiter, idx + len(delimiter)) # Start looking after the first delimiter

               if end_idx == -1:  # If no closing delimiter is found
                  raise ValueError(f"No closing delimiter '{delimiter}' found for node '{node.text}'")  

               # Extract the text between the delimiters 
               between_delimiter = node.text[idx + len(delimiter):end_idx]  # Exclude the delimiters themselves

               if between_delimiter:  # Create a new TextNode for the marked text
                  new_nodes.append(TextNode(between_delimiter, text_type))

               # Step 4: Process the REMAINING text (after the closing delimiter)
               remaining_text = node.text[end_idx + len(delimiter):]
               if remaining_text:  # Call recursively or loop   
                       new_nodes.extend(split_nodes_delimiter([TextNode(remaining_text, TextType.TEXT)], delimiter, text_type))
        else:
            new_nodes.append(node)

    return new_nodes

def process_all_delimiters(old_nodes):

    # Step 1: Process for bold (**)
    new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    # Step 2: Process for italic (*)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

    # Step 3: Process for code (`)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    
    return new_nodes
             

            
    
    