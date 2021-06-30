from bs4 import BeautifulSoup
import requests

parent_content=[]
webpage_url=input("Please enter Webpage URL:")

print("Please enter type of tag  ")
tag_type=int(input("Enter 1 for class tag, 2 for ID tag, enter 3 for CSS selector tag:  "))
parent_tag=input("Please enter parent tag:  ")


class_tags=input("Please enter class tags separated by a space. Press Enter if not applicable:  ").split()
css_tags=input("Please enter CSS tags separated by a space. Press Enter if not applicable:  ").split()


page = requests.get(webpage_url)
soup = BeautifulSoup(page.content, 'html.parser')

#Obtain parent tag content
if tag_type==1:
	parent_content=soup.find_all(class_=parent_tag)
if tag_type==2:
	parent_content=soup.find_all(id=parent_tag)
if tag_type==3:
	parent_content=soup.select(parent_tag)
new_list=[]


child_tag_content=[]
contact_list=[]

#Obtain content from children tags
for x in parent_content:
	child_tag_content=[]
	if class_tags !=[]:
		for i in range(len(class_tags)):
			temp=x.find(class_=[class_tags[i]])
			child_tag_content.append(temp)

	if css_tags !=[]:
		for i in range(len(css_tags)):
			temp=x.select(str(css_tags[i]))
			for y in temp:
				child_tag_content.append(y)

	#Compile contact list
	contact_list.append([' '.join(z.get_text().split()) if z is not None else "Not Available" for z in child_tag_content])

print (contact_list)

#print each list item from contact_list
#for r in contact_list:
#	print(r)
