# Project Requirements: Todo List Website

## 1. Project Overview & Problem Statement
**Overview:** A web-based task management application built with Flask, SQLAlchemy, and Bootstrap that allows users to create, organize, update, and track daily tasks.  
**Problem Statement:** Individuals often struggle to organize daily responsibilities, remember important tasks, and monitor progress across scattered notes or mental checklists.

## 2. Target Users & Scalability
* **Current Scope (Phase 1):** Single-user local or personal web application.
* **Future Scope (Phase 2):** Designed with clean separation of concerns so user authentication and multi-user data isolation can be added later.

## 3. Functional Requirements

### MVP Scope (Phase 1)
* **Create:** Users can add a new task with a title and optional description.
* **Read:** Users can view a dashboard listing all active and completed tasks, as well as view individual task details.
* **Update:** Users can edit the title and description of an existing task.
* **Complete:** Users can toggle a task's status between incomplete and completed.
* **Delete:** Users can permanently remove a task via a secure confirmation action.

### Post-MVP Enhancements (Phase 2)
* **Organization:** Assign priority levels (Low, Medium, High) and custom categories/tags to tasks.
* **Discovery:** Filter tasks by completion status or priority, and search tasks by keyword.
* **Scheduling:** Set and track task due dates.
* **Authentication:** User registration, login, and private per-user task lists.

## 4. Data Validation Rules
* **Task Title:** Required field; cannot be empty or whitespace-only; maximum length of 120 characters.
* **Task Description:** Optional field; supports longer multi-line text.
* **Completion Status:** Boolean flag; defaults to `False` (incomplete) upon creation.
* **Timestamps:** Automatically records creation date and time (`UTC`).

## 5. Non-Functional Requirements
* **Security:** All state-changing forms (Create, Update, Delete, Toggle) must use CSRF protection, and sensitive configuration keys must be stored in environment variables (`.env`).
* **Usability & Responsiveness:** The UI must use Bootstrap 5 grid and components to render cleanly on both mobile (375px) and desktop viewports.
* **Maintainability:** Follow PEP 8 naming conventions and separate database models, forms, routes, and HTML templates into distinct modules.
* **Reliability:** Handle invalid task IDs gracefully with custom HTTP 404 error responses rather than application crashes.
