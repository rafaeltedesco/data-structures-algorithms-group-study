# Data Structures and Algorithms Study Group

Welcome to the Data Structures and Algorithms Study Group! This repository is designed to help us collaboratively solve challenges from platforms like HackerRank, LeetCode, and CodeSignal.

## Rules

1. Each week, challenges will be assigned, and a branch for that week will be created (e.g., `week-1`, `week-2`).
2. Developers should fork the repository, complete the challenges in their fork, and then open a Pull Request (PR) to the corresponding week branch.
3. You can implement the challenges in any programming language you prefer.
4. Create a folder with your name followed by the programming language you are using (e.g., `adriano_java`).
5. Inside your folder, create subfolders for each challenge. Use the format `challenge-number_challenge-name` (e.g., `01_longest_substring_in_a_string`).
6. Each subfolder should contain your solution file(s) and optionally a `README.md` explaining your approach.

## Big O Notation Guidance

Understanding the efficiency of your algorithm is crucial. Please include an analysis of your solution's time and space complexity using Big O notation. For detailed guidance, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Instructions to Contribute

### Step 1: Fork the Repository
1. Click the "Fork" button at the top-right corner of this repository to create your own copy.

### Step 2: Clone Your Fork
```bash
git clone https://github.com/<your-username>/data-structures-algorithms-study.git
cd data-structures-algorithms-study
```

### Step 3: Create a Branch
Switch to the branch for the current week (e.g., `week-1`):
```bash
git checkout week-1
```

### Step 4: Add Your Solution
1. Create a folder with your name and the programming language (e.g., `adriano_java`).
2. Inside your folder, create subfolders for each challenge (e.g., `01_longest_substring_in_a_string`).
3. Add your solution file(s) to the respective subfolder.

### Step 5: Commit and Push
```bash
git add .
git commit -m "Add solutions for week-1 challenges"
git push origin week-1
```

### Step 6: Open a Pull Request
1. Go to your forked repository on GitHub.
2. Click "Compare & pull request."
3. Ensure the base repository is this repository and the base branch is the corresponding week branch (e.g., `week-1`).
4. Add a meaningful title and description, then click "Create pull request."

## Example Structure

Here’s an example of how your folder and files should look:

```
challenges/
├── adriano_java/
│   ├── 01_longest_substring_in_a_string/
│   │   ├── Solution.java
│   │   └── README.md
│   ├── 02_binary_search/
│   │   ├── Solution.java
│   │   └── README.md
├── jane_python/
│   ├── 01_longest_substring_in_a_string/
│   │   ├── solution.py
│   │   └── README.md
│   ├── 02_binary_search/
│   │   ├── solution.py
│   │   └── README.md
```

## Notes
- Be respectful of others' work and provide constructive feedback on PRs.
- Feel free to discuss different approaches to solving challenges in the PR comments.

Happy coding!