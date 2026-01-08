def library_book_details(book_id, title, author, year):
    return (
        f"Book Id : {book_id}\n"
        f"Title : {title}\n"
        f"Author : {author}\n"
        f"Year : {year}\n"
    )

if __name__ == "__main__":
    print(library_book_details(101, "Python Programming", "Jhon", 2020))
