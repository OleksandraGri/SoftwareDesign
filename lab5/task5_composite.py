# Базовий вузол
class LightNode:
    def __init__(self, tag=None):
        self.tag = tag
        self.children = []
        self.style = ""
        self.visible = True
        self.on_created()

    def on_created(self):
        """Хук для виконання коду під час створення елемента."""
        if self.tag:
            print(f"{self.tag} Created")

    def on_inserted(self):
        """Хук для виконання коду після вставки елемента в DOM."""
        if self.tag:
            print(f"{self.tag} Inserted")

    def on_removed(self):
        """Хук для виконання коду після видалення елемента."""
        if self.tag:
            print(f"{self.tag} Removed")

    def add_child(self, child):
        self.children.append(child)
        child.on_inserted()

    def render(self):
        """Метод для виведення елемента в HTML."""
        if not self.visible:
            return
        for child in self.children:
            child.render()

    def apply_styles(self):
        """Метод для застосування стилів до елемента."""
        print(f"Styles applied: {self.style}")

# HTML елемент
class LightElementNode(LightNode):
    def __init__(self, tag, is_block=True, is_self_closing=False):
        super().__init__(tag)
        self.is_block = is_block
        self.is_self_closing = is_self_closing

    def render(self):
        if not self.visible:
            return
        print(f"<{self.tag}>")
        super().render()
        if not self.is_self_closing:
            print(f"</{self.tag}>")

# Текстовий вузол
class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__(tag="text")
        self.text = text

    def render(self):
        if self.visible:
            print(self.text)

# HTML документ
class LightHTML:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def render(self):
        print("<html>")
        print("<body>")
        for line in self.lines:
            print(f"<p>{line}</p>")
        print("</body>")
        print("</html>")

# Абстрактний логер
class Logger:
    def Log(self, message):
        raise NotImplementedError

    def Error(self, message):
        raise NotImplementedError

    def Warn(self, message):
        raise NotImplementedError

# Адаптер логера до файлу
class FileLoggerAdapter(Logger):
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def Log(self, message):
        self.file_writer.Write(message)

    def Error(self, message):
        self.file_writer.WriteLine(f"Error: {message}")

    def Warn(self, message):
        self.file_writer.WriteLine(f"Warn: {message}")

# Специфічні HTML елементи
class Div(LightElementNode):
    def __init__(self):
        super().__init__('div')

class P(LightElementNode):
    def __init__(self):
        super().__init__('p')

class Span(LightElementNode):
    def __init__(self):
        super().__init__('span')

# Ітератор по DOM дереву
class HTMLIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        current = self.stack.pop()
        self.stack.extend(current.children)
        return current

# Командний шаблон
class Command:
    def execute(self):
        pass

class ChangeStyleCommand(Command):
    def __init__(self, element, style):
        self.element = element
        self.style = style

    def execute(self):
        self.element.style = self.style
        print(f"Style of {self.element.tag} changed to {self.style}")

# Шаблон стану
class ElementState:
    def render(self, element):
        pass

class VisibleState(ElementState):
    def render(self, element):
        element.visible = True
        print(f"{element.tag} is now visible.")

class HiddenState(ElementState):
    def render(self, element):
        element.visible = False
        print(f"{element.tag} is now hidden.")

# Відвідувач
class ElementVisitor:
    def visit(self, element):
        pass

class StyleVisitor(ElementVisitor):
    def visit(self, element):
        print(f"Applying styles to {element.tag}")
        element.apply_styles()
