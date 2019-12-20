from list_user_playlist import printUserPlaylists


def menu():
    print(10 * "-", "Menu", 10 * "-")
    print("1. List User Playlist")
    print("0. Exit")
    print(26 * "-")


while True:
    menu()
    choice = input("Enter option [1-5]: ")

    if choice == "1":
        printUserPlaylists()

    elif choice == "0":
        exit()
