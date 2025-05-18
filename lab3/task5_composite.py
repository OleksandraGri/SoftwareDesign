class LightNode:
    def __init__(self, tag=None):
        self.tag = tag
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        pass

class LightElementNode(LightNode):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag
        self._state = VisibleState()

    def render(self):
        print(f"<{self.tag}>")
        for child in self.children:
            child.render()
        if not self.is_self_closing:
            print(f"</{self.tag}>")

    def set_state(self, state):
        self._state = state

    def _render_impl(self):
        self._state.render(self)

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def render(self):
        print(self.text)

class ElementState:
    def render(self, node):
        pass

class VisibleState(ElementState):
    def render(self, node):
        print(f"<{node.tag}>")
        for child in node.children:
            child.render()
            print(f"</{node.tag}>")

class HiddenState(ElementState):
    def render(self, node):
        print(f"<!-- {node.tag} (hidden) -->")

