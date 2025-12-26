import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node3)
        node4 = TextNode("This is a text node", TextType.LINK, "/index.html")
        self.assertNotEqual(node, node4)
        node5 = TextNode("This isa text node", TextType.LINK, "/index.html")
        self.assertNotEqual(node5, node4)


if __name__ == "__main__":
    unittest.main()
