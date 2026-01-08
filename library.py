def library_book_details(book_id, title, author, year):
    return (
        f"Book Id : {book_id}\n"
        f"Title : {title}\n"
        f"Author : {author}\n"
        f"Year : {year}\n"
    )

if __name__ == "__main__":
    book_id = input("101")
    title = input("python Programming")
    author = input("Jhon")
    year = input(2020)

    print(library_book_details(101,"Python Programming","Jhon", 2020))
