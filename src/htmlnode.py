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
    
class LEAFNode(HTMLNode):
      def __init__(self,tag,value,props=None):
        if tag is None and value is None:
            raise ValueError("Must have either a tag or a value!")
        super().__init__(tag,value,children=[],props=props)
         
      def to_html(self):
        if self.tag is None:
            return self.value
        
        props_html = self.props_to_html()
            
        if self.value is None:
            return f'<{self.tag}{props_html}>'
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
      
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
       super().__init__(tag=tag,value=None, children=children,props=props) 

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided !")
        if self.children is None:
            raise ValueError("children value not provided")
        
        result = f"<{self.tag}>"

        for c in self.children:
            result += c.to_html()
        result += f"</{self.tag}>"
        return result    
            
        

         

            
        


       
