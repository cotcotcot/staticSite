import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html = HTMLNode("p")
        html.__repr__()
        html2 = HTMLNode("p", "mon paragraphe", None, { "src": "/index.html", "target": "_blank"})
        print(html2.props_to_html())


if __name__ == "__main__":
    unittest.main()
