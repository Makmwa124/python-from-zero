# programs/ch15_args_demo.py
"""Show what sys.argv contains when you run a program with arguments."""
import sys

print("sys.argv is:", sys.argv)
name = sys.argv[1]
print(f"Hello, {name}! Welcome to Sunny Paws.")
