import json
import cmd

KBASE_FILE = "pkm.json"

class KnowledgeBase():
    def __init__(self):
        self.tagdict = {}
        
    def add_dot(self, kdot):
        if kdot.tag in self.tagdict:
            self.tagdict[kdot.tag].append({"priority": kdot.prio, "content": kdot.content})
        else:
            self.tagdict[kdot.tag] = [{"priority": kdot.prio, "content": kdot.content}]
            
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
        self.content = content
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
            
    def do_load(self, arg):
        kbase.load_base()
        
    def do_commit(self, arg):
        kbase.save_base()
        
    def do_xplore(self, arg):
        XplorePrompt().cmdloop()
        
    def do_EOF(self, arg):
        return True
        
    
class XplorePrompt(cmd.Cmd):
        
    def do_tag(self, tag):
        if tag == "":
            print("List of tags:")
            tag_list = kbase.tagdict.keys()
            for i, tag  in enumerate(tag_list):
                print("%d: %s" % (i, tag))
            
            while True:
                print("Show which tag? Enter tag or c to cancel")
                answer = input()
                if answer == "c":
                    break
                elif answer in kbase.tagdict.keys():
                    for i, kdot in enumerate(kbase.tagdict[answer]):
                        print("%d: %s..." % (i, kdot["content"][:60]))
                else:
                    print("Invalid input!")
                
                    
        
    def do_EOF(self, line):
        return True
if __name__ == '__main__':   
    kbase = KnowledgeBase()
    PyNotePrompt().cmdloop()
    
