import importlib.metadata
import pytest

from sqlite_utils import Database, plugins


@pytest.fixture(scope="function")
def db() -> Database:
    return Database(memory=True, execute_plugins=True)


def test_plugin_installed() -> None:
    found = next(
        filter(lambda x: x["name"] == "sqlite-utils-ml", plugins.get_plugins())
    )
    assert found is not None
    assert found["version"] == importlib.metadata.version("sqlite-utils-ml")


@pytest.mark.parametrize(
    "func",
    [
        "sqml_python_version",
        "sqml_sklearn_version",
        "sqml_load_dataset",
        "sqml_train",
        "sqml_predict",
        "sqml_predict_batch",
    ],
)
def test_registered_functions(db: Database, func: str) -> None:
    functions = {f["name"] for f in db.execute("select name from pragma_function_list")}
    assert func in functions


@pytest.mark.parametrize(
    "table",
    [
        "sqml_experiments",
        "sqml_runs",
        "sqml_models",
        "sqml_metrics",
        "sqml_deployments",
    ],
)
def test_created_tables(db: Database, table: str) -> None:
    assert table in db.table_names()
