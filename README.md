# make24_flet_app
Make 24 Flet App.

## Install Flet
```shell
pip install --upgrade Flet
```

## Publish the App
```shell
flet publish make24_flet_app.py --distpath ./docs --app-name "Make 24" --route-url-strategy hash
```

## Customize the App
Replace `favicon.png` in `docs` folder and all `*.png` icons in `docs/icons` folder with customized ones.

## Test the App
```shell
python -m http.server --directory ./docs
```
And open `http://localhost:8000` in a brower.

## Deploy to Cloudflare
In Cloudflare Pages, create a new project and upload the `docs` folder.
[Make 24 Flet App](https://make24-flet-app.pages.dev/)
