"""Tests for Project Model query system."""

from opg.project_model import Project, ProjectQueryEngine


def test_project_query_returns_query_object():
    project = Project("Test Project")

    query = ProjectQueryEngine.query(project, lambda data: True)

    assert query is not None


def test_project_query_returns_results_when_predicate_matches():
    project = Project("Test Project")

    query = ProjectQueryEngine.query(project, lambda data: True)

    assert len(query) == 1


def test_project_query_returns_empty_when_predicate_fails():
    project = Project("Test Project")

    query = ProjectQueryEngine.query(project, lambda data: False)

    assert len(query) == 0


def test_project_query_result_contains_serialized_project():
    project = Project("Test Project")

    query = ProjectQueryEngine.query(project, lambda data: True)

    assert isinstance(query.results, list)
    assert isinstance(query.results[0], dict)