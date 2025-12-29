import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_text_empty(self):
        with self.assertRaises(TypeError):
            node = TextNode()

    def test_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_diff_type(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_text_set_link(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode(
            "This is a url node", TextType.URL, "https://google.com"
        )
        self.assertEqual(node1.url, None)
        self.assertEqual(node2.url, "https://google.com")

    def test_text_no_type(self):
        with self.assertRaises(TypeError):
            node = TextNode("Text node with no type", None)
            html_node = text_node_to_html_node(node)

    def test_text_wrong_type(self):
        with self.assertRaises(AttributeError):
            node = TextNode("Text node with invalid type", TextType.BOOK)

    def test_text_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image_to_html(self):
        node = TextNode("Image alt text", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)
        expected = '<img src="image.png" alt="Image alt text"></img>'
        self.assertEqual(html_node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
