
# To_Do_List

This Django project,To_Do_List is a web application designed for managing to-do tasks. The project uses Django 5.0.4 and follows standard project structure and settings.
## Setup and Running 

1. Clone the repository:

```bash
  git clone https://github.com/kamalkushwaha1234/Wobot.ai_assignment
```
2. Go inside the project :
```bash
  cd .\To_Do_List\
```
3. Install required packages:

```bash
pip install -r requirements.txt
```
4. Run migrations to set up your database  :

```bash
  python manage.py migrate
  python manage.py makemigrations
```
5.  Start the development server  :

```bash
  python manage.py runserver
```
## Project Flow

| *Component*   | *Description*                                                                                             | *Connections*                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| *Models*      | *ToDoItem*                                                                                                | Used by views to interact with the database.      |
|                 | - Fields: title, description, created_date, due_date, completed                                             |                                                                                             |
| *Views*       | *Home Views*                                                                                              | Fetch, update, and delete ToDoItem data.          |
|                 | - home(): Display all items                                                                                 | Renders home.html                               |
|                 | - create_todo(): Add new item                                                                               | Redirects to home()                               |
|                 | - complete_todo(): Mark item as completed                                                                   | Redirects to home()                               |
|                 | - delete_todo(): Remove an item                                                                             | Redirects to home()                               |
|                 | *User Views*                                                                                              | Handle user authentication and management.        |
|                 |-/api/token/ :Generate Token                                                                                               |Used the create a token for authentication         
|                 | - login_page(): User login                                                                                  | Redirects to home() on success, uses login.html |
|                 | - register_page(): User Register                                                                                  | Redirects to home() on success, uses register.html |
|                 | - profile_page(): User profile                                                                                  | To see User Profile |
|                 | - logout_page(): User logout                                                                                  | Delete the token from Localstorage and logout
| *Templates*   | *home.html*                                                                                               | Main interface for displaying and managing tasks. |
|                 | - Displays all to-do items                                                                                  | Interacts with all home views functions.          |
|                 | - Includes forms for new tasks and buttons for task completion and deletion                                 |                                                   |
|                 | *login.html*                                                                                              | Used for user login.                              |
|                 | *register.html*                                                                                            | Used for user registration.                       |
|                 | *profile.html*                                                                                            | Displays user profile information.                 |

### Explanation
- *Models*: The ToDoItem model is central to the application, storing all to-do items and related data.
- *Views*: Views are split into two categories, handling either task management(**home views**) or user management (**User views**)functionalities. They interact with the model to process data and then direct the flow to appropriate templates.
- *Templates*: Serve as the frontend, displaying data to the user and capturing user inputs. They are closely linked with views which provide the necessary data and handle form submissions.
- *URL Routing*: It acts as the dispatcher that connects URLs to specific view functions, ensuring the correct handling of user requests based on the URL accessed.


## Screenshots
###Home page
![image](https://github.com/kamalkushwaha1234/Wobot.ai_assignment/assets/131939203/bd700ae7-ef95-4207-acda-b3a112db407f)

### To Create a To-Do-List 
You have to fill the entery 
![image](https://github.com/kamalkushwaha1234/Wobot.ai_assignment/assets/131939203/cbd7dece-c48a-4491-92f9-b17fb12b6203)
### Hence ,To-Do-List created
![image](https://github.com/kamalkushwaha1234/Wobot.ai_assignment/assets/131939203/4f7dd9e1-a06d-447f-8cb2-692178d86ff3)







