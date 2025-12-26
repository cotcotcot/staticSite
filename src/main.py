#!/usr/bin/env python3
from textnode import TextType, TextNode

def main() :
    textnode = TextNode("test", TextType.TEXT, "/null")

    print(f"TextNode({textnode.text}, {textnode.text_type}, {textnode.url})")

if __name__ == "__main__":
    main()
