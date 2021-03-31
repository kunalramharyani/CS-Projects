def arithmetic_arranger(problems, showanswerLine = False):
  
  #Checking the number of problems
  if len(problems)>5:
    return "Error: Too many problems."
  else:
    #Creating strings for formatting
    firstLine = ""
    secondLine = ""
    dashedLine = ""
    answerLine = ""

    #Creating the lists to store the arranged problems, digits and accepted operands
    arranged_problems = list()
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    accepted_operands = ["+", "-"]


    #Looping through the problems object
    for index, problem in enumerate(problems):
      split_problem = problem.split()
      firstnum = split_problem[0]
      operand = split_problem[1]
      secondnum = split_problem[2]
      
      #Checking if the operand is + or -
      if operand not in accepted_operands:
        return "Error: Operator must be '+' or '-'." 
      else:
        #Checking for valid digits
        for digit in firstnum:
          if digit not in digits:
            return "Error:  Numbers must only contain digits." 
          else: 
            continue

        for digit in secondnum:
          if digit not in digits:
            return "Error: Numbers must only contain digits." 
          else: 
            continue
        #Checking the number of digits in each number
        if len(firstnum)>4 or len(secondnum)>4:
          return "Error: Numbers cannot be more than four digits."
        else: 

            if operand == '+':
              answer = int(firstnum) + int(secondnum)
            elif operand == '-': 
              answer = int(firstnum) - int(secondnum)
            else:
              return "Unknown Error"
            #Formatting each line
            width = max(len(firstnum),len(secondnum)) + 2
            firstLine += str(firstnum.rjust(width))
            secondLine +=  str(operand + secondnum.rjust(width-1)) 
            dashedLine += str("-" * width)
            answerLine += str(answer).rjust(width)

            if index < len(problems)-1:
              firstLine += "    "
              secondLine += "    "
              dashedLine += "    "
              answerLine += "    "
            
            if showanswerLine == True: 
              arranged_problems = (firstLine + "\n" + secondLine + "\n" + dashedLine + "\n" + answerLine)
            else: 
              arranged_problems = (firstLine + "\n" + secondLine + "\n" + dashedLine)


    return arranged_problems