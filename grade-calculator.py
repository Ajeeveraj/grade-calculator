# welcome
print("Welcome, please add your grades to the Smart grade analyzer.")


# define grades
def get_grades(avg):
    if avg < 50:
        return "F"
    elif avg < 69:
        return "D"
    elif avg < 76:
        return "C"
    elif avg < 86:
        return "B"
    else:
        return "A"

# input grades
def student_scores():
    scores = []
    print("Enter your grades, type done when your finished.\n")
    
    while True:
        user_input = input("Score ")
        
        if user_input.lower() == "done":
            break
        
        try:
            score = float(user_input)
            
            # Only valid scores
            if 0 <=score <= 100:
                scores.append(score)
            else:
                print("Invalid(must be 0-100).")
                   
        except ValueError:
            print("That is not a number try again!")
                   
    if not scores:
        print("Please enter your scores.")
        return
        
    #Calculations
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    letter_grade = get_grades(average_score)
        
    #Send results to user
    print("\n\n RESULTS")
    print(f"Average score:{average_score:.2f}")
    print(f"Highest score:{highest_score}")
    print(f"Lowest score:{lowest_score}")
    print(f"Final grade:{letter_grade}")
        
        
#Run the program
student_scores()
        
        
        
                   
           
            

        


    
    


    

    
    
        
   
    
