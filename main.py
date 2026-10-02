# Simulate a list of issues/tasks for a hypothetical open-source project
project_issues = [
    {
        "id": 1,
        "title": "Fix typo in README",
        "description": "There's a typo in the 'Installation' section of the README file.",
        "labels": ["documentation", "easy", "good first issue"],
        "difficulty": "easy"
    },
    {
        "id": 2,
        "title": "Implement user authentication",
        "description": "Add user registration and login functionality.",
        "labels": ["feature", "complex"],
        "difficulty": "hard"
    },
    {
        "id": 3,
        "title": "Update dependencies",
        "description": "Upgrade all project dependencies to their latest stable versions.",
        "labels": ["maintenance", "medium"],
        "difficulty": "medium"
    },
    {
        "id": 4,
        "title": "Bug: Button not clickable on mobile",
        "description": "The 'Submit' button is not responsive on small screens.",
        "labels": ["bug", "frontend", "good first issue"],
        "difficulty": "easy"
    },
    {
        "id": 5,
        "title": "Add unit tests for utility functions",
        "description": "Write unit tests for the `utils.py` module.",
        "labels": ["testing", "medium"],
        "difficulty": "medium"
    },
    {
        "id": 6,
        "title": "Refactor database connection",
        "description": "Improve the way the application connects to the database for better performance.",
        "labels": ["refactoring", "complex"],
        "difficulty": "hard"
    },
    {
        "id": 7,
        "title": "Add example usage to docstrings",
        "description": "Enhance docstrings for public functions with small usage examples.",
        "labels": ["documentation", "easy"],
        "difficulty": "easy"
    }
]

def find_first_pr_tasks(issues):
    """
    Simulates OSS Buddy by finding small, manageable tasks suitable for a first PR.
    Filters issues based on 'easy' difficulty and specific labels.
    """
    first_pr_candidates = []
    for issue in issues:
        # OSS Buddy logic: Identify tasks that are 'easy' and fall into common first-PR categories.
        if issue["difficulty"] == "easy" and \
           ("documentation" in issue["labels"] or "bug" in issue["labels"] or "good first issue" in issue["labels"]):
            first_pr_candidates.append(issue)
    return first_pr_candidates

if __name__ == "__main__":
    print("Welcome to OSS Buddy!")
    print("Searching for small, valuable tasks for your first Pull Request...\n")

    suggested_tasks = find_first_pr_tasks(project_issues)

    if suggested_tasks:
        print("Here are some tasks OSS Buddy suggests for your first PR:")
        for task in suggested_tasks:
            print(f"- ID: {task['id']}, Title: {task['title']}")
            print(f"  Description: {task['description']}")
            print(f"  Labels: {', '.join(task['labels'])}\n")
    else:
        print("No suitable tasks found at the moment. Keep an eye out for new opportunities!")
