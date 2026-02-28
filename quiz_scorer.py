
def calculate_total(scores):
    """Return the total of all scores."""
    return sum(scores)


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def get_highest(scores):
    if len(scores) == 0:
        return None
    return max(scores)


def get_lowest(scores):
    if len(scores) == 0:
        return None
    return min(scores)


def add_score(scores, new_score):
    scores.append(new_score)
    return scores


if __name__ == "__main__":
    student_scores = [85, 90, 78, 92, 88]

    print("Quiz Scorer - Created by Ayman")
    print("Scores:", student_scores)
    print("Total:", calculate_total(student_scores))
    print("Average:", calculate_average(student_scores))
    print("Highest:", get_highest(student_scores))
    print("Lowest:", get_lowest(student_scores))