package com.example.library.exception;

/**
 * Custom exception class.
 * SRP: Handles book-related errors.
 */
public class BookNotFoundException extends RuntimeException {

    public BookNotFoundException(String message) {
        super(message);
    }
}
