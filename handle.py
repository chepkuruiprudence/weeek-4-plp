try:
    with open("calculator.py", "r") as file:
        content = file.read() 
        print(content)
except FileNotFoundError:
    print("Error: The file 'calculator.py' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

#write tpo another file
    with open("calculatorII.py", "w") as outfile:
        outfile.write(content)
        print("\nContent successfully written to 'calculatorII.py'.")

except FileNotFoundError:
    print(
        "Error: The file 'calculator.py' does not exist. Please make sure the file is in the same directory as this script."
    )
except Exception as e:
    print(f"An error occurred: {e}")
