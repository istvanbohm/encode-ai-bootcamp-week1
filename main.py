import sys
import subprocess

def main():
    print("Choose your chef:")
    print("(1) Passionate Mexican")
    print("(2) Focused French")
    print("(3) Hungry Hungarian")
    print("(4) Crazy Argentinian")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    script_map = {
        '1': 'MexicanChefGPT.py',
        '2': 'FrenchChefGPT.py',
        '3': 'HungarianChefGPT.py',
        '4': 'ArgentinianChefGPT.py', 
    }

    if choice in script_map:
        script_name = script_map[choice]
        try:
            subprocess.run(['python', script_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script_name}: {e}")
    else:
        print("Error: Invalid choice.")
        sys.exit(1)

if __name__ == "__main__":
    main()
