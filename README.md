# 🧠 Legal Assistance Platform – Project Documentation

## 📌 ERD Diagram (Entities & Relationships)
![ERD](<Screenshot 2025-04-30 115621.png>)
**Entities:**
- `User` → has one `Profile`
- `Profile` → has many `Cases`
- `Case` → has many `Messages`

**Relationships:**
- One-to-One: `User` ↔ `Profile`
- One-to-Many: `Profile` → `Case`
- One-to-Many: `Case` → `Message`

---

## 🔄 RESTful Routing Tables

### 1. 🧑 User

| Action     | HTTP Method | Route           | Description             |
|------------|-------------|------------------|-------------------------|
| Create     | POST        | `/users/signup`  | Create a new user       |
| Read (all) | GET         | `/users/login`   | Log in a user           |
| Read (one) | GET         | `/users/refresh` | Refresh user token      |

---

### 2. 👤 Profile *(belongs to User)*

| Action  | HTTP Method | Route                      | Description           |
|---------|-------------|-----------------------------|-----------------------|
| Create  | POST        | `/users/:user_id/profile`   | Create a profile      |
| Read    | GET         | `/users/:user_id/profile`   | View a user's profile |
| Update  | PUT/PATCH   | `/users/:user_id/profile`   | Update the profile    |
| Delete  | DELETE      | `/users/:user_id/profile`   | Delete the profile    |

---

### 3. 📁 Case *(belongs to Profile)*

| Action     | HTTP Method | Route                          | Description             |
|------------|-------------|----------------------------------|-------------------------|
| Create     | POST        | `/profiles/:profile_id/cases`   | Create a new case       |
| Read (all) | GET         | `/profiles/:profile_id/cases`   | List all profile cases  |
| Read (one) | GET         | `/cases/:id`                    | View a specific case    |
| Update     | PUT/PATCH   | `/cases/:id`                    | Update a case           |
| Delete     | DELETE      | `/cases/:id`                    | Delete a case           |

---

### 4. 💬 Message *(belongs to Case)*

| Action     | HTTP Method | Route                          | Description               |
|------------|-------------|----------------------------------|---------------------------|
| Create     | POST        | `/cases/:case_id/messages`      | Add a message to a case   |
| Read (all) | GET         | `/cases/:case_id/messages`      | List all messages in case |
| Read (one) | GET         | `/messages/:id`                 | View a specific message   |
| Update     | PUT/PATCH   | `/messages/:id`                 | Update a message          |
| Delete     | DELETE      | `/messages/:id`                 | Delete a message          |

---

## ✅ User Stories

- As a new user, I want to register with email and password so I can log in later.
- As a user, I want to create a profile to be recognized as a lawyer or a client.
- As a client, I want to create a legal case and assign it to a lawyer.
- As a lawyer, I want to view the list of cases assigned to me.
- As a client/lawyer, I want to send and receive messages inside each case.
- As a user, I want to reset my password if I forget it.

---