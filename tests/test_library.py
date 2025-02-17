"""Check that the library is working as expected."""

import json
from importlib import util
from pathlib import Path


def test_library_matches() -> None:
    """Check that library.json corresponds to valid files."""
    # TODO: add more validation checks
    hub_dir = Path(__file__).parent.parent / "loader_hub"
    library_path = hub_dir / "library.json"
    library_dict = json.load(open(library_path, "r"))
    for k, entry in library_dict.items():
        # make sure every entry has an "id" field
        assert "id" in entry
        entry_id = entry["id"]
        entry_dir = hub_dir / entry_id
        # make sure the loader directory exists
        assert entry_dir.exists()
        entry_file = entry_dir / "base.py"
        # make sure that the loader file exists
        assert entry_file.exists()

        spec = util.spec_from_file_location("custom_loader", location=str(entry_file))
        if spec is None:
            raise ValueError(f"Could not find file: {str(entry_file)}.")
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore
