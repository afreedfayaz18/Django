afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~$ cd Documents
afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ source afr_env/bin/activate
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ python manage.py runserver
python: can't open file 'manage.py': [Errno 2] No such file or directory
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ cd eshop1
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 29, 2021 - 15:43:46
Django version 3.2, using settings 'eshop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[29/Apr/2021 15:44:45] "GET /admin/ HTTP/1.1" 302 0
[29/Apr/2021 15:44:45] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
[29/Apr/2021 15:44:45] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2271
[29/Apr/2021 15:44:45] "GET /static/admin/css/login.css HTTP/1.1" 200 939
[29/Apr/2021 15:44:45] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18545
[29/Apr/2021 15:44:45] "GET /static/admin/css/base.css HTTP/1.1" 200 19513
[29/Apr/2021 15:44:45] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[29/Apr/2021 15:44:45] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 1360
[29/Apr/2021 15:44:45] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[29/Apr/2021 15:44:45] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
^C(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py createsuperserver
Unknown command: 'createsuperserver'. Did you mean createsuperuser?
Type 'manage.py help' for usage.
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py createsuperuser
Username (leave blank to use 'afreedfayaz'): admin1
Email address: 
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: 
Password: 
Password (again): 
Superuser created successfully.
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 29, 2021 - 15:50:44
Django version 3.2, using settings 'eshop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[29/Apr/2021 15:51:25] "GET /admin/ HTTP/1.1" 302 0
[29/Apr/2021 15:51:25] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
[29/Apr/2021 15:51:40] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[29/Apr/2021 15:51:40] "GET /admin/ HTTP/1.1" 200 3327
[29/Apr/2021 15:51:40] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[29/Apr/2021 15:51:40] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[29/Apr/2021 15:51:40] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[29/Apr/2021 15:51:40] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[29/Apr/2021 15:51:45] "GET /admin/auth/user/ HTTP/1.1" 200 7828
[29/Apr/2021 15:51:45] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[29/Apr/2021 15:51:45] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[29/Apr/2021 15:51:45] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6874
[29/Apr/2021 15:51:45] "GET /static/admin/js/core.js HTTP/1.1" 200 5698
[29/Apr/2021 15:51:45] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[29/Apr/2021 15:51:45] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[29/Apr/2021 15:51:45] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7902
[29/Apr/2021 15:51:45] "GET /static/admin/js/actions.js HTTP/1.1" 200 6540
[29/Apr/2021 15:51:45] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[29/Apr/2021 15:51:45] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 5984
[29/Apr/2021 15:51:45] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[29/Apr/2021 15:51:45] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
[29/Apr/2021 15:51:46] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[29/Apr/2021 15:51:46] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 200 1097
[29/Apr/2021 15:51:55] "GET /admin/auth/user/1/change/ HTTP/1.1" 200 15051
[29/Apr/2021 15:51:55] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[29/Apr/2021 15:51:55] "GET /static/admin/css/forms.css HTTP/1.1" 200 8804
[29/Apr/2021 15:51:55] "GET /static/admin/js/calendar.js HTTP/1.1" 200 8466
[29/Apr/2021 15:51:55] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19634
[29/Apr/2021 15:51:55] "GET /static/admin/js/SelectBox.js HTTP/1.1" 200 4360
[29/Apr/2021 15:51:55] "GET /static/admin/js/SelectFilter2.js HTTP/1.1" 200 12350
[29/Apr/2021 15:51:55] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[29/Apr/2021 15:51:55] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
[29/Apr/2021 15:51:55] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11097
[29/Apr/2021 15:51:55] "GET /static/admin/img/icon-unknown.svg HTTP/1.1" 200 655
[29/Apr/2021 15:51:55] "GET /static/admin/img/selector-icons.svg HTTP/1.1" 200 3291
[29/Apr/2021 15:51:55] "GET /static/admin/img/icon-unknown-alt.svg HTTP/1.1" 200 655
[29/Apr/2021 15:51:55] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
[29/Apr/2021 15:51:55] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
[29/Apr/2021 15:52:23] "POST /admin/auth/user/1/change/ HTTP/1.1" 302 0
[29/Apr/2021 15:52:24] "GET /admin/auth/user/ HTTP/1.1" 200 8030
[29/Apr/2021 15:52:24] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[29/Apr/2021 15:52:58] "GET /admin/ HTTP/1.1" 302 0
[29/Apr/2021 15:52:58] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
[29/Apr/2021 15:52:58] "GET /static/admin/css/base.css HTTP/1.1" 200 19513
[29/Apr/2021 15:52:58] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2271
[29/Apr/2021 15:52:58] "GET /static/admin/css/login.css HTTP/1.1" 200 939
[29/Apr/2021 15:52:58] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18545
[29/Apr/2021 15:52:58] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 1360
[29/Apr/2021 15:52:58] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[29/Apr/2021 15:52:58] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[29/Apr/2021 15:52:58] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[29/Apr/2021 15:52:58] "GET /favicon.ico HTTP/1.1" 404 1995
/home/afreedfayaz/Documents/eshop1/eshop1/settings.py changed, reloading.
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/afreedfayaz/Documents/afr_env/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/home/afreedfayaz/Documents/afr_env/lib/python3.8/site-packages/django/core/management/__init__.py", line 363, in execute
    settings.INSTALLED_APPS
  File "/home/afreedfayaz/Documents/afr_env/lib/python3.8/site-packages/django/conf/__init__.py", line 82, in __getattr__
    self._setup(name)
  File "/home/afreedfayaz/Documents/afr_env/lib/python3.8/site-packages/django/conf/__init__.py", line 69, in _setup
    self._wrapped = Settings(settings_module)
  File "/home/afreedfayaz/Documents/afr_env/lib/python3.8/site-packages/django/conf/__init__.py", line 170, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/afreedfayaz/Documents/eshop1/eshop1/settings.py", line 57, in <module>
    'DIRS': [templates],
NameError: name 'templates' is not defined
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$