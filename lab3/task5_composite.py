class LightNode:
    def __init__(self):
        self.children = []

    def on_created(self):
        pass

    def on_inserted(self):
        pass

    def on_removed(seld):
        pass

    def on_styles_applied(self):
        pass

    def on_text_rendered(self):
        pass
        
    def add_child(self, child):
        self.children.append(child)
        child.on_inserted()

    def render(self):
        self.on_created()
        self._render_impl()
        self.on_text_rendered()

    def _render_impl(self):
        raise NotImplementedError()

class LightElementNode(LightNode):
    def __init__(self, tag, is_block=True):
        super().__init__(tag)
        self.is_block = is_block
        self.tag = tag
        self.styles = {}
        self.classes = []

    def add_style(self, name, value):
        self.styles[name] = value
        self.on_styles_applied()

    def add_class(self, class_name):
        self.classes.append(class_name)
        self.on_class_list_applied()

    def on_class_list_applied(self):
        print(f"Class applied to {self.tag}")
        
    def _render_impl(self):
        print(f"<{self.tag}>")
        for child in self.children:
            child.render()
        print(f"</{self.tag}>")

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def render(self):
        print(self.text)
