try: #Normal execution
    myList = [1, 2, 3, 4, 5]
    print(myList[2])
    print(myList[10]) #IndexError

    myDict = {'a':1, 'b':2, 'c':3, 'd':4}
    print(myDict['e']) #KeyError

except IndexError:
    print("IndexError occurred")

except KeyError:
    print("KeyError occurred")

except: #Any exceptions
    print("Error occured")

finally: #Optional 
    print("Execution completed")