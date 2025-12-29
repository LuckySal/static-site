import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node1 = HTMLNode()
        expected = (
            'HTMLNode tag: "None" value: "None" children: "[]" props: "{}"'
        )
        self.assertEqual(repr(node1), expected)

    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode(tag="a", value="link", props=test_props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), expected)

    def test_all_values(self):
        node1 = HTMLNode()
        test_tag = "a"
        test_value = "MTG"
        test_children = [node1]
        test_props = {"href": "https://scryfall.com", "target": "_blank"}
        test_node = HTMLNode(
            tag=test_tag,
            value=test_value,
            children=test_children,
            props=test_props,
        )
        expected = (
            "HTMLNode "
            f'tag: "{test_tag}" '
            f'value: "{test_value}" '
            f'children: "{test_children}" '
            f'props: "{test_props}"'
        )
        self.assertEqual(repr(test_node), expected)


if __name__ == "__main__":
    unittest.main()
