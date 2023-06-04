## Using Git and GitHub on a Mac

Git and GitHub are tools that help you keep track of changes in your code and collaborate with others. Here's a step-by-step guide to using Git and GitHub on your Mac:

### Step 1: Install Git

1. Open the "Terminal" application on your Mac. You can find it in the "Utilities" folder within the "Applications" folder.
2. In the Terminal, type `git --version` and press Enter to check if Git is already installed.
3. If Git is not installed, a popup will appear asking if you want to install the Xcode Command Line Tools. Click "Install" and follow the on-screen instructions to complete the installation.

### Step 2: Configure Git

1. In the Terminal, type `git config --global user.name "Your Name"` and press Enter. Replace "Your Name" with your actual name (e.g., John Doe).
2. Type `git config --global user.email "your.email@example.com"` and press Enter. Replace "your.email@example.com" with your email address.

### Step 3: Create a New Repository

1. Decide on a name for your project. Let's say it's called "my-project".
2. In the Terminal, type `mkdir my-project` and press Enter. This will create a new directory for your project.
3. Type `cd my-project` and press Enter to navigate into the project directory.
4. Type `git init` and press Enter to initialize a new Git repository.

### Step 4: Make Changes and Commit

1. Start working on your project, creating or modifying files as needed.
2. Whenever you make changes and want to save them, go to the Terminal.
3. Type `git add .` and press Enter. This tells Git to include all the changes you made.
4. Type `git commit -m "Commit message"` and press Enter. Replace "Commit message" with a short description of the changes you made. For example, "Added homepage HTML file".

### Step 5: Connect to GitHub

1. Go to [GitHub.com](https://github.com) and sign in or create a new account.
2. On GitHub, create a new repository by clicking on the "New" button.
3. Choose a name for your repository, such as "my-project", and click "Create repository".
4. Copy the remote repository URL provided by GitHub.
5. In the Terminal, type `git remote add origin <remote-repository-url>` and press Enter. Replace `<remote-repository-url>` with the URL you copied.
6. Finally, type `git push -u origin main` and press Enter. This sends your code from your Mac to GitHub.

### Step 6: Collaborate with Others

1. Share the link to your GitHub repository with others to collaborate.
2. They can clone the repository to their own Macs, make changes, and push them back to GitHub to share with you.

That's it! You're now using Git and GitHub on your Mac to track changes and collaborate with others on your coding projects. Remember to regularly commit and push your changes to keep your work safe and share your progress with others.

If you need more guidance or want to learn advanced Git commands, check out the official Git documentation: [https://git-scm.com/doc](https://git-scm.com/doc)
```
