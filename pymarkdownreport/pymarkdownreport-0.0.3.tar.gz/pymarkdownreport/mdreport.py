

class MDReport():
    """This class implements a mardown report generator
    """
    def __init__(self, title:str):
        self.report = ""
        self.H1(title)

    def H1(self, text:str): 
        self.report += f"# {text}\n"

    def H2(self, text:str): 
        self.report += f"## {text}\n"

    def H3(self, text:str): 
        self.report += f"### {text}\n"

    def text(self, text:str): 
        self.report += f"{text}\n"

    def bold(self, text:str):
        self.report += f"**{text}**\n"
    
    def italic(self, text:str): 
        self.report += f"*{text}*\n"

    def bullet_points(self, *args): 
        for arg in args:
            self.report += f"* {arg}\n"

    def numbered_list(self, *args): 
        for idx,arg in enumerate(args):
            self.report += f"{idx+1}. {arg}\n"

    def link(self, text: str, source: str):
        self.report += f"[{text}]({source})\n"

    def image(self, source:str, title: str = "", alt_text: str = "alt text"):   
        self.report += f"![{alt_text}]({source} '{title}')\n"
    
    def code_block(self, language:str, text:str):
        self.report += f"'''{language}\n {text} \n'''\n"

    def blockquote(self, text:str):
        self.report += f"> {text}\n"

    def horizontal_rule(self): 
        self.report += f"---\n"

    def save(self, filepath:str):
        with open(filepath,'w') as f:
            f.write(self.report)




def test_mdreport():
    report = MDReport("Test Report") 
    report.H1("This is a test report for H1")
    report.H2("This is a test report for H2")
    report.H3("This is a test report for H3")
    report.horizontal_rule()
    report.text("This is a text input")
    report.horizontal_rule()
    report.bold("This is bold text")
    report.horizontal_rule()
    report.italic("This is italic text")
    report.horizontal_rule()
    report.bullet_points("This", "Is", "Test", "For", "Bullet", "Points")
    report.horizontal_rule()
    report.numbered_list("This", "Is", "Test", "For", "Numbered", "List")
    report.horizontal_rule()
    report.link("This is a link", "https://www.google.com/") 
    report.horizontal_rule()
    report.image("./image.png","Test Image")
    report.horizontal_rule()
    report.image("./non_existent_image.png","Non existent image","Test for alternative text")
    report.horizontal_rule()
    report.code_block("python","#This is python syntax \n a = 6 \n b = 5 \n a+b = 11 \n def sum(a,b): \n    return a+b")
    report.horizontal_rule()
    report.blockquote("This is a blockquote")
    report.save("./report.md")

if __name__ == "__main__":
    pass