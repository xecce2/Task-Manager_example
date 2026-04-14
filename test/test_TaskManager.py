import pytest
from unittest.mock import patch, mock_open, call
from json import JSONDecodeError
from src.TaskManager import TaskManager

# Mock task data for testing
mock_tasklist = [
    {"title": "Test Task 1", "description": "This is the first test task", "priority": "High"},
    {"title": "Test Task 2", "description": "This is the second test task", "priority": "Medium"}
]

# Test TaskManager initialization with an empty file (or missing file)
@patch("builtins.open", mock_open())
@patch("builtins.print")
def test_task_manager_init_empty_file(mock_print):
    tm = TaskManager()
    assert tm.tasklist == []
    printed_args = [str(c.args[0]) for c in mock_print.call_args_list]
    assert "Expecting value: line 1 column 1 (char 0)" in printed_args
    mock_print.assert_any_call("File Created")

# Test TaskManager initialization with pre-existing task list
@patch("builtins.open", mock_open(read_data='[{"title": "Test Task 1", "description": "First Task", "priority": "Low"}]'))
@patch("builtins.print")
def test_task_manager_init_existing_file(mock_print):
    tm = TaskManager()
    assert len(tm.tasklist) == 1
    assert tm.tasklist[0]["title"] == "Test Task 1"
    mock_print.assert_not_called()

# Test addTask method (mocking user input)
@patch("builtins.open", mock_open())
@patch("builtins.input", side_effect=["Test Task 3", "Test description", "Low"])
def test_add_task(mock_input):
    tm = TaskManager()
    tm.addTask()
    assert len(tm.tasklist) == 1
    assert tm.tasklist[0]["title"] == "Test Task 3"
    assert tm.tasklist[0]["priority"] == "Low"

# Test see_task method (mocking print output)
@patch("builtins.print")
def test_see_task(mock_print):
    tm = TaskManager()
    tm.tasklist = mock_tasklist
    tm.see_task()
    mock_print.assert_any_call("Test Task 1", "This is the first test task", "High")
    mock_print.assert_any_call("Test Task 2", "This is the second test task", "Medium")

# Test remove_task method (mocking user input and file write)
@patch("builtins.open", mock_open())
@patch("builtins.input", side_effect=["test task 1"])
def test_remove_task(mock_input):
    tm = TaskManager()
    tm.tasklist = mock_tasklist.copy()
    tm.remove_task()
    assert len(tm.tasklist) == 1
    assert tm.tasklist[0]["title"] == "Test Task 2"

# Test filterby_priority method (mocking user input)
@patch("builtins.input", side_effect=["high"])
@patch("builtins.print")
def test_filter_by_priority(mock_print, mock_input):
    tm = TaskManager()
    tm.tasklist = mock_tasklist
    tm.filterby_priority()
    mock_print.assert_any_call("Test Task 1", "This is the first test task", "High")

# Test task_finder method (mocking user input)
@patch("builtins.input", side_effect=["test task 1"])
@patch("builtins.print")
def test_task_finder(mock_print, mock_input):
    tm = TaskManager()
    tm.tasklist = [
        {"title": "Test Task 1", "description": "This is the first test task", "priority": "High"}
    ]
    tm.task_finder()
    mock_print.assert_any_call("Test Task 1", "This is the first test task", "High")

# Test task_finder when no task is found
@patch("builtins.input", side_effect=["nonexistent task"])
@patch("builtins.print")
def test_task_finder_not_found(mock_print, mock_input):
    tm = TaskManager()
    tm.tasklist = mock_tasklist
    tm.task_finder()
    mock_print.assert_called_once_with("Task not found")