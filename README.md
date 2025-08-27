# Movie Recommendation and Review API

To challenge your FastAPI skills, you can build a **"Movie Recommendation and Review API"**. This project will test your knowledge of advanced features like dependencies, authentication, and database integration. 🎬

***

## Project Statement: Movie Recommendation and Review API

Create an API that allows users to register, log in, and perform actions related to movies. The API should have two main types of users: **standard users** and **admin users**.

### Core Features

* **User Management**:
    * **Registration**: Standard users can register with a unique username, email, and a password.
    * **Authentication**: Implement a secure authentication system (e.g., JWT) to handle user login and protect routes. Users get a token upon successful login.
    * **Authorization**: Create a distinction between standard and admin users.
        * Standard users can view movie details, post reviews, and rate movies.
        * Admin users have full CRUD (Create, Read, Update, Delete) access to movie data.

* **Movie Management**:
    * **Create**: Admins can add new movies to the database. A movie should have attributes like `title`, `director`, `release_year`, `genre`, and a `description`.
    * **Read**:
        * Any user (authenticated or not) can view a list of all movies.
        * Authenticated users can view detailed information for a specific movie, including its average rating and all user reviews.
    * **Update**: Admins can update movie details.
    * **Delete**: Admins can delete movies.

* **Review and Rating System**:
    * **Create**: Authenticated standard users can submit a review and a rating (e.g., on a scale of 1 to 5) for a movie. A user can only submit one review per movie.
    * **Read**: When viewing a specific movie, all associated reviews should be visible.
    * **Update**: Users can update their own reviews and ratings.
    * **Delete**: Users can delete their own reviews.

* **Recommendation Engine**:
    * Implement a simple recommendation endpoint. When a user requests recommendations, the API should return a list of movies based on their highest-rated genres. For example, if a user has rated sci-fi movies highly, the API should recommend other sci-fi movies they haven't seen.

***

### Technical Requirements

* **Framework**: FastAPI
* **Database**: Use a database to store movie, user, and review data. **SQLAlchemy with an ORM** (Object-Relational Mapper) like `SQLModel` or `Alembic` is a great choice for this.
* **Authentication**: Implement **JWT (JSON Web Tokens)** for user authentication and authorization.
* **Dependencies**: Make extensive use of FastAPI's dependency injection system for managing database sessions and handling authentication checks.
* **Validation**: Use `Pydantic` models for request body validation and response serialization.
* **Testing**: Write unit tests for your API endpoints. This is a crucial step for an expert-level project. Use `pytest` for this.

This project goes beyond basic CRUD operations by integrating authentication, authorization, and a simple recommendation logic, showcasing a well-rounded understanding of FastAPI's capabilities.