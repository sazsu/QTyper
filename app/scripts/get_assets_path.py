from pathlib import Path


def get_assets_path(app_path: Path):
	if app_path.stem == 'app':
		return app_path / 'assets'
	return app_path / '_internal' / 'app' / 'assets'
