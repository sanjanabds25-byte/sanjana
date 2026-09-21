

candidates = []
applications = []
interviews = []


# Add Candidate
def add_candidate():
    candidate_id = input("Enter Candidate ID: ")
    name = input("Enter Candidate Name: ")
    email = input("Enter Email: ")
    skills = input("Enter Skills: ")

    candidate = {
        "id": candidate_id,
        "name": name,
        "email": email,
        "skills": skills
    }

    candidates.append(candidate)
    print("Candidate added successfully!\n")


# Add Job Application
def add_application():
    application_id = input("Enter Application ID: ")
    candidate_id = input("Enter Candidate ID: ")
    job = input("Enter Job Title: ")

    application = {
        "id": application_id,
        "candidate_id": candidate_id,
        "job": job,
        "status": "Applied"
    }

    applications.append(application)
    print("Job application added successfully!\n")


# Schedule Interview
def schedule_interview():
    interview_id = input("Enter Interview ID: ")
    candidate_id = input("Enter Candidate ID: ")
    date = input("Enter Interview Date: ")

    interview = {
        "id": interview_id,
        "candidate_id": candidate_id,
        "date": date,
        "status": "Scheduled"
    }

    interviews.append(interview)
    print("Interview scheduled successfully!\n")


# HR Analytics
def show_analytics():
    print("\n===== HR ANALYTICS =====")
    print("Total Candidates :", len(candidates))
    print("Total Applications:", len(applications))
    print("Total Interviews  :", len(interviews))

    selected = 0

    for application in applications:
        if application["status"] == "Selected":
            selected += 1

    print("Selected Candidates:", selected)
    print("========================\n")


# Display Candidates
def show_candidates():
    print("\n===== CANDIDATES =====")

    if len(candidates) == 0:
        print("No candidates found.")
    else:
        for c in candidates:
            print("ID:", c["id"])
            print("Name:", c["name"])
            print("Email:", c["email"])
            print("Skills:", c["skills"])
            print("-------------------")


# Main Menu
while True:

    print("\n===== RECRUITMENT & HR ANALYTICS PORTAL =====")
    print("1. Add Candidate")
    print("2. Add Job Application")
    print("3. Schedule Interview")
    print("4. Show Candidates")
    print("5. HR Analytics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_candidate()

    elif choice == "2":
        add_application()

    elif choice == "3":
        schedule_interview()

    elif choice == "4":
        show_candidates()

    elif choice == "5":
        show_analytics()

    elif choice == "6":
        print("Thank you for using HR Portal!")
        break

    else:
        print("Invalid choice. Please try again.")