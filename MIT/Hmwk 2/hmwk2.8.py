def report_card():
    class_names = []
    class_grades = []
    num_classes = int(input("How many classes did you take? "))
    print("Please enter name and grade for each class ")
    
    for i in range(num_classes):
         name = (input("What was the name of your class? "))
         grade = (input("what was your grade? "))
         class_names.append(name)
         class_grades.append(grade)
         
    for i in range(num_classes):
    #this concept works, but i do not know how to make this
    # keep going through list regardless of how many items in the list
    #print(class_names, "-", class_grades)
        print(class_names[0], class_grades[0])
        print(class_names[1], class_grades[1])
        print(class_names[2], class_grades[2])


report_card()


        
# () = tuples -- []= list -- {} = dictionaries
