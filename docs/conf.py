from good_identity_federation_practice import __app_name__, __version__

project = __app_name__.replace("-", " ").title()
author = "Albert Wu, Matthew X. Economou, Sebastian Benatar"
copyright = f"2024, {author}"
release = __version__
version = __version__

extensions = ["myst_parser"]

myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]
