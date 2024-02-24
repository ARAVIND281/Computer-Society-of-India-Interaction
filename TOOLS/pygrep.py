import argparse
import re
import os
import sys

def grep_files(pattern, files, ignore_case=False, count=False, recursive=False, before_context=0, after_context=0, invert_match=False, word_match=False, colorize=False):
    regex_flags = re.IGNORECASE if ignore_case else 0
    if word_match:
        pattern = r'\b{}\b'.format(pattern)
    compiled_pattern = re.compile(pattern, regex_flags)
    total_matches = 0

    for file_path in files:
        if os.path.isdir(file_path) and recursive:
            for root, _, filenames in os.walk(file_path):
                for filename in filenames:
                    total_matches += process_file(os.path.join(root, filename), compiled_pattern, count, before_context, after_context, invert_match, colorize)
        elif os.path.isfile(file_path):
            total_matches += process_file(file_path, compiled_pattern, count, before_context, after_context, invert_match, colorize)
        else:
            print(f"Error: {file_path} is not a valid file or directory", file=sys.stderr)

    if count:
        print(f"Total matches: {total_matches}")

def process_file(file_path, compiled_pattern, count, before_context, after_context, invert_match, colorize):
    matches = 0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                match = compiled_pattern.search(line) is not None
                if invert_match:
                    match = not match
                if match:
                    matches += 1
                    if not count:
                        context_before = lines[max(0, i-before_context):i]
                        context_after = lines[i+1:i+1+after_context]
                        display_match(file_path, i+1, line, context_before, context_after, colorize)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
    return matches

def display_match(file_path, line_number, line, context_before, context_after, colorize):
    if colorize:
        line = re.sub(r'(' + pattern + r')', '\033[91m\\1\033[0m', line)
    if context_before:
        for context_line in context_before:
            print(f"{file_path}:{line_number - len(context_before)}-{context_line}", end='')
    print(f"{file_path}:{line_number}:{line}", end='')
    if context_after:
        for context_line in context_after:
            print(f"{file_path}:{line_number + len(context_after)}+{context_line}", end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python implementation of grep")
    parser.add_argument('pattern', type=str, help="Pattern to search for")
    parser.add_argument('files', type=str, nargs='+', help="Files or directories to search")
    parser.add_argument('-i', '--ignore-case', action='store_true', help="Ignore case distinctions")
    parser.add_argument('-c', '--count', action='store_true', help="Only print a count of matching lines per file")
    parser.add_argument('-r', '--recursive', action='store_true', help="Recursively search directories")
    parser.add_argument('-B', '--before-context', type=int, default=0, help="Print NUM lines of leading context")
    parser.add_argument('-A', '--after-context', type=int, default=0, help="Print NUM lines of trailing context")
    parser.add_argument('-v', '--invert-match', action='store_true', help="Select non-matching lines")
    parser.add_argument('-w', '--word-match', action='store_true', help="Force PATTERN to match only whole words")
    parser.add_argument('--color', action='store_true', help="Highlight matching text")

    args = parser.parse_args()

    grep_files(args.pattern, args.files, args.ignore_case, args.count, args.recursive, args.before_context, args.after_context, args.invert_match, args.word_match, args.color)
