import cmd
import pynote

class PyNotePrompt(cmd.Cmd):

    def do_new(self, tag):
        content = input("Enter text: ")
        if content == "":
            print("Please enter some text!")
        else:
            if tag == "":
                kdot = pynote.KDot(content=content)
            else:
                kdot = pynote.KDot(tag=tag, content=content)
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
    kbase = pynote.KnowledgeBase()
    PyNotePrompt().cmdloop()