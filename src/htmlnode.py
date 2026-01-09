class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props  = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ""
        if self.props != None:
            for prop in self.props:
                attributes += f' {prop}="{self.props[prop]}"'

        return attributes

    def __repr__(self):
        print(f"(htmlNode: {self.tag}, {self.value}, {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node as no Value")
        else:
            if self.tag == None: return f"{self.value}"
            if self.props: return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props = None)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent Node as no tag")
        if self.children == None or self.tag == "":
            raise ValueError("Parent Node as no children")
        
        child_html = ""
        for child in self.children:
            child_html +=  f"{child.to_html()}"

        if self.props: return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
        return f"<{self.tag}>{child_html}</{self.tag}>"
