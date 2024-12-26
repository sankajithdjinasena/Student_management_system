# Import necessary Libraries 
import csv
import re


file_name = "Student_details.csv" # This is the csv file name that I used to read and save data.
x = " " # This variable I used to make space in titles

# Using re module for check validation of phone number
def is_valid_phone_number(phone):
    phone_regex = r'(94[0-9]{9}$)'
    return re.match(phone_regex, phone) is not None
    
def read_from_csv():
    try:
        # read file in read mode
        with open(file_name, mode='r') as file:
            # Reads the CSV file and converts each row into a dictionary, where the keys are the column headers from the CSV file.
            reader = csv.DictReader(file)

            # Initializes an empty list to store the processed student data.
            students = [] 
            
            for row in reader:
                students.append({
                    'id': row['id'],
                    'name': row['name'],
                    'age': int(row['age']),
                    'degree': row['degree'],
                    'gpa': float(row['gpa']),
                    'contactInfo': row['contactInfo'],
                    'email' : row['email'],
                    'district': row['district']
                })
            
            print(f"Data successfully loaded from {file_name}\n")
            # return students list
            return students
            
    except FileNotFoundError:
        # Return a message if the file is not found
        print(f"File {file_name} not found. Starting with an empty list.\n")
        
    except Exception as e:
        # Return a message if an error occurred while reading the file
        print(f"An error occurred while reading the file: {e}\n")

def save_to_csv():
    try:
        # read file in write mode
        with open(file_name,'w', newline='') as file:
            fieldnames = ['id', 'name', 'age', 'degree', 'gpa', 'contactInfo','email','district']

            # write the csv as a dictionary
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for student in students:
                # Write student list record in row-wise
                writer.writerow(student)
                
            # return message if data saved to the csv successfully. 
            print(f"Data successfully saved to {file_name}\n")
            
    except Exception as e:
        # Return a message if an error occurred while saving the file
        print(f"An error occurred while saving: {e}\n")

def add_student():
    print("-" * 114)
    print(f"{x:36}Add Student to Student Management System\n")
    
    try:
        # Get student's academic year and get its last 2 digit to create student ID
        year = int(input("\tEnter the year: ")[-2:])
        
        # Get student's Degree program
        print("\tEnter your degree Program:\t\n\t1. Data Science(CDS)\n\t2. Software Engineering(CSE)\n\t3. Computer Information System(CIS)")
        degree_n = int(input("\tEnter Degree: "))
        if degree_n == 1:
            degree = "CDS";
        elif degree_n == 2:
            degree = "CSE";
        elif degree_n == 3:
            degree = "CIS";
        else:
            raise ValueError

        # Get student ID last digits      
        student_id = int(input("\tEnter Student last digits: "))
        padded_num = str(student_id).rjust(4, '0')
        student_id = f"{year}{degree}{padded_num}"

        # Filtering to check the that student is already in the database or not
        filtered_students = [student for student in students if student['id'].upper() == student_id.upper()]
        if filtered_students:
            # Return a message if student in the database
            print("\tStudent ID already in database.")
            main()
            
        else: 
            # Get student's name     
            name = input("\tEnter Student Name: ")
            # Get student's age  
            age = int(input("\tEnter Age: "))

            # When student adding to the database, normally GPA = 0
            gpa = 0.0

            # Get student's contact number  
            contactInfo = input("\tEnter you contact number (Start with 94): ")
            while True:
                # Cheking telephone number validation (According to Sri Lanka format - 947XXXXXXXX)
                if is_valid_phone_number(contactInfo):
                    contactInfo = contactInfo
                    break
                else:
                    # Return a message if entered number is not in the right format and go back to main
                    print("\tInvalid Phone Number")
                    main()

            # Get student's district
            district = input("\tWhat is your district: ").capitalize()

            # Asking permission to submit data   
            submit = int(input("\tEnter 1 to submit or Enter 0 to go back to main menu: "))
            if submit == 1: # If entered value = 1, the data save to the database
                pass
            elif submit == 0: # If entered value = 0, the data not save to the database
                print("\tRecord not saved.")
                print("\tBacking to main menu...")
                main()
            else:
                raise ValueError

        # Creating unique email for each student using their degree program, academic year and last digit
        email = f"{student_id}@ac.sab.lk"
                
        # Append data into student list
        students.append({"id": student_id, "name": name, "age": age, "degree": degree, "gpa": gpa, "contactInfo": contactInfo, 'email':email,'district':district})

        # Return a message if data added to the list successfully.
        print("\tStudent added successfully!")
        # Return unique email for the student
        print(f"\n\tStudent Email: {email}\n")
    except ValueError:
        # Print a message when added a record in wrong format
        print("\tInvalid input. Please try again.")


