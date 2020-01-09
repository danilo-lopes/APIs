from list_user_playlist import printUserPlaylists
from controller import getUserToken, renewToken, haveControllerAcess


def menu():
    print(10 * "-", "Menu", 10 * "-")
    print("1. List User Playlist")
    print("0. Exit")
    print(26 * "-")


while True:
    menu()
    choice = input("Enter option [1-5]: ")

    if choice == "1":
        token = getUserToken()

        haveAccess = haveControllerAcess(token)

        if haveAccess == 'Unauthorized':
            token = renewToken(token)
            printUserPlaylists(token)
        
        else:
            printUserPlaylists(token)

    elif choice == "0":
        exit()
