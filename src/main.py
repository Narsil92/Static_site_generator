from textnode import TextNode , TextType
# import TextNode and TextType class

#main func
def main():
    # Create a TextNode with some test values
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # When you print the node, Python automatically calls __repr__
    print(node)




#make sure it only run in main
if __name__ == "__main__":
    main()    