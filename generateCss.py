#Declarations

def create_css(boundvalues):
    left=0
    top=0
    width=0
    height=0
    selector=""
    position="position:absolute;"
    border="\nborder:solid;"
    width_str1="{width: 100%;}"
    width_str2="{width: 150%;}"
    width_str3="{width: 200%;}"
    fp = open("style.css","w")
    for itr_each in boundvalues:
        selectorname = str(itr_each[0])
        selector_list = selectorname.split()
        selector = selector_list[0]
        fp.write("\n."+str(selector)+"{\n")
        fp.write(str(border))
        width = itr_each[3]-left
        height = itr_each[4]-top
        fp.write("\nleft:"+str(left)+";\ntop:"+str(top)+";\nwidth:"+str(width)+";\nheight:"+str(height)+";\n}")
    fp.write("\n@media screen and (max-width:600px) {\n .header:"+str(width_str1)+".footer:"+str(width_str1)+"}")
    fp.write("\n@media screen and (min-width:600px) and (max-width:768px){\n .header:"+str(width_str2)+".footer:"+str(width_str2)+"}")
    fp.write("\n@media screen and (min-width:768px){\n .header:"+str(width_str3)+".footer:"+str(width_str3)+"}")
        