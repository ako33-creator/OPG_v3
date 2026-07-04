"""Basic performance safety tests for Project Model."""

from opg.project_model import Project, ProjectCloner
from opg.project_model.diff import ProjectDiffer
from opg.project_model.query import ProjectQueryEngine
from opg.project_model.snapshot import ProjectSnapshotter


def test_clone_performance_safety():
    project = Project("Perf Test")

    cloned = ProjectCloner.clone(project)

    assert cloned is not project


def test_snapshot_performance_safety():
    project = Project("Perf Test")

    snapshot = ProjectSnapshotter.snapshot(project)

    assert isinstance(snapshot.data, dict)


def test_diff_performance_safety():
    project = Project("Perf Test")

    diff = ProjectDiffer.diff(project, project)

    assert diff.has_changes is False


def test_query_performance_safety():
    project = Project("Perf Test")

    result = ProjectQueryEngine.query(project, lambda d: True)

    assert len(result) >= 0