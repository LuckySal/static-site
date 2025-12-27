import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
     
    def test_diff_type(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_set_link(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a url node", TextType.URL, "https://google.com")
        self.assertEqual(node1.url, None)
        self.assertEqual(node2.url, "https://google.com")


if __name__ == "__main__":
    unittest.main()
