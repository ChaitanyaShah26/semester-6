# Library Management System – Spring Boot REST API

## Description

This project is a simple Library Management System built using Spring Boot.
It demonstrates REST API development while strictly following SOLID principles.
The project uses in-memory storage and does not require any database.

---

## Features

- Add books
- View all books
- View book by ID
- Clean layered architecture
- No database dependency

---

## SOLID Principles Used

### 1. Single Responsibility Principle (SRP)

Each class has only one responsibility:

- Controller → handles HTTP requests
- Service → business logic
- Repository → data storage
- Model → data representation

### 2. Open/Closed Principle (OCP)

The system is open for extension but closed for modification.
Repository implementation can be changed without affecting services.

### 3. Liskov Substitution Principle (LSP)

Service implementations can replace service interfaces without breaking functionality.

### 4. Interface Segregation Principle (ISP)

Small, focused interfaces are used instead of large ones.

### 5. Dependency Inversion Principle (DIP)

High-level modules depend on abstractions, not concrete implementations.

---

## How to Run

1. Import project in IDE
2. Run LibraryManagementApplication.java
3. Access API on http://localhost:8080

---

## Technologies Used

- Java
- Spring Boot
- REST API
- Maven

---

## Swagger API Documentation

Swagger UI is integrated using Springdoc OpenAPI.

### Access Swagger UI

http://localhost:8080/swagger-ui.html

### Benefits

- Interactive API documentation
- Easy testing of REST endpoints
- Clear request and response visualization

Swagger configuration follows SOLID principles:

- Separate configuration class
- No business logic mixed with documentation
