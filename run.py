import bb
import os

def start_app():
    try:
        # Clear terminal screen
        os.system('clear')
        
        # Calling the main function from your .so file
        # Make sure your bb.py had a main() function before compiling
        bb.main()
        
    except AttributeError:
        print("\033[31m[!] Error: Could not find main() function in bb.so\033[0m")
    except Exception as e:
        print(f"\033[31m[!] An error occurred: {e}\033[0m")

if __name__ == "__main__":
    start_app()
    
