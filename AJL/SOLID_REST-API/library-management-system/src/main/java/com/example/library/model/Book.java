package com.example.library.model;

/**
 * Represents a Book entity in the library.
 * SRP: This class only holds book data.
 */
public class Book {

    private Long id;
    private String title;
    private String author;
    private boolean available;

    public Book(Long id, String title, String author, boolean available) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.available = available;
    }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isAvailable() { return available; }

    public void setAvailable(boolean available) {
        this.available = available;
    }
}
