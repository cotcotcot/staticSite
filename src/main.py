#!/usr/bin/env python3
from textnode import (TextNode, TextType, text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_image,
                      split_nodes_link,text_to_textnodes, markdown_to_blocks)
from htmlnode import HTMLNode, LeafNode,ParentNode

from block import (
    markdown_to_html_node,
    block_to_block_type,
    BlockType,
)

import os, shutil

from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def cpdir_proper(src, dest):
    todo = os.listdir(src)
    for relative in todo:
        absolute = os.path.join(src, relative)
        absolute_dest = os.path.join(dest, relative)
        if os.path.isdir(absolute):
            os.mkdir(absolute_dest)
            cpdir_proper(absolute, absolute_dest)
        else:
           shutil.copy(absolute, dest)
    
def cpdir(src, dest):
    if os.path.exists(src):
        shutil.rmtree(dest)
        os.mkdir(dest)
        cpdir_proper(src, dest)
    else:
        print(" répertoire src est manquant")

def main() :
    src = "/home/emmanuel/Nextcloud/Emmanuel/learning/python/staticSite/static/"
    dest = "/home/emmanuel/Nextcloud/Emmanuel/learning/python/staticSite/public"
    dir_path_content = "/home/emmanuel/Nextcloud/Emmanuel/learning/python/staticSite/content"
    template_path = "/home/emmanuel/Nextcloud/Emmanuel/learning/python/staticSite/template.html"
    cpdir(src, dest)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dest)


if __name__ == "__main__":
    main()
