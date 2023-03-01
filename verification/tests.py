"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
        "input": ["2023-03-01", "2023-03-01", "09:00", "17:00", []],
        "answer": 8,
        "explanation": "start and end dates are the same and there are no holidays"
        },
        {
        "input": ["2023-03-01", "2023-03-02", "09:00", "17:00", []],
        "answer": 16,
        "explanation": "start and end dates are consecutive weekdays with no holidays"
        },
        {
        "input": ["2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]],
        "answer": 16,
        "explanation": "start and end dates are consecutive weekdays and there is one holiday"
        },
    ],
    "Extra": [
        {
        "input": ["2023-03-01", "2023-03-02", "09:00", "17:00", ["2023-03-01", "2023-03-02"]],
        "answer": 0,
        "explanation": "start and end dates are consecutive weekdays and there is a holiday on both days"
        },
        {
        "input": ["2023-03-01", "2023-03-05", "09:00", "17:00", []],
        "answer": 24,
        "explanation": "no work at weekend"
        },
        {
        "input": ["2023-03-01", "2023-03-05", "09:00", "13:00", ["2023-03-01", "2023-03-03"]],
        "answer": 4,
        "explanation": "no work at weekend and holidays"
        },
    ]
}
