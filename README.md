# Django project template
My favorite django project skeleton with separated setting files handled by [django-environ](https://github.com/joke2k/django-environ).

## Basic project:
```bash
django-admin startproject \
--template="https://github.com/tinnguyen18920/django-project-template/archive/master.zip" \
project_name \
project_dir 
```

If in production environment. Make sure `SECRET_KEY` and `DATABASE_URL` in `project_name/.env` or `os.environ` (this is more priority) not be blanked.


## Project with Heroku files:
Using template at heroku branch. As the same in `master` branch but has `Procfile`, other dependencies in Pipfile.
```bash
django-admin startproject \
--template="https://github.com/tinnguyen18920/django-project-template/archive/heroku.zip" \
--name=Procfile \
project_name \
project_dir 
```
Don't forget to set `DJANGO_SETTINGS_MODULE` on heroku config vars.



# License
MIT License

Copyright (c) 2021 tinnguyen18920

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.