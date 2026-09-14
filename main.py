def show_menu():
    print("\n===== Recruitment & HR Analytics Portal =====")
    print("1. Candidate Management")
    print("2. Job Application Management")
    print("3. Interview Scheduling")
    print("4. Recruitment Management")
    print("5. HR Analytics")
    print("6. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Candidate Management")
        elif choice == "2":
            print("Job Application Management")
        elif choice == "3":
            print("Interview Scheduling")
        elif choice == "4":
            print("Recruitment Management")
        elif choice == "5":
            print("HR Analytics")
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()