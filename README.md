# Bankers Visualiser

A very simple Python script that I wrote for visualising the Banker's Algorithm for ENCE360
(Operating Systems) at the University of Canterbury

## Usage
To run:
'''console
user@linux~$ python3 main.py
'''

Then enter the number of total resources available with spaces between each integer:
'''console
+-----------------------------+
Enter available resources: A B C D E
'''

Then enter the resources used by each of the processes:
'''console
+-----------------------------+
 
Enter Process Requirements: 1A 1B 1C 1D 1E
 
Enter Current Allocations: 0 0 0 0 0
 
+-----------------------------+
'''

Do repeat this until all processes have current resources and resources required to complete then
continue. To continue leave the final entry blank.

To run the visualiser enter the process you wish to complete until all process require no
resources to complete
'''console
+-----------------------------+
 
Available
[ A B C D E ]
 
+-----------------------------+
 
Required to Complete: 
 
P0 [ 0 0 0 0 0 ]
P1 [ 0 0 0 0 0 ]
 
+-----------------------------+
 
Currently Used
P0 [ 0 0 0 0 0 ]
P1 [ 0 0 0 0 0 ]
 
+-----------------------------+
 
What Process to complete? 

'''

## Author
Jos Craw (2019)


