import generateCss
from generateHtml import aa

#Declarations
selector_unique = []
selector_only = []
replaced_list = []

#Getting unique selector
def remove_duplicate(duplicate):
    selector_unique = [] 
    for itr in duplicate: 
        if itr not in selector_unique: 
            selector_unique.append(itr) 
    return selector_unique  


def boundRef(boundvalues):
    #Removing Confidence Value
    for itr_each in boundvalues:
        selectorname = str(itr_each[0])
        selector_list = selectorname.split()
        selector = selector_list[0] 
        itr_each[0] = selector
        selector_only.append(selector)
    selector_unique = remove_duplicate(selector_only)
    #Counting the selector
    for itr in selector_unique:
        selector_unique_count = selector_only.count(itr)
        itr_init = 1
        select_name = itr 
        if selector_unique_count > 1:
            for name in selector_only :
                if name ==select_name:
                    name = select_name + str(itr_init)
                    itr_init+=1
                    replaced_list.append(name)
        else:
            replaced_list.append(select_name)

    #Replacing the original list by renamed selectors
    iterator = 0
    for itr in range(0,len(boundvalues)):
        boundvalues[iterator][0] = replaced_list[iterator]
        iterator = iterator+1
    return boundvalues
    
#Generating CSS,Html and Dictionary
def createFiles(boundvalues):
    refined_list = boundRef(boundvalues)
    generateCss.create_css(refined_list)
    obj2=aa()
    print(aa)
    obj2.createDict(boundvalues)
    obj2.create_html(refined_list)
    print("end")


