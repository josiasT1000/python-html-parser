import htmElement

class HtmlTree():
    def __init__(self, file):
        self.tree = []

def filter(s, l, j=""):
    for f in l:
        my_list = s.split(f)
        s = j.join(my_list)
    return s

def make_tree(my_str):
    return True


with open("file2.html", "r") as f:
   s = f.read()
   my_str = filter(s, ["\n","\t"])
   print(my_str)
   parts = []
   open_sym = "<"
   close_sym = ">"
   while my_str.count("<") > 0 and my_str.count(">") > 0:
       text = my_str[my_str.index(open_sym) + 1: my_str.index(close_sym)]
       my_str = my_str[my_str.index(close_sym): len(my_str)]
       if close_sym == ">":
           parts.append({"tag": text})
           open_sym = ">"
           close_sym = "<"
       else:
           parts.append({"text": text})
           open_sym = "<"
           close_sym = ">"

   print(parts)



