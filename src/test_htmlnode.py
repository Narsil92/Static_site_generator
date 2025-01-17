import unittest


from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
      #Test raise NotImplemented exception
      def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
         node.to_html()      
      
      #Test when all values provided are empy since default value for each parameter is Noone
      def test_constructor_default(self):
          node=HTMLNode()
          self.assertIsNone(node.tag)
          self.assertIsNone(node.value)
          self.assertIsNone(node.children)
          self.assertIsNone(node.props)

      #Test where some contructor values are provided and some are empyy
      def test_constructor_with_some_args(self):
          node=HTMLNode(tag="a",value="some text")    
          self.assertEqual(node.tag , "a")
          self.assertEqual(node.value, "some text")
          self.assertIsNone(node.children)
          self.assertIsNone(node.props)   

      #Test with no other values provided aside from props without converting props dict to html
      def test_props_rest_noone(self):
          node=HTMLNode(props={"href": "https://www.google.com"})
          self.assertEqual(node.props, {"href": "https://www.google.com"})

      # Test with no prop and how props_to_html method is converting props dict into string
      def test_props_to_html(self):         
          node = HTMLNode(props=None)
          self.assertEqual(node.props_to_html(), "")
      # Test with one prop and how props_to_html method is converting props dict into string
      def test_one_prop_to_html(self):
          node = HTMLNode(props={"href": "https://www.google.com"})
          self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
      # Test with multiple props and how props_to_html method is converting props dict into string   
      def test_multiple_props_to_html(self):
          node = HTMLNode(props={
           "href": "https://www.google.com",
           "target": "_blank"}
           )
          self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
      
      #Test children list. Children parameter should be a list of HTMLNode objects.
      def test_constructor_with_children(self):
          child_node=HTMLNode("span", "some text")
          parent_node=HTMLNode(tag="div", children=[child_node])
          self.assertEqual(parent_node.tag, "div")
          self.assertIsNone(parent_node.value)
          self.assertEqual(len(parent_node.children), 1)
          self.assertIsNone(parent_node.props)
          self.assertEqual(parent_node.children[0].tag, "span")
          self.assertEqual(parent_node.children[0].value, "some text")
      


if __name__ == "__main__":
    unittest.main()          
     




    