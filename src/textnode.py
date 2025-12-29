from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    """An enum of supported text types"""

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    URL = "url"
    IMAGE = "image"


class TextNode:
    """A class containing basic ingormation abaout a section of text"""

    def __init__(self, text, text_type, url=None):
        """TextNode constructor

        Args:
            text (string, required): Contents of the text.
            text_type (TextType, required): The type of the text. Used to convert to HTML. See TextType enum for accepted types.
            url (string, optional): URL destination for link and image text types. Defaults to None.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    """Converts a text node to the corresponding LeafNode

    Args:
        text_node (TextNode, required): A text node to convert

    Raises:
        TypeError: Raised if text type is missing or incorrect

    Returns:
        LeafNode: Leaf node containing HTML properties
    """
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url, "alt": text_node.text},
            )
        case _:
            raise TypeError("Node is not a recognized type.")
