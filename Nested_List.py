# Nested List 

# A nested list in Python is essentially a list that contains other lists as its elements.
# This structure allows you to create multi-dimensional data representations, which can be useful for various applications like matrices, tables, or complex data arrangements.

#   A nested list is just a list Within the list

# Nested lidt example 
nested_list = [[1,2,3],[4,5],[6,7,8]]

# flattening the nested list using function
def listObjectId(rolesArray):
    values = []
    for i in rolesArray:
        for j in i:
            values.append(j)
    return values

flat_list = listObjectId(nested_list)
print(flat_list)


#output = [1,2,3,4,5,6,7,8,9]




