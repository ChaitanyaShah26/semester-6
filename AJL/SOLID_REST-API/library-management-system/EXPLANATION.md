## Library Management System – Spring Boot REST API (SOLID Principles)

---

## 1. Project Overview

This project is a **Library Management System** implemented as a **REST API using Spring Boot**.
The main objective of this project is **not complexity**, but **clean architecture** and **proper use of SOLID principles**.

The system allows:

- Adding books
- Fetching all books
- Fetching a book by ID

The application uses **in-memory storage**, meaning **no database is required**, making it simple and easy to understand.

---

## 2. High-Level Architecture

The project follows a **layered architecture**:

```
Controller → Service → Repository → Model
```

Each layer has a **clear responsibility**, which is the foundation of SOLID principles.

---

## 3. Package Structure Explanation

```
com.example.library
│
├── controller
├── service
├── repository
├── model
├── exception
├── config
└── LibraryManagementApplication.java
```

Each package exists for a **single, well-defined purpose**.

---

## 4. File-by-File Explanation with SOLID Principles

---

## 4.1 LibraryManagementApplication.java

### Purpose

This is the **entry point** of the Spring Boot application.

### Key Responsibilities

- Bootstraps the Spring context
- Starts the embedded server (Tomcat)

### Code Concept

- Uses `@SpringBootApplication` to enable:
  - Auto-configuration
  - Component scanning
  - Configuration support

### SOLID Principle Used

✅ **Single Responsibility Principle (SRP)**
This class is only responsible for **starting the application**, nothing else.

---

## 4.2 Book.java (Model Layer)

### Purpose

Represents a **Book entity** in the library.

### What it Contains

- Book ID
- Title
- Author
- Availability status

### What it Does NOT Do

- No business logic
- No database logic
- No API logic

### SOLID Principle Used

✅ **Single Responsibility Principle (SRP)**
The class only represents **data**, making it easy to maintain and reuse.

---

## 4.3 BookRepository.java (Repository Interface)

### Purpose

Defines **data access operations** for books.

### Why an Interface?

- To avoid tight coupling
- To allow easy replacement of implementation later (e.g., database)

### Methods Defined

- `findAll()`
- `findById(Long id)`
- `save(Book book)`

### SOLID Principles Used

✅ **Dependency Inversion Principle (DIP)**
Higher-level modules depend on **abstractions**, not concrete classes.

✅ **Interface Segregation Principle (ISP)**
The interface contains **only required methods**, no unnecessary operations.

---

## 4.4 BookRepositoryImpl.java (Repository Implementation)

### Purpose

Provides an **in-memory implementation** of `BookRepository`.

### How Data Is Stored

- Uses `ArrayList<Book>` as temporary storage
- No database or external dependency

### Benefits

- Simple
- Easy to test
- Can be replaced with JPA later

### SOLID Principles Used

✅ **Open/Closed Principle (OCP)**
The system is open for extension (database repository) but closed for modification.

✅ **Liskov Substitution Principle (LSP)**
`BookRepositoryImpl` can replace `BookRepository` anywhere without breaking behavior.

---

## 4.5 BookService.java (Service Interface)

### Purpose

Defines **business logic operations** related to books.

### Why This Layer Exists

- Separates business logic from controllers
- Keeps controllers thin and clean

### SOLID Principles Used

✅ **Dependency Inversion Principle (DIP)**
Controllers depend on this interface, not implementation.

✅ **Interface Segregation Principle (ISP)**
Only relevant business methods are exposed.

---

## 4.6 BookServiceImpl.java (Service Implementation)

### Purpose

Implements the **actual business logic**.

### Responsibilities

- Fetch all books
- Fetch book by ID
- Add new books
- Handle missing book scenarios

### Important Design Choice

- Uses **constructor injection**
- Depends on `BookRepository` interface, not concrete class

### SOLID Principles Used

✅ **Single Responsibility Principle (SRP)**
Handles only business rules.

✅ **Dependency Inversion Principle (DIP)**
Depends on abstractions.

✅ **Liskov Substitution Principle (LSP)**
Can be substituted wherever `BookService` is used.

---

## 4.7 BookController.java (Controller Layer)

### Purpose

Exposes REST API endpoints.

### Endpoints

- `GET /api/books`
- `GET /api/books/{id}`
- `POST /api/books`

### What the Controller Does

- Accepts HTTP requests
- Sends HTTP responses
- Delegates logic to Service layer

### What It Does NOT Do

- No business logic
- No data storage logic

### SOLID Principles Used

✅ **Single Responsibility Principle (SRP)**
Only handles HTTP request–response cycle.

✅ **Dependency Inversion Principle (DIP)**
Uses `BookService` interface instead of implementation.

---

## 4.8 BookNotFoundException.java

### Purpose

Handles scenarios where a requested book does not exist.

### Why a Custom Exception?

- Clean error handling
- Improves readability
- Avoids cluttering service logic

### SOLID Principle Used

✅ **Single Responsibility Principle (SRP)**
Dedicated class for error representation.

---

## 4.9 SwaggerConfig.java

### Purpose

Configures **Swagger / OpenAPI documentation**.

### What It Provides

- API title
- Description
- Versioning
- Interactive UI

### Why Separate Config?

- Keeps documentation separate from logic
- Easy to extend later

### SOLID Principles Used

✅ **Single Responsibility Principle (SRP)**
Only responsible for API documentation.

✅ **Open/Closed Principle (OCP)**
Swagger config can be extended without touching controllers.

---

## 5. SOLID Principles Summary Table

| Principle | Where Used                           | How                                                |
| --------- | ------------------------------------ | -------------------------------------------------- |
| SRP       | All layers                           | Each class has only one responsibility             |
| OCP       | Repository, SwaggerConfig            | New behavior added without modifying existing code |
| LSP       | Service & Repository implementations | Interfaces can be safely replaced                  |
| ISP       | Service & Repository interfaces      | Small, focused interfaces                          |
| DIP       | Controller & Service                 | Depend on abstractions, not concrete classes       |

##
