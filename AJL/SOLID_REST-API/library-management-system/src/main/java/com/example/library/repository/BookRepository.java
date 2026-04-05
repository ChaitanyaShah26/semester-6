package com.example.library.repository;

import com.example.library.model.Book;
import java.util.List;

/**
 * Repository abstraction.
 * DIP: Higher layers depend on this interface.
 */
public interface BookRepository {

    List<Book> findAll();
    Book findById(Long id);
    void save(Book book);
}
