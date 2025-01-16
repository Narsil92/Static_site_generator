import unittest


from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
      #Test raise NotImplemented
      def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
         node.to_html()
      
      
      # Test with no prop
      def test_props_to_html(self):         
          node = HTMLNode(props=None)
          self.assertEqual(node.props_to_html(), "")
      # Test with one prop
      def test_one_prop_to_html(self):
          node = HTMLNode(props={"href": "https://www.google.com"})
          self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
      # Test with multiple props    
      def test_multiple_props_to_html(self):
          node = HTMLNode(props={
           "href": "https://www.google.com",
           "target": "_blank"}
           )
          self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()          
     




    