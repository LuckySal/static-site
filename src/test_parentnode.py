import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_empty(self):
        with self.assertRaises(TypeError):
            node = ParentNode()

    def test_parent_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag=None, children=[LeafNode(tag="p", value="Test")]
            )
            res = node.to_html()

    def test_parent_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag="div", children=[])
            res = node.to_html()

    def test_parent_with_children_to_html(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_nesting_to_html(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_deep_nesting_to_html(self):
        expected = '<p color="red"><div color="blue"><span color="black"><a href="test.com" target="_blank">Inner</a></span></div></p>'
        leaf1 = LeafNode(
            tag="a",
            value="Inner",
            props={"href": "test.com", "target": "_blank"},
        )
        parent1 = ParentNode(
            tag="span", children=[leaf1], props={"color": "black"}
        )
        parent2 = ParentNode(
            tag="div", children=[parent1], props={"color": "blue"}
        )
        parent3 = ParentNode(
            tag="p", children=[parent2], props={"color": "red"}
        )
        self.assertEqual(parent3.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
