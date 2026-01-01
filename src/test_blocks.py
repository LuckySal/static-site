import unittest

from blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestBlocks(unittest.TestCase):
    # Test converting markdown text to blocks
    def test_markdown_to_blocks_empty(self):
        text = ""
        res = markdown_to_blocks(text)
        expected = []
        self.assertEqual(expected, res)

    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        res = markdown_to_blocks(text)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(expected, res)

    # Test determining type of markdown block
    def test_block_type_none(self):
        block = """
This block has no format.
It should be of type \"paragraph\""""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    # TODO: Finish unit tests
    def test_block_type_heading(self):
        heading_block = """# This is a "Heading" block"""
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading_block))

    def test_block_type_code(self):
        code_block = """```This is a "code" block```"""
        self.assertEqual(BlockType.CODE, block_to_block_type(code_block))

    def test_block_type_quote(self):
        quote_block = """>Quote line 1
>Quote line 2
>Quote line 3"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(quote_block))

    def test_block_type_ul(self):
        ul_block = """- Item
- Item
- Item"""
        self.assertEqual(
            BlockType.UNORDERED_LIST, block_to_block_type(ul_block)
        )

    def test_block_type_ol(self):
        ol_block = """1. Item 1
2. Item 2
3. Item 3
4. Item 4"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(ol_block))


if __name__ == "__main__":
    unittest.main()
