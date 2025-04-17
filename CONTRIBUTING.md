# Contributing to Data Structures and Algorithms Study Group

Thank you for your interest in contributing to this repository! Please follow these guidelines to ensure a smooth collaboration.

## How to Contribute

1. **Fork the Repository**  
   - Click the "Fork" button at the top-right corner of this repository to create your own copy.

2. **Clone Your Fork**  
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/data-structures-algorithms-study.git
     cd data-structures-algorithms-study
     ```

3. **Switch to the Weekly Branch**  
   - Each week, a branch will be created for the assigned challenges (e.g., `week-1`, `week-2`). Switch to the appropriate branch:
     ```bash
     git checkout week-<week-number>
     ```

4. **Add Your Solution**  
   - Create a folder with your name and the programming language you are using (e.g., `adriano_java`).
   - Inside your folder, create subfolders for each challenge. Use the format `challenge-number_challenge-name` (e.g., `01_longest_substring_in_a_string`).
   - Add your solution file(s) to the respective subfolder.

5. **Write a README (Optional)**  
   - You can include a `README.md` in your challenge folder to explain your approach, thought process, or any challenges you faced.

6. **Commit Your Changes**  
   - Stage and commit your changes:
     ```bash
     git add .
     git commit -m "Add solutions for week-<week-number> challenges"
     ```

7. **Push Your Changes**  
   - Push your changes to your forked repository:
     ```bash
     git push origin week-<week-number>
     ```

8. **Open a Pull Request**  
   - Go to your forked repository on GitHub.
   - Click "Compare & pull request."
   - Ensure the base repository is this repository and the base branch is `main`.
   - Add a meaningful title and description, then click "Create pull request."

## Big O Notation Guidance

Big O notation is a way to describe the efficiency of your algorithm in terms of time and space complexity. When contributing solutions, please include an analysis of your algorithm's complexity. Here's a quick overview:

- **Time Complexity**: Describes how the runtime of your algorithm grows as the input size increases.
  - Example: `O(n)` means the runtime grows linearly with the input size.
- **Space Complexity**: Describes how the memory usage of your algorithm grows as the input size increases.
  - Example: `O(1)` means the algorithm uses constant memory regardless of input size.

### Common Big O Notations
- `O(1)`: Constant time
- `O(log n)`: Logarithmic time
- `O(n)`: Linear time
- `O(n log n)`: Linearithmic time
- `O(n^2)`: Quadratic time
- `O(2^n)`: Exponential time

Including this analysis helps others understand the trade-offs of your solution and compare it with alternative approaches.

## Code of Conduct

- Be respectful of others' work and contributions.
- Provide constructive feedback when reviewing pull requests.
- Avoid plagiarism. Ensure your solutions are your own work.

## Pull Request Guidelines

- Ensure your code is well-documented and follows the repository's folder structure.
- Test your code thoroughly before submitting.
- Add meaningful commit messages to describe your changes.
- If you are solving a challenge in a new language, ensure the folder structure is consistent with the examples provided in the `README.md`.
- **Create Unit Tests**: If possible, include unit tests for your code to verify its correctness. Place the test files in the same folder as your solution or in a dedicated `tests` folder.
- **Set Up a CI Pipeline**: If you are familiar with Continuous Integration (CI) tools (e.g., GitHub Actions), consider adding a pipeline to automatically run your tests. This ensures that your code works as expected and maintains quality.
- **Explain Your Solution**: In your pull request description or in a `README.md` file within your solution folder, explain your approach and why you chose it. Highlight the trade-offs, challenges, and any assumptions made.
- **Provide References**: If you used any reference material (e.g., articles, books, or tutorials) to develop your solution, include them in your explanation. This helps others understand the context and learn from your work.

## Example Folder Structure

```
challenges/
├── your_name_language/
│   ├── 01_challenge-name/
│   │   ├── solution.ext
│   │   └── README.md (optional)
│   ├── 02_challenge-name/
│   │   ├── solution.ext
│   │   └── README.md (optional)
```

## Need Help?

If you have any questions or need help, feel free to open an issue or reach out to the group.

Happy coding!