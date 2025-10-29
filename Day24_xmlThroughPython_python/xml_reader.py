import xml.etree.ElementTree as et

#in html there is a DOM which represents the page as a tree DS, in XML same occurs.
#so we first fetch the whole tree DS
#next we fetch the root element from the tree DS
tree=et.parse('employee.xml')
root=tree.getroot()

#now we are gonna read all the sub elemets from employees using a loop (Here 'employee' is the subelement of 'employees')

for x in root.findall('employee'): #findall function reads, and returns a python list
    #Now the x in not content, it is the whole element, so we have to find the content inside the data.
    # so x=employee element
    #x.find('name') is the name elemnt inside the employee
    # and x.find('name').text is the content inside the name element
    #the upper task is been done to fetch al the data 
    name=x.find('name').text
    age=x.find('age').text
    gender=x.find('gender').text
    email=x.find('email').text
    phone=x.find('phone').text
    address=x.find('address').text
    print(name,' | ',age,' | ',gender,' | ',email,' | ',phone,' | ',address)
    #the upper thing fetches for one employee, because of the loop it is able to fetch all the employee data
    
    
