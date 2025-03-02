class Library:
    def __init__(self, list):
        self.books = list
        self.no_books = len(list)

    def disp_books(self):
        print("\n📚 Available Books:")
        for book in self.books:
            print("📖", book)

    def add_book(self, book):
        self.books.append(book)
        self.no_books += 1
        print("\n✅ 📘 Book Added Successfully!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.no_books -= 1
            print(f"\n📕 {book} Book Issued Successfully ✅")
        else:
            print("\n❌ Book Not Available!")

    def return_book(self, book):
        self.books.append(book)
        self.no_books += 1
        print(f"\n🔄 {book} Book Returned Successfully ✅")

    def no_of_books(self):
        return self.no_books


if __name__ == "__main__":
    lib = Library(["Python", "Java", "C", "C++", "SQL", "HTML", "CSS", "JavaScript", "React", "Angular"])

while True:
    print("\n📌 MENU:")
    print("1️⃣  DISPLAY BOOKS 📚")
    print("2️⃣  ADD BOOK ➕")
    print("3️⃣  NO OF BOOKS 🔢")
    print("4️⃣  ISSUE BOOK 📕")
    print("5️⃣  RETURN BOOK 🔄")
    print("6️⃣  EXIT 🚪")

    ch = int(input("\n➡️ Enter Your Choice: "))

    if ch == 1:
        lib.disp_books()
    elif ch == 2:
        book = input("✍️ Enter the name of the book you want to add: ")
        lib.add_book(book)
    elif ch == 3:
        print("\n📊 No. of Books Available: ", lib.no_of_books())
    elif ch == 4:
        book = input("📤 Enter the name of the book you want to issue: ")
        lib.issue_book(book)
    elif ch == 5:
        book = input("📥 Enter the name of the book you want to return: ")
        lib.return_book(book)
    elif ch == 6:
        print("\n🙏 Thank You for Using Our Library! 😊")
        print("\n🔁 Visit Again! 📚")
        break
    else:
        print("\n⚠️ Invalid Choice! Please Try Again.")
        input("\n🔄 Press Enter to Continue")
