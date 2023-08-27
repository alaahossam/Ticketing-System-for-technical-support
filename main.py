
# Importing required modules
import json

# Function to load issue types from an external file
def load_issue_types():
    with open('issue_types.json', 'r') as file:
        issue_types = json.load(file)
    return issue_types

# Function to display available issue categories
def display_categories(issue_types):
    print("Available categories:")
    for category in issue_types:
        print("-", category)

# Function to display issue types within a category
def display_issue_types(issue_types, category):
    if category in issue_types:
        print("Issue types in category", category + ":")
        for issue_type in issue_types[category]:
            print("-", issue_type)
    else:
        print("Category not found!")

# Function to create a support ticket
def create_ticket(issue_types):
    category = input("Enter the category of the issue: ")
    display_issue_types(issue_types, category)
    issue_type = input("Enter the issue type: ")
    description = input("Enter a brief description of the issue: ")

    # Create the ticket
    ticket = {
        "category": category,
        "issue_type": issue_type,
        "description": description
    }
    print("Ticket created successfully!")
    print(ticket)

# Main program
def main():
    # Load issue types from external file
    issue_types = load_issue_types()

    # Display available categories
    display_categories(issue_types)

    # Create a ticket
    create_ticket(issue_types)

# Run the main program
if __name__ == '__main__':
    main()
