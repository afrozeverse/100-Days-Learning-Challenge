import markdown as md

def convertToHtml(md_file,html_file):
    try:
        with open(md_file,'r') as file:
            md_text=file.read()

        html_text=md.markdown(md_text)

        with open(html_file,'w') as file:
            file.write(html_text)
        print("SUCCESS: Convertion succesful.")
    except:
        print("ERROR: Convertion error!")
    
convertToHtml('sample.md','converted.html')