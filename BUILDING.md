## Пререквизиты

[pyinstaller](https://pyinstaller.org/en/stable/requirements.html)

## Сборка

### Unix-like

```sh
cd path/to/QTyper
```
```sh
pyinstaller --onedir --add-data=app/startup.sql:app --add-data=app/assets:app/assets --icon=path/to/QTyper/app/assets/logo_light.png --name=QTyper --noconsole app/__main__.py
```

### Windows
```sh
cd path\to\QTyper
```

```sh
pyinstaller --onedir --add-data=app\startup.sql;app --add-data=app\assets;app\assets --icon=path\to\QTyper\app\assets\logo_light.png --name=QTyper --noconsole app\__main__.py
```
