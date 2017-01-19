#Defines function fizzbuzz
def fizzbuzz(b):
	
    result = []
    
    for x in range(1, b+1):
    	#If x is divisible by 3 and 5
        if x % 3 == 0 and x % 5 == 0:
            result.append("fizz buzz")
            #checks if its dvisible by 3 only
        elif x % 3 == 0:

            result.append('fizz')
            #Checks if x is divisible by 5 
        elif x % 5 == 0:
            result.append('buzz')
        else:
        	#Otherwise returns the value of x
            result.append(str(x))
    return result

def main():
    print(', '.join(fizzbuzz(20)))

main()