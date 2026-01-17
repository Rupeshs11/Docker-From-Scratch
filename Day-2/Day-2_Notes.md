# Day 02 – File Creation, Deletion & Editing in Linux

## 📌 Overview
In Linux, files and directories are created, deleted, copied, moved,
and edited using simple terminal commands. These operations are
performed daily while working on Linux systems.

Understanding these commands is essential for managing files efficiently.

---

## 📄 File Creation

### 🔹 touch
Used to create an empty file.

```bash
touch file_name
📝 Note:
If the file already exists, this command updates its timestamp.

📁 Directory Creation
🔹 mkdir
Used to create a new directory.

bash
Copy code
mkdir directory_name
📝 Note:
Directories help organize files in a structured way.

❌ File Deletion
🔹 rm
Used to delete a file.

bash
Copy code
rm file_name
📝 Note:
Deleted files are not moved to trash; they are permanently removed.

❌ Directory Deletion
🔹 rmdir
Used to delete an empty directory.

bash
Copy code
rmdir directory_name
📝 Note:
The directory must be empty before deletion.

📋 Copy Files
🔹 cp
Used to copy files from one location to another.

bash
Copy code
cp source_file destination_file
📝 Note:
The original file remains unchanged after copying.

🔀 Move / Rename Files
🔹 mv
Used to move or rename files.

bash
Copy code
mv old_name new_name
📝 Note:
This command is used for both moving and renaming files.

✏️ File Editing
🔹 vi
Used to edit files using the vi editor.

bash
Copy code
vi file_name
📝 Note:
vi is a powerful editor commonly available on all Linux systems.

🔹 nano
Used to edit files using the nano editor.

bash
Copy code
nano file_name
📝 Note:
nano is beginner-friendly and easy to use.