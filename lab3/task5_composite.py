class LightNode:
    def __init__(self, tag=None):
        self.tag = tag
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
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

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def render(self):
        print(self.text)
