from pymarkdownreport.mdreport import MDReport


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
    table, ax = report.table(3)
    ax[0].header = "Text"
    ax[1].header = "Image1"
    ax[2].header = "Image2"
    ax[1].text("This is the firts image.")
    ax[1].image("./image.png","This is an image in a table")
    ax[2].text("This is the second image")
    ax[2].image("./image.png","This is an image in a table")
    ax[0].italic("This is some italic in a table we line break it")
    ax[0].text("This is a very long text aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    ax[0].bullet_points("This", "Is", "Test", "For", "Bullet", "Points")
    report.draw_table(table)
    report.save("./report.md")

if __name__ == "__main__":
    test_mdreport()