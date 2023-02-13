import mysql.connector

def query_database(query, data=None):
    # Connect to the database
    conn = mysql.connector.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx"
    )
    
    # Create a cursor and execute the query
    cursor = conn.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    
    # Fetch the results of the query
    results = cursor.fetchall()
    
    # Clean up and close the connection
    cursor.close()
    conn.close()
    
    return results

def add_user(name, birthday):
    query = "INSERT INTO users (name, birthday) VALUES (%s, %s);"
    data = (name, birthday)
    query_database(query, data)

def update_user(name, birthday, id):
    query = "UPDATE users SET name = %s, birthday = %s WHERE id = %s;"
    data = (name, birthday, id)
    query_database(query, data)

def delete_user(id):
    query = "DELETE FROM users WHERE id = %s;"
    data = (id,)
    query_database(query, data)

def show_users():
    query = "SELECT * FROM users;"
    results = query_database(query)
    for result in results:
        print(result)

def main_menu():
    print("1. Add user")
    print("2. Update user")
    print("3. Delete user")
    print("4. Show users")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_user_menu():
    name = input("Enter the name: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")
    add_user(name, birthday)
    print("User added successfully.")

def update_user_menu():
    id = int(input("Enter the id of the user to update: "))
    name = input("Enter the new name: ")
    birthday = input("Enter the new birthday (YYYY-MM-DD): ")
    update_user(name, birthday, id)
    print("User updated successfully.")

def delete_user_menu():
    id = int(input("Enter the id of the user to delete: "))
    delete_user(id)
    print("User deleted successfully.")

def show_users_menu():
    print("\nShowing Users:")
    print("---------------")
    users = query_database("SELECT * FROM users")
    if len(users) == 0:
        print("No users found in the database.")
    else:
        for i, user in enumerate(users):
            print(f"{i+1}. {user[1]} {user[2]}")
    print("\n")

# Main program loop
while True:
    choice = main_menu()
    if choice == 1:
        add_user_menu()
    elif choice == 2:
        update_user_menu()
    elif choice == 3:
        delete_user_menu()
    elif choice == 4:
        show_users_menu()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")