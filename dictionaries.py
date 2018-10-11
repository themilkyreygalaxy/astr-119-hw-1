#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	78
}
print(type(example_dict))	#will say dict

#get a value via key
course = example_dict["class"]
print(course)

#change the value via key
example_dict["awesomeness"] += 3	#increase awesomeness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])