import json
import cmd
import re

KBASE_FILE = "pkm.json"

class KnowledgeBase():
    def __init__(self):
        self.tagdict = {}
        
    def add_dot(self, kdot):
        if kdot.tag in self.tagdict:
            self.tagdict[kdot.tag].append({"priority": kdot.prio, "content": kdot.content})
        else:
            self.tagdict[kdot.tag] = [{"priority": kdot.prio, "content": kdot.content}]
            
    def del_dot_in_tag(self, tag, idx):
        del self.tagdict[tag][idx]
            
    def save_base(self):
        with open(KBASE_FILE, "w") as outfile:
            json.dump(self.tagdict, outfile, indent=4)
    
    def load_base(self):
        with open(KBASE_FILE) as infile:
            self.tagdict = json.load(infile)

    def search_base(self, search_term):
        search_results = []
        for tag in self.tagdict.keys():
            for dot in self.tagdict[tag]:
                match = re.search((search_term), dot["content"])
                if match:
                    search_results.append(dot)
        return search_results
        
        
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
        
        
    def do_EOF(self, arg):
        return True
        
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
                        print("%d: %s \n" % (i, kdot["content"]))
                else:
                    print("Invalid input!")
            
    def do_search(self, search_term):
        results = kbase.search_base(search_term)
        if len(results) == 0:
            print("No matches found")
        else:
            for i, kdot in enumerate(results):
                print("%d: %s \n" % (i, kdot))
                
                    
        
    
if __name__ == '__main__':   
    kbase = KnowledgeBase()
    PyNotePrompt().cmdloop()
    
