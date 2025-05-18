class LightNode:
    def __init__(self, tag=None):
        self.tag = tag
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        pass

    def accept(self, visitor):
        pass

class LightElementNode(LightNode):
    def __init__(self, tag, is_block=True, is_self_closing=False):
        super().__init__(tag)
        self.is_block = is_block
        self.is_self_closing = is_self_closing

    def render(self):
        print(f"<{self.tag}>")
        for child in self.children:
            child.render()
        if not self.is_self_closing:
            print(f"</{self.tag}>")

    def accept(self, visitor):
        visitor.visit_element(self)
        for child in self.children:
            child.accept(visitor)

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def render(self):
        print(self.text)

    def accept(self, visitor):
        visitor.visit_text(self)
        
class NodeVisitor:
    def visit_element(self, element):
        pass

    def visit_text(self, text):
        pass

class StatsVisitor(NodeVisitor):
    def __init__(self):
        self.element_count = 0
        self.text_count = 0
        self.total_chars = 0

    def visit_element(self, element):
        self.element_count += 1

    def visit_text(self, text):
        self.text_count += 1
        self.total_chars += len(text.text)

