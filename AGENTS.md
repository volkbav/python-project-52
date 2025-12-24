Ты не должен смотреть в файлы, указанные в .gitignore

## Структура проекта

```
build.sh
Makefile
manage.py
pyproject.toml
README.md
ruff.toml
locale/
	ru/
		LC_MESSAGES/
			django.mo
			django.po
task_manager/
	__init__.py
	asgi.py
	functions.py
	mixins.py
	rollbar_test.py
	settings.py
	urls.py
	views.py
	wsgi.py
	labels/
		__init__.py
		admin.py
		apps.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py
		migrations/
			__init__.py
			0001_initial.py
	statuses/
		__init__.py
		admin.py
		apps.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py
		migrations/
			__init__.py
			0001_initial.py
			0002_rename_statusindexview_status_alter_status_options.py
			0003_alter_status_name.py
	tasks/
		__init__.py
		admin.py
		apps.py
		filter.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py
		migrations/
			__init__.py
			0001_initial.py
			0002_task_author_task_status.py
			0003_alter_task_options_task_description_task_executor_and_more.py
			0004_task_labels.py
			0005_alter_task_labels.py
	templates/
		base.html
		form.html
		header.html
		root.html
		labels/
			create.html
			delete.html
			index.html
			update.html
		registration/
			login.html
		statuses/
			create.html
			delete.html
			index.html
			update.html
		tasks/
			create.html
			delete.html
			index.html
			show_task.html
			update.html
		users/
			create.html
			delete.html
			index.html
			update.html
	users/
		__init__.py
		admin.py
		apps.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py
		migrations/
			__init__.py
```

## Запрещенные для просмотра файлы и папки (.gitignore)

Агент не должен просматривать следующие файлы и папки, указанные в .gitignore:

- `__pycache__/`
- `.Python`
- `build/`
- `develop-eggs/`
- `dist/`
- `downloads/`
- `eggs/`
- `.eggs/`
- `lib/`
- `lib64/`
- `parts/`
- `sdist/`
- `var/`
- `wheels/`
- `share/python-wheels/`
- `*.egg-info/`
- `.installed.cfg`
- `*.egg`
- `MANIFEST`
- `*.manifest`
- `*.spec`
- `pip-log.txt`
- `pip-delete-this-directory.txt`
- `.pytest_cache/`
- `.coverage`
- `.coverage.*`
- `.cache`
- `*.log`
- `local_settings.py`
- `db.sqlite3`
- `db.sqlite3-journal`
- `.python-version`
- `uv.lock`
- `*.sage.py`
- `.env`
- `.venv`
- `env/`
- `venv/`
- `ENV/`
- `env.bak/`
- `venv.bak/`
- `.ruff_cache/`
- `.vscode`
- `.DS_Store`
- `coverage.xml`

