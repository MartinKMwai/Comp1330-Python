def part_one(n1, n2, n3):

  results = []

  a= [n1, n1, n2, n2, n3, n3]
  b= [n2, n3, n1, n3, n2, n1]
  c= [n3, n2, n3, n1, n1, n2]

  for m in range (len(a)):
    num1 = a[m]
    num2 = b[m]
    num3 = c[m]
   
                            
                                                                  
                                                                   #PART 1
        #divide
        # Division, division
    div1 = float((num1 / num2) / num3)
    results.append(div1)
    # division, addition
    div2 = float((num1 / num2) + num3)
    results.append(div2)
    # division, multiplication
    div3 = float((num1 / num2) * num3)
    results.append(div3)
    #division, subtraction
    div4 = float((num1 / num2) - num3)
    results.append(div4)

          #add
    #add, subtract
    add1 = float((num1 + num2) - num3)
    results.append(add1)
    # add, multiply
    add2 = float((num1 + num2) * num3)
    results.append(add2)
    # add, divide
    add3 = float((num1 + num2) / num3)
    results.append(add3)
    # add, add
    add4 = float((num1 + num2) + num3)
    results.append(add4)

        #multipy
    #multiply, add
    mult1 = float((num1 * num2) + num3)
    results.append(mult1)
    #multiply, divide
    mult2 = float((num1 * num2) / num3)
    results.append(mult2)
    #multiply, subtract
    mult3 = float((num1 * num2) - num3)
    results.append(mult3)
    #multiply, multiply
    mult4 = float((num1 * num2) * num3)
    results.append(mult4)


      #subtract 
  # subtract, add
    sub1 = float((num1 - num2) + num3)
    results.append(sub1)
  # subtact, subtract
    sub2 = float((num1 - num2) - num3)
    results.append(sub2)
  # subtact, multiply
    sub3 = float((num1 - num2) * num3)
    results.append(sub3)
  # subtract, divide
    sub4 = float((num1 - num2) / num3)
    results.append(sub4)

                                                                    #PART 2
                        #num 1, 2, 3
          #divide
    # Division, division
    if num2 / num3 != 0:
        div1a = float(num1 / (num2 / num3))
        results.append(div1a)
    # division, addition
    if num2 + num3 != 0:
        div2a = float(num1 / (num2 + num3))
        results.append(div2a)
    # division, multiplication
    if num2 * num3 != 0:
        div3a = float(num1 / (num2 * num3))
        results.append(div3a)
    #division, subtraction
    if num2 - num3 != 0:
        div4a = float(num1 / (num2 - num3))
        results.append(div4a)

          #add
    #add, subtract
    add1a = float(num1 + (num2 - num3))
    results.append(add1a)
    # add, multiply
    add2a = float(num1 + (num2 * num3))
    results.append(add2a)
    # add, divide
    if num2 / num3 != 0:
        add3a = float(num1 + (num2 / num3))
        results.append(add3a)
    # add, add
    add4a = float(num1 + (num2 + num3))
    results.append(add4a)

        #multipy
    #multiply, add
    mult1a = float(num1 * (num2 + num3))
    results.append(mult1a)
    #multiply, divide
    if num2 / num3 != 0:
        mult2a = float(num1 * (num2 / num3))
        results.append(mult2a)
    #multiply, subtract
    mult3a = float(num1 * (num2 - num3))
    results.append(mult3a)
    #multiply, multiply
    mult4a = float(num1 * (num2 * num3))
    results.append(mult4a)


      #subtract 
  # subtract, add
    sub1a = float(num1 - (num2 + num3))
    results.append(sub1a)
  # subtact, subtract
    sub2a = float(num1 - (num2 - num3))
    results.append(sub2a)
  # subtact, multiply
    sub3a = float(num1 - (num2 * num3))
    results.append(sub3a)
  # subtract, divide
    if num2 / num3 != 0:
        sub4a = float(num1 - (num2 / num3))
        results.append(sub4a)

                                                                                                     
  res_initial = []
  for t in results:
    res_initial.append(t)
  
  results.sort(reverse=True)

  
  b_ind = 0
  for i in range(len(results)):
    if results[i] < 1:
      if b_ind == 0:
        b_ind = i 

  results = results[:b_ind - 1]
  fin_results = []
  for x in range(len(results)):
    if results[x] % 1 == 0 and results[x] != 0 and results[x] not in fin_results:
      fin_results.append(results[x])

  
  fin_results.reverse()
  return fin_results







def part_three():
  card = []

  for c in range(5):
    r = input("")
    r = r.split(" ")
    card.append(r)

  n_throws = int(input(""))

  throws = []
  for throw in range(n_throws):
    t = input("")
    t = t.split(" ")
    throws.append(t)

  for q in throws:
    n1 = q[0]
    n2 = q[1]
    n3 = q[2]

    res = part_one(int(n1), int(n2), int(n3))
    for k in res:
      for g in range(len(card)):
        for y in range(len(card[g])):
          if card[g][y] != "x":
            if int(k) == int(card[g][y]):
              card[g][y] = "x"

  for v in card:
    print(" ".join(str(u) for u in v))

part_three()
