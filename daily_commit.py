import os
import random
from datetime import datetime

DSA_PROBLEMS_POOL = [
    {
        "name": "Search in Rotated Sorted Array",
        "difficulty": "Hard",
        "lang": "python",
        "filename": "search_rotated.py",
        "code": """def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
""",
        "desc": "Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums."
    },
    {
        "name": "Merge k Sorted Lists",
        "difficulty": "Hard",
        "lang": "python",
        "filename": "merge_k_lists.py",
        "code": """import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    h = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(h, (lst.val, i, lst))
    
    dummy = ListNode(0)
    curr = dummy
    while h:
        val, i, node = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next
""",
        "desc": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it."
    },
    {
        "name": "Valid Palindrome",
        "difficulty": "Easy",
        "lang": "python",
        "filename": "valid_palindrome.py",
        "code": """def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
""",
        "desc": "A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward."
    },
    {
        "name": "Subsets",
        "difficulty": "Medium",
        "lang": "python",
        "filename": "subsets.py",
        "code": """def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
""",
        "desc": "Given an integer array nums of unique elements, return all possible subsets (the power set)."
    }
]

def run_daily_update():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    problem = random.choice(DSA_PROBLEMS_POOL)
    
    problem_name_clean = problem["name"].replace(" ", "-")
    prob_dir = os.path.join(repo_dir, "LeetCode", problem_name_clean)
    
    # Avoid duplicate folders if already run, add timestamp suffix if so
    if os.path.exists(prob_dir):
        timestamp = datetime.now().strftime("%M%S")
        prob_dir = f"{prob_dir}-{timestamp}"
        
    os.makedirs(prob_dir, exist_ok=True)
    
    # Write solution
    sol_file = os.path.join(prob_dir, problem["filename"])
    with open(sol_file, "w", encoding="utf-8") as f:
        f.write(problem["code"])
        
    # Write README
    readme_file = os.path.join(prob_dir, "README.md")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(f"# LeetCode: {problem['name']}\n\n**Difficulty:** {problem['difficulty']}\n\n## Description\n{problem['desc']}\n")
        
    # Write to main README log
    main_readme = os.path.join(repo_dir, "README.md")
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_line = f"| LeetCode | [{problem['name']}](./LeetCode/{problem_name_clean}) | {problem['difficulty']} | {problem['lang'].capitalize()} | {date_str} |\n"
    
    with open(main_readme, "a", encoding="utf-8") as f:
        f.write(log_line)
        
    print(f"Logged new solve: {problem['name']}")

if __name__ == "__main__":
    run_daily_update()
