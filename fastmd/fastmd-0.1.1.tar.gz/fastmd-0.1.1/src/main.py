import fastmd as md

md_text = "# heading1\nhello"

html = md.tohtml(md_text)

print(html)
