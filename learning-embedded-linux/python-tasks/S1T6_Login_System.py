def login_system():
    users = {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3"
    }

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")


login_system()

