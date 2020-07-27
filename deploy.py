## More people probably have python on their system so I will use python.
import os 
import shutil
import subprocess

## Remove all html files and track all md files except for the template
whitelist_htmls = ["per_page_template.html"]
blacklist_mds = ["README.md"]
html_files=[]
md_files=[]
for (root,dirs,files) in os.walk('.'): 
    for f in files:
        if ".md" in f and not f in blacklist_mds:
            md_files.append(os.path.join(root,f))
        if ".html" in f and not f in whitelist_htmls:
            html_files.append(os.path.join(root,f))
for h in html_files:
    os.unlink(h)

## Populate the contents
md_paths=[]
for m in md_files:
    basepath = m[:-3]
    if basepath[-5:]=="index":
        basepath = basepath[:-6]
    mdfile=open(m)
    mdlines = mdfile.readlines()
    md_paths.append((mdlines[0][1:].strip()+"\n",basepath))
    mdfile.close()
md_paths=sorted(md_paths)

pptfile=open("per_page_template.html")
pptlines=pptfile.readlines()
pptfile.close()

to_remove=False
final_lines=[]
for l in pptlines:
    if "populate TOC here" in l:
        to_remove=True
        final_lines.append(l)
        for m in md_paths:
            final_lines.append("<p><a href='{}'>{}</a></p>\n".format(m[1][1:], m[0].rstrip()))
    elif "end populate TOC" in l: 
        to_remove=False
        final_lines.append(l)
    elif to_remove:
        continue
    else:
        final_lines.append(l)
pptfile=open("per_page_template.html","w")
pptfile.write("".join(final_lines))
pptfile.close()

for m in md_files:
    basepath = m[:-3]
    if basepath[-5:]=="index":
        basepath = basepath[:-6]
    ## make the directory 
    os.makedirs(basepath,exist_ok=True)
    htmlpath = os.path.join(basepath,"index.html")
    shutil.copy("per_page_template.html",htmlpath)
    ## fill in the spot for the MD
    mdfile=open(m)
    mdlines = mdfile.readlines()
    mdfile.close()
    
    contribs = (subprocess.check_output(['git', 'log','--follow','--name-only',m[2:]])).decode('ascii')
    contribs = contribs.split("\n")
    if (len(contribs)<2):
        print("Warning: File {} has not been git committed. Please git commit your file so we can credit you :)".format(m))
    else:
        last_update_time=contribs[2][5:].strip()
        
        contribs = filter(lambda i: i[:7]=="Author:",contribs)
        contrib_dict={}
        for c in contribs:
            contrib_dict[c[7:].split("<")[0]]=True
        contrib_list= list(contrib_dict.keys())
        
        mdlines.insert(1,"Last updated:" + last_update_time+"\n")
        mdlines.insert(2,"Contributors:" + ",".join(contrib_list)+"\n")
    htmlfile = open(htmlpath)
    htmllines=htmlfile.readlines()
    htmlfile.close()
    for v,l in enumerate(htmllines):
        if "<title>" in l:
            htmllines.insert(v+1,mdlines[0][1:].strip()+"\n")
        if "insert markdown content here" in l:
            htmllines.insert(v+1,"".join(mdlines)+"\n")
    
    htmlfile=open(htmlpath,"w")
    htmlfile.write("".join(htmllines))
    
