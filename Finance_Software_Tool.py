from syslog import LOG_LOCAL0
import numpy as np
import tkinter

# Calculate what needs to go to each account - 

#Breakdown by fixed sums
gross_income = input()

#Calculate monthly outgoings (commitments)
commitments = input()
commitment2 = input()
commitment3 = input()
after_commitments = gross_income-commitments

### Breakdown by Percentage ###
living = after_commitments*0.5
emergency = after_commitments*0.05
fun = after_commitments*0.25
float = after_commitments*0.2

emergency_and_fun = emergency+fun

print('#################### FINANCES #################### \n \n \n Living:           ' + str(living) + '\n Emergency Fund:    ' + str(emergency) + '\n Fun:              ' 
    + str(fun) + '\n Float:            ' + str(float) + '\n \n To each account \n \n' + ' Monzo:            ' + str(emergency_and_fun) + '\n Santander:        ' + str(living) + 
    '\n \n \n #################################################')
