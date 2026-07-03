from opg.project_model import Project


def test_project_initially_contains_no_objects():
    project = Project(name="Demo")

    assert hasattr(project, "objects")
    assert project.objects == []


def test_project_object_count_is_zero():
    project = Project(name="Demo")

    assert project.object_count == 0


def test_projects_do_not_share_object_lists():
    project_a = Project(name="A")
    project_b = Project(name="B")

    assert project_a.objects is not project_b.objects