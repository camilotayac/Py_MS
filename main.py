import function.linux_commands as fl
import library.library as library


def main():
    library.install_library()
    fl.create_folder('data')

if __name__ == "__main__":
    main()