# A script written by Aharon Gross
import itertools
import subprocess
import os


def main():
  # Use the itertools library to generate all permutations of the numbers 1-6
  permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6]))
  
  i = 0
  j = 0
  gdb.execute("set pagination off")
  
  print ("Press 1 for the full solution or any other key for a test run")
  print ("Please not that the test run will not let you know if the solution is right or wrong, it is merely for test purposes.")
  inp = raw_input("")

  while (j < 720):
    if os.path.exists("bomb_solutions.txt"): os.remove("bomb_solutions.txt")
    # Convert the permutation tuple to a string
    perm_str = ''.join(str(permutations[j]))
    perm_str = perm_str.replace('(', '')
    perm_str = perm_str.replace(')', '')
    perm_str = perm_str.replace(',', '')
    
    # Write the answeres int the text file
    f = open("bomb_solutions.txt", "a")
    """
    Replace the text "Enter your answers here!" with your 5 previous answers.
    Make sure to put '\n' between each answer and at the end of the text.
    Make sure there are no adiitional spaces.
    Example of a valid input - f.write("I turned the moon into something I call a Death Star.\n0 1 1 2 3 5\n6 942\n4 2\n5 115\n")
    """
    f.write("Enter your answeres here!")
    f.write(perm_str + "\n")
    f.close()
    # Test the bomb with the current permutation
    gdb.execute("file bomb")
    gdb.execute("break explode_bomb")
    gdb.execute("r bomb_solutions.txt")
    # Exit the currnt run
    subprocess.call(["echo", "y | gdb -ex 'kill' -ex 'y'"], shell=True)
    
    # A breakpoint was hit - test the next permutation
    if gdb.breakpoints()[i].hit_count > 0:
      i += 1
      if inp != "1": break
      j += 1
      gdb.execute("return")
      continue
    else:
      # The solution was found!
      print("Solution found:", perm_str)
      print("No need to do anything! Your score was automatically updated and the txt file now holds the right answers to all phases.")
      exit()

main()

