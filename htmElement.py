
class HtmlElement():

    def __init__(self, tag="", text="", self_tag=True):
        self.tag = tag
        self.attr = {}
        self.child = []
        self.text = text
        self.self_tag = self_tag
        self.tabs = 0

    def __str__(self):
        value = self.tabs*"\t" + "<" + self.tag + " "
        for a, v in self.attr.items():
            value += a + "=\""
            for vi in v:
                value += vi + " "
            value += "\" "
        value += ">"
        for child in self.child:
            child.tabs = self.tabs + 1
            value += "\n" + child.__str__()
        if not self.self_tag:
            value += "\n" + self.tabs*"\t" + "</" + self.tag + ">"
        return value


    def add_child(self, child):
        self.child.append(child)

    def add_attr(self, attr, val, overwrite=True):
        if overwrite:
            self.attr[attr] = [val]
        else:
            self.attr[attr].append(val)



h1 = HtmlElement("H1", "Hello world", False)
h1.add_attr("id", "title")
h1.add_attr("id", "title-two", False)

btn = HtmlElement("button", "click", False)
btn.add_attr("class","btn btn-primary")

elt = HtmlElement("div", "", False)
elt.add_attr("class", "container")
elt.add_child(h1)
elt.add_child(btn)
#print(elt)