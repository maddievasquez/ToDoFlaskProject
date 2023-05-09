# Flask To-Do App with MongoDB and User Authentication

This Flask application allows users to create and manage to-do items with the help of MongoDB. It also includes a user authentication system using [this tutorial](https://github.com/LukePeters/User-Login-System-Tutorial).

The app allows registered users to create, edit, and delete their to-do items. To use the app, users must first create an account by registering. Once logged in, they can create new to-do items, set a priority level, and assign a due date. Users can also edit or delete their existing to-do items.

## MongoDB

MongoDB is used as the database for the application. The `todos` collection stores all the to-do items created by users. Each to-do item is represented as a document in the collection, with the following fields:

- `content`: a string that describes the to-do item
- `degree`: a string indicating the priority level of the to-do item
- `due_date`: a string representing the due date of the to-do item
- `user_id`: the ID of the user who created the to-do item

## User Authentication

The user authentication system is based on [this tutorial](https://github.com/LukePeters/User-Login-System-Tutorial). It uses MongoDB to store user information such as username and password. Users can register for an account, log in to their account, and log out of their account. Once logged in, users can create, edit, and delete their to-do items.

## Creating a To-Do Item

To create a new to-do item, users must first log in to their account. They can then navigate to the homepage and fill out the form to create a new to-do item. They can specify the content, priority level, and due date of the to-do item. Once submitted, the new to-do item is added to the `todos` collection in MongoDB.

## Editing a To-Do Item

To edit an existing to-do item, users must first log in to their account. They can then navigate to the homepage and click the "Edit" button next to the to-do item they want to edit. They can then update the content, priority level, or due date of the to-do item. Once submitted, the updated to-do item is saved to the `todos` collection in MongoDB.

## Deleting a To-Do Item

To delete an existing to-do item, users must first log in to their account. They can then navigate to the homepage and click the "Delete" button next to the to-do item they want to delete. The to-do item is then removed from the `todos` collection in MongoDB.

## Adding a Due Date

To add a due date to a to-do item, users can fill out the "Due Date" field when creating or editing a to-do item. The due date is stored in the `due_date` field of the to-do item document in MongoDB.

## Conclusion

This Flask application provides a simple way for users to create and manage to-do items with the help of MongoDB. The user authentication system ensures that only registered users can access and manage their to-do items. The app can be easily extended to add more features, such as email reminders for upcoming due dates or a calendar view to visualize to-do items over time.
