from typing import Tuple
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
        self.report += f"```{language}\n {text} \n```\n"

    def blockquote(self, text:str):
        self.report += f"> {text}\n"

    def horizontal_rule(self): 
        self.report += f"---\n"

    def save(self, filepath:str):
        with open(filepath,'w') as f:
            f.write(self.report)
    
    def table(self, width: int):
        table: MDTable = MDTable(width)
        return table, table.tables

    def draw_table(self, table):
        self.report += "\n"
        self.report += table.draw() 

class MDTable(MDReport):
    """This class is used to create tables"""

    def __init__(self, width:int): 
        self.report = ""
        self.single_table: MDTableElement = MDTableElement()
        self.tables: Tuple[MDTableElement] = ()

        for i in range(0,width):
            single_table: MDTableElement = MDTableElement()
            self.tables += (single_table,) 
    
    def draw(self) -> str:
        table:str = "|" 
        for _table in self.tables: 
            # write headers
            table += f"{_table.header}|"
        table += "\n|"
        for _table in self.tables: 
            # write headers
            table += f"---|"
        table += "\n|"
        for _table in self.tables: 
            # write content
            report = _table.report.replace("\n","<br />")
            table += f"{report}|"

        return table


class MDTableElement(MDReport): 
    """Class to wrap a single element of a table. 
    """
    def __init__(self):
        self.header: str = ""
        self.report:str = ""


if __name__ == "__main__":
    pass