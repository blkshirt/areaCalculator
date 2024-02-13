'''Area Calculator 
    by blkShirt'''

#you've made your way to the "functions section"
#here i have put the functions that will be reoccuring

def rec():
    length = int(input("Enter the base value other than zero:"))
    width = int(input("Enter the width value other than zero:"))
    Area = width*length #MATH
    print("Area = ",Area)
#clever function names huh?
def tri():
    base = int(input("Enter the base value other than zero:"))
    heigth = int(input("Enter the height value other than zero:"))
    Area = .5*(base*heigth) #MATH
    print("Area = ",Area)
#so original, 'circ'
def circ():
    radius = int(input("Enter the radius value:"))
    Area = 3.14*(radius**2) #MATH
    print("Area = ",Area)

#ahh, there's a loop but it's not on a rollercoaster
cont="y" or "yes"

while cont=="y" or "yes":
    shape = input("Enter a shape to calculate Area (rectangle, triangle, or circle):")
    shape = shape.lower()
#the two lines above this one is how the program determines what the user would like to do
    #from there we go to the loop-de-loop below where the functions will be recalled
    if(shape=="rectangle" or "rec" or "r"):
        try: rec()
        except ValueError: 
            print("You must enter a number: ")
            rec()
    elif(shape=="triangle" or "tri" or "t"):
        try: tri()
        except ValueError:
            print("You must enter a number: ")
            tri()
    elif(shape=="circle" or "circ" or "c" or "cir"):
        try: circ()
        except ValueError:
            print("You must enter a number: ")
            circ()
    else:
        print("Please input rectangle, triangle, or circle: ")
        continue
        # ^ for when the user slips and hits the wrong key of course
    cont=input("Would you like to continue (Y/N)?")
    cont=cont.lower()
    #woah maybe this is a rollercoaster
    #another loop!
    if (cont)!=str:
       print("You must enter Y to continue or N to end program: ")
        #this print line feels a little sassy but hey the mood fits somehow
        cont=input("Would you like to continue (Y/N)?")
    cont=cont.lower()
    break 
cont=cont.lower()
print("Thanks for using me!") 


#"When you see a good person, think of becoming like her or him. When you see someone not so
#good, reflect on your own weak points." -Confucius
