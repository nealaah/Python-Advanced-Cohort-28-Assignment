from datetime import datetime
class DuplicateVisitorError(Exception):
    def __init__(self, visitor):
        self.message= f"Visitor '{visitor} already signed in, no back visits allowed"
        super().__init__(self.message)


def main():
   filename ="Visitors.txt"
   try:
        with open(filename, "r", encoding="utf-8") as f:
            pass
   except FileNotFoundError:
        with open(filename, "r", encoding="utf-8") as f:
            pass
   
   visitor = input(f"Enter your name:")
   timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

   try:
        last_visitor = None
        with open(filename, "r", encoding="utf-8") as f:
            content=f.readlines()
            if content:
                last_line= content[-1]
                last_name = last_line.split("-")[0] if content else None

        if visitor == last_visitor:
            raise DuplicateVisitorError("Already signed in")
        
        with open (filename, "a")as f:
            f.write(f"{visitor}- {timestamp}\n")

        print("Logged in successfully")


   except DuplicateVisitorError as e:
    print("Error:", e)

if __name__ == "__main__":
    main()
