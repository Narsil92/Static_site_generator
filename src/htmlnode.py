class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag #string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value
        self.children = children
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag 

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")    
    
    # Method return a string that represents the HTML attributes of the node.
    def props_to_html(self):
        if self.props is None:
            return ""
        result=""
        for key,value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f'HTMLNode: tag:{self.tag},value:{self.value},children:{self.children},props_:{self.props}'
        
        


       
