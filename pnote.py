import json
import cmd

KBASE_FILE = ""

class KnowledgeBase():
    def __init__(self):
        tagdict = {}
        
    def add_dot(self, kdot):
        if kdot.tag in self.tagdict:
            self.tagdict[tag].append({"priority": kdot.prio, "content": kdot.content}
        else:
            self.tagdict[tag] = [{"priority": kdot.prio, "content": kdot.content}]
            
    def del_dot_in_tag(self, idx):
        del self.tagdict[tag][idx]
            
    def save_base(self):
        with open(KBASE_FILE, "w") as outfile:
            json.dump(self.tagdict, outfile, indent=4)
    
    def load_base(self):
        with open(KBASE_FILE) as infile:
            self.tagdict = json.load(infile)
        
        
class KDot():
    def __init__(self, tag="general", content="", prio=5):
        self.tag = tag
        self.contentent = content
        self.prio = prio
        
        
class PyNotePrompt(cmd.Cmd):

    def do_new(self, tag):
        content = input("Enter text: ")
        if content == "":
            print("Please enter some text!")
        else:
            if tag == "":
                kdot = KDot(content=content)
            else:
                kdot = KDot(tag=tag, content=content)
            kbase.add_dot(kdot)
            
    def do_load(self):
        kbase.load_base()
        
    def do_commit(self):
        kbase.save_base()
        
    
class XplorePrompt(cmd.Cmd):
        
    def do_tag(self, tag):
        if tag == "":
            print("List of tags:")
            for key in kbase.tagdict.keys():
                print(key)
                
        else:
            for i, dot in enumerate(kbase.tagdict[tag]):
                print("%d: %s..." % (i, dot[:20]))
        
    def do_EOF(self, line):
        return True
if __name__ == '__main__':   
    #MyPrompt().cmdloop()
    
