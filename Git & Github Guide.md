## Using Git and GitHub on a Mac

Git and GitHub are tools that help you keep track of changes in your code and collaborate with others. Here's a step-by-step guide to using Git and GitHub on your Mac:

### Step 1: Install Git

1. Open the "Terminal" application on your Mac. You can find it in the "Utilities" folder within the "Applications" folder.
2. In the Terminal, type `git --version` and press Enter to check if Git is already installed.
3. If Git is not installed, a popup will appear asking if you want to install the Xcode Command Line Tools. Click "Install" and follow the on-screen instructions to complete the installation.

### Step 2: Configure Git

1. In the Terminal, type `git config --global user.name "Your Name"` and press Enter. Replace "Your Name" with your actual name (e.g., John Doe).
2. Type `git config --global user.email "your.email@example.com"` and press Enter. Replace "your.email@example.com" with your email address.

### Cloning a Repository

If you want to work on an existing Git repository that is hosted on GitHub, you can easily clone it to your Mac. Here's how:

1. Go to the repository's page on GitHub.
2. Click on the "Code" button, and you will see a URL for cloning the repository.
3. In the Terminal, navigate to the directory where you want to clone the repository. For example, if you want to clone it into your "Documents" folder, use the command `cd ~/Documents`.
4. Type `git clone <repository-url>` and press Enter. Replace `<repository-url>` with the URL you copied from GitHub.
5. ```git clone https://github.com/JaySandoz/ProductDescriptions.git```
6. Git will start cloning the repository, including all its files and commit history. Once it's done, you will have a local copy of the repository on your Mac/PC.

Cloning a repository creates a local copy of the code on your machine, allowing you to work on it and make changes without affecting the original repository.

### Making Changes and Committing

1. Start working on your project, creating or modifying files as needed.
2. Whenever you make changes and want to save them, go to the Terminal.
3. Use the `cd` command to navigate to the cloned repository's directory.
4. Type `git status` and press Enter to see the list of changes you've made.
5. Use `git add .` to stage all the changes or `git add <file-name>` to stage specific files.
6. Type `git commit -m "Commit message"` and press Enter. Replace "Commit message" with a descriptive message summarizing your changes.

### Pushing Changes to GitHub

1. If you want to share your changes with others or back them up on GitHub, you need to push them.
2. In the Terminal, type `git push origin main` and press Enter. This sends your local commits to the GitHub repository.
3. Enter your GitHub username and password when prompted.

### Collaborating with Others

1. Share the repository URL with others to collaborate on the project.
2. Others can clone the repository, make changes, and push their changes back to GitHub.

That's it! You're now using Git and GitHub on your Mac to track changes and collaborate with others on your coding projects. Remember to regularly commit and push your changes to keep your work safe and share your progress with others.

For more advanced Git commands and features, check out the official Git documentation: [https://git-scm.com/doc](https://git-scm.com/doc)
