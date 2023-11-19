# Defining The Function 'Swapping Files'
def swappingFile():
  #----------------------------STORING THE FILES NAMES FOR FOR SWAPPING ---------------------------------------------------------  
    from_file = input("You want which file to get changed ?")
    with_file = input("You want which file to get changed with ?")

#----------------------------Code to read the data of both files-------------------------------------------------------------
    with open(from_file,'r') as a:
        data_a = a.read()
    with open(with_file,'r') as b:
        data_b = b.read()
#---------------------------------------End----------------------------------------------------------------------
#--------------------------------Code to swapp the data of both file--------------------------------------------------------

    with open(from_file,'w') as a:
         a.write(data_b)
    with open(with_file,'w') as b:
          b.write(data_a)
#------------------------------------------End-----------------------------------------------------------------

# Calling The Function
swappingFile()