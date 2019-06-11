#Declarations
import operator
class aa:
    def __init__(self):
        self.selector_list = []
        self.selector_only = []
        self.selector_unique = []
        self.stack=[]
        self.stack_top=-1
        self.open_dict={}
        self.close_dict={}
        self.sorted_list=[]
        self.itr = 1

#remove_duplicate
    def remove_duplicate(self, duplicate):
        self.selector_unique = [] 
        for itr in duplicate: 
            if itr not in self.selector_unique: 
                self.selector_unique.append(itr) 
        return self.selector_unique  


#Creating the Dictionary
    def createDict(self, selectors):
        print("Selectors create dict",selectors)
        for itr_each in selectors:
            selector = str(itr_each[0])
            
            #selector_list = selectorname.split()
            #selector = selector_list[0] 
            #itr_each[0] = selector
            self.selector_only.append(selector)
            #print(self.selector_only)
        print("selectorname:",self.selector_only)
        self.selector_unique = self.remove_duplicate(self.selector_only)
        print("selector_unique:",self.selector_unique)
        for row in self.selector_only:
            #print("Entered dict")
            if row == 'header':
                self.open_dict['header']="<header class='header'>"
                self.close_dict['header']="</header>"
            elif row == 'footer':
                self.open_dict['footer']="<footer class='footer'>"
                print(self.open_dict['footer'])
                self.close_dict['footer']="</footer>"
            else:
                #self.selector_unique = self.remove_duplicate(self.selector_only)
                print("selector_unique:",self.selector_unique)
                for itr in self.selector_unique:
                    #print("f")
                    self.selector_unique_count = self.selector_only.count(itr)
                    #print(self.selector_unique_count)
                    itr_init = 1
                    select_name = itr 
                    if self.selector_unique_count >= 1:
                        #print("F1")
                        for name in self.selector_only :
                            if name == select_name:
                                name = select_name + str(itr_init)
                                itr_init+=1
                                #print("if")
                                if select_name == 'div':
                                    dict_name_1 = "<div class=\"" + name + "\">"
                                    dict_name_2 = "</div>"
                                    self.open_dict[name] = dict_name_1
                                    self.close_dict[name] = dict_name_2
                                elif select_name == 'multi-line':
                                    dict_name_1 = "<p class=\"" + name + "\">"
                                    dict_name_2 = "</p>"
                                    self.open_dict[name] = dict_name_1
                                    self.close_dict[name] = dict_name_2
                                elif select_name == 'image':
                                    dict_name_1 = "<img src='image.png' class=\"" + name + "\">"
                                    dict_name_2 = "</img>"
                                    self.open_dict[name] = dict_name_1
                                    self.close_dict[name] = dict_name_2       
        print(self.open_dict)
        print(self.close_dict)
    
    def push(self,element):
        self.stack.append(element)
        self.stack_top+=1
    
    def pop(self):
        element=self.stack.pop()
        self.stack_top-=1
        return element  
    
    
    def sort_list(self,box_list):
        TAG_NAME, XMIN, YMIN, XMAX, YMAX=(0,1,2,3,4)
        i=0
        while(len(box_list)>1):
            j=1
            self.push(box_list[i])
            self.sorted_list.append(box_list[i])
            while(j<len(box_list)):
                if(box_list[j][XMAX]<self.stack[self.stack_top][XMAX] and box_list[j][YMAX]<self.stack[self.stack_top][YMAX]):
                    self.push(box_list[j])
                    self.sorted_list.append(box_list[j])
                j+=1
            while(self.stack_top>=0):
                element=self.pop()
                box_list.remove(element)
        #self.sorted_list.append(box_list[i])
        return self.sorted_list
    
    def create_html(self,box_list):

        TAG_NAME, XMIN, YMIN, XMAX, YMAX=(0,1,2,3,4)
        sorted_list=self.sort_list(box_list)
        print(sorted_list)
        fp = open("generated_html_"+str(self.itr),"w")
        self.itr += 1
        fp.write("<html>\n<head><link rel='stylesheet' href='style.css'></head>\n<body>\n")
        print("<html>\n<head><link rel='stylesheet' href='style.css'></head>\n<body>\n")
        ##### html generation ############
        list_length=len(sorted_list)
        self.stack=[['dummy',-1,-1,-1,-1]]
        self.stack_top=0
        self.push(sorted_list[0])
        i=1
        print(self.open_dict[sorted_list[0][TAG_NAME]])
        fp.write(str(self.open_dict[sorted_list[0][TAG_NAME]]))
        while(i<list_length):
            if(sorted_list[i][YMAX]<self.stack[self.stack_top][YMAX]):
                self.push(sorted_list[i])
                print(self.open_dict[sorted_list[i][TAG_NAME]])
                fp.write(str(self.open_dict[sorted_list[i][TAG_NAME]]))
                fp.write("\n")
    
            else:
                while(sorted_list[i][YMAX]>=self.stack[self.stack_top][YMAX] and self.stack_top>0):
                    element=self.pop()
                    print(self.close_dict[element[TAG_NAME]])
                    fp.write("\n")
                self.push(sorted_list[i])
                print(self.open_dict[sorted_list[i][TAG_NAME]])
                fp.write(str(self.open_dict[sorted_list[i][TAG_NAME]]))
                fp.write("\n")
            i+=1
        while(self.stack_top>0):
            element=self.pop()
            print(self.close_dict[element[TAG_NAME]])
            fp.write(str(self.close_dict[element[TAG_NAME]]))
            fp.write("\n")
    
        fp.write("</body>\n</html>")
        fp.close()
    
        
    