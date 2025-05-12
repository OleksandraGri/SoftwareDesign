from task5_composite import LightElementNode, LightTextNode

class LightHTML:
    def __init__(self):
        self.nodes = []

    def add_line(self, line):
        if "Dramatis Personae" in line:
            self.nodes.append(LightElementNode("h2"))
        elif line.strip().startswith("ACT") or line.strip().startswith("Scene"):
            self.nodes.append(LightElementNode("h2"))
        elif len(line.strip()) < 20 and line.strip() != "":
            self.nodes.append(LightElementNode("h2"))
        elif line.startswith(" "):
            self.nodes.append(LightElementNode("blockquote"))
        else:
            self.nodes.append(LightElementNode("p"))

        self.nodes[-1].add_child(LightTextNode(line))

    def render(self):
        print("<html>")
        print("<body>")

        for node in self.nodes:
            node.render()

        print("</body>")
        print("</html>")
