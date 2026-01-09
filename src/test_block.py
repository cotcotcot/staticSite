import unittest

from block import (
    markdown_to_html_node,
    block_to_block_type,
    BlockType,
)

from textnode import markdown_to_blocks
class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
    
        md = "```\ntneauitn```"
        print(f"{md} : {block_to_block_type(md)}")

        md = "#### Heading"
        print(f"{md} : {block_to_block_type(md)}")

        md = "> #### Heading\n> etinua3yyP"
        print(f"{md} : {block_to_block_type(md)}")

        md = "> #### Heading\n  etinua3yyP"
        print(f"{md} : {block_to_block_type(md)}")

        md = "- Heading\nl2\n- etina"
        print(f"{md} : {block_to_block_type(md)}")

        md = "- Heading\n- l2\n- etina"
        print(f"{md} : {block_to_block_type(md)}")

        md = "1. Heading\n2. from age\n3. to age\n4. the same"
        print(f"{md} : {block_to_block_type(md)}")

        md = "1. Heading\n 2. from age\n3. to age\n4. the same"
        print(f"{md} : {block_to_block_type(md)}")

        md = "1. Heading\n26. from age\n3. to age\n4. the same"
        print(f"{md} : {block_to_block_type(md)}")

        md = "dw#### Heading"
        print(f"{md} : {block_to_block_type(md)}")


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
