package com.example.library.service;

import com.example.library.model.Book;
import java.util.List;

/**
 * Business logic abstraction.
 */
public interface BookService {

    List<Book> getAllBooks();
    Book getBookById(Long id);
    void addBook(Book book);
}
