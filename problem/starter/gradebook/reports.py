"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass

from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    averages = average_per_student(records)
    subjects = subjects_offered(records)
    top = top_scorer(records)
    passing = passing_students(records)
    
    lines = []
    lines.append("=== Gradebook Report ===")
    lines.append(f"Total records: {len(records)}")
    lines.append(f"Subjects offered: {', '.join(sorted(subjects))}")
    lines.append("")
    lines.append("Averages:")
    
    for name in sorted(averages.keys()):
        avg = averages[name]
        lines.append(f"  {name:<8}: {avg}")
    
    lines.append("")
    lines.append(f"Top scorer: {top[0]} ({top[1]})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passing)}")
    
    return "\n".join(lines)
