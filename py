# Create a list of first names
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

# Create a list of preferred sizes for some customers
preferred_size = ['Small', 'Large', 'Medium']

# Add Depak's preferred size to the list
preferred_size.append('Medium')

# Print the updated list of preferred sizes
print(preferred_size)

# Create a two-dimensional list with customer data: name, size, and expedited shipping preference
customer_data = [
    ['Ainsley', 'Small', True],
    ['Ben', 'Large', False],
    ['Chani', 'Medium', True],
    ['Depak', 'Medium', False]
]

# Print the initial customer data
print(customer_data)

# Update Chani's shipping preference to False (regular shipping)
customer_data[2][2] = False

# Remove Ben's shipping preference as he is unsure
customer_data[1].remove(False)

# Combine existing customer data with new customers' data
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

# Print the final customer data
print(customer_data_final)