def view_students():
    while True:
        print("-" * 114)
        print(f"{x:38}Search Student in Student Management System\n")
        
        # View option
        print("\t1. View all student") # View all the students data in database
        print("\t2. View Students by Student ID") # Filtering students by their ID
        print("\t3. View Students by Degree") # Filtering students by their Degree
        print("\t4. View Students by GPA") # Filtering students by their GPA
        print("\t5. View Students by District") # Filtering students by their District
        print("\t6. Delete record") # Delete records
        print("\t7. Update Student record") # Update student's records
        print("\t8. Update GPA") # Update student's GPA
        print("\t9. Back") # Backing to main menu

        print("\n\t(Enter the option number)\n")

        # Read user input
        choice = input("\tEnter your choice: ")
        print()

        if choice == "1":
            # check the list
            # 1. If the there is student in the list , print his/him details 
            # 2. If the there is no student in the list, print "No student found" message.
            if not students:
                print("\tNo students found.")
                return
            print("-" * 114)
            print(f"  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
            print("-" * 114)
            for student in students:
                # If there are data, print students data.
                print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
            print()
            
        elif choice == "2":
            # Calling to filter by ID option
            filter_by_id()

        elif choice == "3":
            # Calling to filter by Degree option
            filter_by_degree()

        elif choice == "4":
            # Calling to filter by GPA
            filter_by_gpa()
            
        elif choice == "5":
            # Calling to filter by District
            filter_by_district()

        elif choice == "6":
            # Calling to delete record option
            delete_student()

        elif choice == "7":
            # Calling to record update student's data option
            update_student()
        elif choice == "8":
            # Calling to record update student's GPA option
            update_GPA()

        elif choice == "9":
            print("\tBacking...")
            break
            
        else:
            # Return a message if the user entered a wrong input
            print("\tInvalid choice. Please try again.")

def filter_by_id():
    print("-" * 114)
    # Get user input for flter data by ID
    student_id = input("\tEnter the Student ID to search for: ").strip()
    print("\n")
    # Checking the similar data for entered student ID and make a new list called filtered_students
    filtered_students = [student for student in students if student['id'].upper() == student_id.upper()]
    
    if filtered_students:
        print(f"  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
        print("-" * 114)
        for student in filtered_students:
            # If there are data in filtered_students, print students data.
            print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
        print()
    else:
        # Return a message if there is no student found with the entered ID.
        print(f"\tNo student found with ID: {student_id}")

def filter_by_degree():
    print("-" * 114)
    # Get user input for flter data by Course Code
    print("\tDegree programs are: CDS/CSE/CIS")
    degree = input("\tEnter the Degree to search for: ").strip()
    print("\n")
    # Checking the similar data for entered Course cod and make a new list called filtered_course
    filtered_degree = [student for student in students if student['degree'].upper() == degree.upper()]
    
    if filtered_degree:
        print(f"  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
        print("-" * 114)
        for student in filtered_degree:
            # If there are data in filtered_course, print students data.
            print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
        print()
    else:
        # Return a message if there is no student found with the course code.
        print(f"\tNo student found with Degree: {degree}")

def filter_by_district():
    print("-" * 114)
    # Get user input for flter data by District
    district_c = input("\tEnter the District to search for: ").strip().capitalize()
    print("\n")
    # Checking the similar data for entered Districtand make a new list called filtered_district
    filtered_district = [student for student in students if student['district'].upper() == district_c.upper()]
    
    if filtered_district:
        print(f"  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
        print("-" * 114)
        for student in filtered_district:
            # If there are data in filtered_district, print students data.
            print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
        print()
    else:
        # Return a message if there is no student found with the district.
        print(f"\tNo student found with District: {district_c}")

def filter_by_gpa():
    print("-" * 114)
    # Get user input for flter data by GPA
    gpa = float(input("\tEnter the GPA to search for: "))
    print("\n")
    while True:
        print("\tSelect Option")
        print("\t1. Equal to") 
        print("\t2. Greater than")
        print("\t3. Less than")
        print("\t4. Back")
        print("\n\t(Enter the option number)\n")
        mark = input("\tEnter the Option: ").strip()
        if int(mark) > 4 or int(mark) == 0 :
            # Return a message if user entered a wrong input
            print("\tInvalid choice. Please try again.")
        elif int(mark) == 4:
            print("\tBacking...")
            break
        else:
                # Flitering students details that equal to user's input GPA
            if int(mark) == 1 :
                filtered_students = [student for student in students if student['gpa'] == gpa]
                # Flitering students details that greater than to user's input GPA
            elif int(mark) == 2:
                filtered_students = [student for student in students if student['gpa'] > gpa]
                # Flitering students details that less than to user's input GPA
            elif int(mark) == 3:
                filtered_students = [student for student in students if student['gpa'] < gpa]
                
            if filtered_students:
                print(f"  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
                print("-" * 114)
                for student in filtered_students:
                    print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
                print()
            else:
                print("\tNo student.\n")

def delete_student():
    print("-" * 114)
    print(f"{x:49}Delete Data\n")
    # Taking student ID for delete data
    student_id = input("\tEnter the Student ID to delete: ").strip()
    print("\n")
    # Taking entered student course code for delete data
    # If the entered ID and that student enrolled with the course code and there is a record in the database, record will delete
     # If the entered ID true but that student enrolled with the course code is not match with the entered course code, the record not delete.
    filtered_course = [student for student in students if student['id'].upper() == student_id.upper() ]

    if not filtered_course:
        print(f"\tNo student found with that id: {student_id}")


    for student in filtered_course:
        if student :
            # Remove the student if the above condition comes true
            students.remove(student)
            print(f"\tStudent with ID {student_id} has been deleted.")
            return
        

def update_GPA():
    # Taking student ID for updating GPA
    student_id = input("\tEnter the Student ID to update: ").strip()
    print("\n")
    student_found = False  # Flag to track if a student is found

    for student in students:
        # Checking the particular student ID
        if student['id'].upper() == student_id.upper():
            student_found = True
            print(f"\tCurrent data for Student ID {student_id}:")
            # Return current details of the student
            print(f"\t\tName: {student['name']}, \n\t\tDegree Program: {student['degree']},\n\t\tGPA: {student['gpa']}")
            # Get new GPA value
            new_gpa = input("\tEnter new GPA (or press Enter to keep current): ").strip()
            if new_gpa:
                try:
                    gpa_value = float(new_gpa)
                    if 0.0 <= gpa_value <= 4.0:  # Validate GPA range
                        student['gpa'] = gpa_value
                        print(f"\t{student_id}'s GPA changed to {gpa_value}")
                    else:
                        print("\tInvalid GPA. Please enter a value between 0.0 and 4.0.")
                except ValueError:
                    print("\tInvalid GPA. Keeping current value.")
            else:
                print("\tNo changes made to the GPA.")
            return  # Exit after updating

    if not student_found:
        print(f"\tNo student found with ID {student_id}.")

def update_student():
    student_id = input("\tEnter the Student ID to update: ").strip()
    print("\n")
    for student in students:
        if student['id'].upper() == student_id.upper() :
            print(f"\tCurrent data for Student ID {student_id}:")
            # Return the current data of student
            print(f"\t\tName: {student['name']} \n\t\tAge: {student['age']}\n\t\tDegree Program: {student['degree']}\n\t\tGPA: {student['gpa']}\n\t\tContact Number: {student['contactInfo']}\n\t\tEmail: {student['email']}\n\t\tDistrict: {student['district']}\n")
            # Get new Name for entered ID
            new_name = input("\tEnter new name (or press Enter to keep current): ").strip()
            # Get new age for entered ID
            new_age = input("\tEnter new age (or press Enter to keep current): ").strip()
            # Get new contact number for entered ID
            new_contactInfo = input("\tEnter new contact number (or press Enter to keep current): ").strip()
            # Get new district for entered ID
            new_district = input("\tEnter new district (or press Enter to keep current): ").strip()

            # update new details for entered student ID
            if new_name:
                student['name'] = new_name
            if new_district:
                student['district'] = new_district
            if new_contactInfo:
                check = is_valid_phone_number(new_contactInfo)
                if check:
                    student['contactInfo'] = new_contactInfo
                else:
                    print("\tInvalid Phone Number. Try again")
                    update_student()
            if new_age:
                try:
                    student['age'] = int(new_age)
                except ValueError:
                    print("\tInvalid age. Keeping current value.")
        
            print("\tStudent data updated successfully!")
            return
    
    print(f"\tNo student found with ID: {student_id}")
    view_students()

def get_report():
    student_id = input("\tEnter the Student ID to get Report: ").strip().upper()
    print("\n")
    student_find = False
    print("-" * 114)
    print(f"{x:42}Report of Student ID: {student_id}\n")
    for student in students:  
        if student['id'].upper() == student_id.upper() :
            student_find = True
            # Return the current data of student
            print(f"\tStudent ID: {student['id']} \n\tName: {student['name']} \n\tAge: {student['age']} \n\tDegree Program: {student['degree']}\n\tGPA: {student['gpa']}\n\tContact Number: {student['contactInfo']}\n\tEmail: {student['email']}\n\tDistrict: {student['district']}")
            print("\n\tDegree Programs:\t\n\t\t1. Data Science(CDS)\n\t\t2. Software Engineering(CSE)\n\t\t3. Computer Information System(CIS)\n")
            print()
    if not student_find :        
        print(f"\tNo student found with ID: {student_id}")

def student_main(student_id):
    while True:
        print("\n"+"-" * 114)
        print("\t1. View my data")
        print("\t2. Update my data")
        print("\t3. Report")
        print("\t4. Back")
        choice = input("\tEnter choice number: ")
    
        if choice == "1":
            # calling to student view option
            student_view(student_id)
        elif choice == "2":
            # calling to student update option
            student_update(student_id)
        elif choice == "3":
            # calling to student report option
            student_report(student_id)
        elif choice == "4":
            print("\tBacking...\n\n")
            save_to_csv()
            break
            break
        else:
            print("\tInvalid choice. Please try again.")

def student_view(student_id):
    filtered_students = [student for student in students if student['id'].upper() == student_id.upper()]
    if filtered_students:
        print(f"\n  {'ID':<10}{'Name':<30}{'Age':<5}{'Degree':<10}{'GPA':<5}{'Contact Number':<17}{'Email':<22}{'District':<15}")
        print("-" * 114)
        for student in filtered_students:
            # If there are data in filtered_students, print students data.
            print(f"  {student['id']:<10}{student['name']:<30}{student['age']:<5}{student['degree']:<10}{student['gpa']:<5}{student['contactInfo']:<17}{student['email']:<22}{student['district']:<15}")
        print()

def student_update(student_id):
    for student in students:
        if student['id'].upper() == student_id.upper() :
            print(f"\tCurrent data for Student ID {student_id}:")
            # Return the current data of student
            print(f"\t\tName: {student['name']} \n\t\tAge: {student['age']}\n\t\tDegree Program: {student['degree']}\n\t\tGPA: {student['gpa']}\n\t\tContact Number: {student['contactInfo']}\n\t\tEmail: {student['email']}\n\t\tDistrict: {student['district']}\n")
            # Get new age for entered ID
            new_age = input("\tEnter new age (or press Enter to keep current): ").strip()
            # Get new contact number for entered ID
            new_contactInfo = input("\tEnter new contact number (or press Enter to keep current): ").strip()
            # Get new district for entered ID
            new_district = input("\tEnter new district (or press Enter to keep current): ").strip()

            # update new details for entered student ID
            if new_district:
                student['district'] = new_district
            if new_contactInfo:
                check = is_valid_phone_number(new_contactInfo)
                if check:
                    student['contactInfo'] = new_contactInfo
                else:
                    print("\tInvalid Phone Number. Try again")
            if new_age:
                try:
                    student['age'] = int(new_age)
                except ValueError:
                    print("\tInvalid age. Keeping current value.")
        
            print("\tStudent data updated successfully!")
            return
    print(f"\tNo student found with ID: {student_id}")


def student_report(student_id):
    student_find = False
    print("-" * 114)
    print(f"{x:42}Report of Student ID: {student_id}\n")
    for student in students:  
        if student['id'].upper() == student_id.upper() :
            student_find = True
            # Return the current data of student
            print(f"\tStudent ID: {student['id']} \n\tName: {student['name']} \n\tAge: {student['age']} \n\tDegree Program: {student['degree']}\n\tGPA: {student['gpa']}\n\tContact Number: {student['contactInfo']}\n\tEmail: {student['email']}\n\tDistrict: {student['district']}")
            print("\n\tDegree Programs:\t\n\t\t1. Data Science(CDS)\n\t\t2. Software Engineering(CSE)\n\t\t3. Computer Information System(CIS)\n")
            print()
    if not student_find :        
        print(f"\tNo student found with ID: {student_id}")

def main():
    while True:
        print("-" * 114)
        print(f"{x:45}STUDENT MANAGEMENT SYSTEM")
        print("-" * 114)
        # Main menu options for admin
        print("\t1. Add Student")
        print("\t2. View Students")
        print("\t3. Generate Report")
        print("\t4. Save file")
        print("\t5. Back to Login menu")
        
        print("\n\t(Enter the option number.)\n")
        
        choice = input("\tEnter your choice: ")
        print()

        # Checking the user input and calling to requested method
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            get_report()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("\tBacking...\n\n")
            save_to_csv()
            break
            break
        else:
            print("\tInvalid choice. Please try again.")

# Calling to main 
if __name__ == "__main__":
    students = read_from_csv()
    while True:
        print("-" * 114)
        print(f"{x:40}Welcome to Student Management System")
        print("-" * 114)
        print("\n\t1. Admin")
        print("\t2. Student")
        print("\t3. Exit\n")
    
        choice = input("\tEnter choice number: ")
        if choice == "1":
            # Get admin user name
            username = input("\tEnter user name: ").lower()
            # Get admin password
            password = input("\tEnter password: ")
            if username == "admin" and password == "1234":
                main()
            else:
                print("\tInvalid user name or password. Try again")
        elif choice == "2":
            student_id = input("\tEnter the Student ID to Login: ").strip().upper()
            filtered_students = [student for student in students if student['id'].upper() == student_id.upper()]
            if filtered_students:
                contact_number = input("\tEnter the contact number to Login: ").strip().upper()
                filtered_students = [student for student in filtered_students if student['contactInfo'].upper() == contact_number.upper()]
                if filtered_students:
                    student_main(student_id)  
                else:
                    print("\tInvalid contact number.")
            else:
                print(f"\tNo student found with ID: {student_id}")
            
        elif choice == "3":
            print("\tExiting...\n\n")
            save_to_csv()
            break
            break
        else:
            print("\tInvalid choice. Please try again.")



