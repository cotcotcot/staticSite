import unittest

from textnode import (TextNode, TextType, text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_image,
                      split_nodes_link,text_to_textnodes, markdown_to_blocks)
from htmlnode import HTMLNode, LeafNode,ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html = HTMLNode("p")
        html.__repr__()
        html2 = HTMLNode("p", "mon paragraphe", None, { "src": "/index.html", "target": "_blank"})
        print(html2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("a", "click me", {"href":"/index.html","bidon":"fort"})
        print(node2.to_html())
        self.assertEqual(node2.to_html(), '<a href="/index.html" bidon="fort">click me</a>')

        node3 = LeafNode("img", "Hello, world!", {"href":"/index.html"})
        print(node3.to_html())
        self.assertEqual(node3.to_html(), '<img href="/index.html">Hello, world!</img>')
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
      node = TextNode("This is a text node", TextType.TEXT)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")


    def test_extract_markdown_links(self):
      text = "etisuan [mon texte](mon url) ![mon texte](mon image)  èoptnd [mon texte](mon url2) "
      text2 = "etisuan [mon texte](mon url) ![mon texte](mon image)  èoptnd [mon texte](mon url2) ![mon texte](mon image2) "
      print(extract_markdown_links(text))
      print(extract_markdown_links(text2))
      print(extract_markdown_images(text))
      print(extract_markdown_images(text2))

    def test_text_to_nodes(self):
      text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
      print(text_to_textnodes(text))

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":

    unittest.main()
