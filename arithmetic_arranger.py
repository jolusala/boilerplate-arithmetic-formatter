'''def arithmetic_arranger(problems):
  listaOperadores = list()
  listaValores = list()
  listaResultados = list()
  validadorOperadores = 0
  validadorValores = 0
  validadorDigitos = 0
  validadorOperaciones = 0

  
  for i in problems:
    listaLimpia = i.split(" ")
    listaOperadores.append(listaLimpia[1])
    listaValores.append([listaLimpia[0], listaLimpia[2]])

 ######################################################################
  if len(problems) < 6: #Valida que no haya mas de 4 operaciones
    validadorOperaciones = len(problems)
  else:
    print("Error: Too many problems.")
   

      
#####################################################################
  for i in listaOperadores:#Valida que los operadores sean + o -
      #print(listaOperadores[i])
      if i == '+' or i == '-':
        validadorOperadores +=1
        #print("Todo bien Operadores")
              
      
      else:
          print("Error: Operator must be '+' or '-'")
          break

######################################################################
      
      
  for i in listaValores: #Valida que los operandos sean menor de 4 digitos
      if len(str(i[0])) <= 4 and len(str(i[1])) <= 4:
        validadorValores +=1
        #print("Todo bien Valores")
        #print(i[0],i[1])

      else:
          print("Error: Numbers cannot be more than four digits.")
          break

#######################################################################
  for i in listaValores:#Valida que los operandos sean numeros
      if i[0].isnumeric() and i[1].isnumeric():
        validadorDigitos +=1
        #print("Todo bien Valores")
        #print(i[0],i[1])

      else:
          print("Error: Numbers must only contain digits.")
          break
        
#########################################################################
  for i in range(len(listaValores)):#Realiza las operaciones aritmeticas
    if listaOperadores[i] == "+":
      listaResultados.append(int(listaValores[i][0])+int(listaValores[i][1]))
      
    elif listaOperadores[i] == "-":
      listaResultados.append(int(listaValores[i][0])-int(listaValores[i][1]))

  


  

  print(validadorOperadores)
  print(validadorValores)
  print(validadorDigitos)
  print(validadorOperaciones)
  print(listaResultados)'''

def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operand = []
    second_operand = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first_operand.append(pieces[0])
        operator.append(pieces[1])
        second_operand.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_line.append(" "*2 + first_operand[i])
        else:
            first_line.append(" "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_line.append(operator[i] + " " + second_operand[i])
        else:
            second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

    for i in range(len(first_operand)):
        third_line.append("-"*(max(len(first_operand[i]), len(second_operand[i])) + 2))

    if answer:
        for i in range(len(first_operand)):
            if operator[i] == "+":
                ans = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                ans = str(int(first_operand[i]) - int(second_operand[i]))

            if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems