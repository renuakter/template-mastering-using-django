# Untitled

# 🚀 Django Template Mastering (Clean Project Setup)

## 📁 Project Structure

```
myproject/
│
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│
├── authentication_app/
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── master/
│   │   ├── base.html
│   │   ├── nav.html
│   │
│   └── home.html
```

---

# ⚙️ Step 1: settings.py Configuration

```
TEMPLATES= [
    {
'DIRS': [BASE_DIR/'templates'],
'APP_DIRS':True,
    },
]
```

---

# 🌐 Step 2: Main URL Configuration

📍 `myproject/urls.py`

```
fromdjango.contribimportadmin
fromdjango.urlsimportpath,include

urlpatterns= [
path('admin/',admin.site.urls),
path('',include('authentication_app.urls')),
]
```

---

# 🔗 Step 3: App URL Configuration

📍 `authentication_app/urls.py`

```
fromdjango.urlsimportpath
from.viewsimportbasepage

urlpatterns= [
path('',basepage,name='basepage'),
]
```

---

# 🧠 Step 4: View Function

📍 `authentication_app/views.py`

```
fromdjango.shortcutsimportrender

defbasepage(request):
returnrender(request,"home.html")
```

---

# 🎨 Step 5: Master Base Template

📍 `templates/master/base.html`

```
<!DOCTYPE html>
<html>
<head>
<title>Django Project</title>
<style>
body {
            margin:0;
            font-family:Arial;
            background: #f4f6f9;
        }

        .container {
            padding:40px;
            text-align:center;
        }

footer {
            background: #222;
            color:white;
            padding:15px;
            margin-top:40px;
        }
</style>
</head>
<body>

{% include 'master/nav.html' %}

<divclass="container">
    {% block body %}
    {% endblock %}
</div>

<footer>
<p>© 2026 Django Project | Built by Sweety</p>
</footer>

</body>
</html>
```

---

# 🧭 Step 6: Navbar Template

📍 `templates/master/nav.html`

```
<style>
ul {
    list-style-type:none;
    margin:0;
    padding:0;
    overflow:hidden;
    background: #333;
}

li {
    float:left;
}

lia {
    display:block;
    color:white;
    padding:14px20px;
    text-decoration:none;
}

lia:hover {
    background: #111;
}
</style>

<ul>
<li><ahref="/">Home</a></li>
<li><ahref="#">About</a></li>
<li><ahref="#">Contact</a></li>
</ul>
```

---

# 🏠 Step 7: Child Template (Home Page)

📍 `templates/home.html`

```
{% extends 'master/base.html' %}

{% block body %}
<h1>Welcome to Django Template Mastering 🎉</h1>
<p>This page is using template inheritance.</p>
{% endblock %}
```

---

# ▶️ Run Server

```
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 🧩 Template Concept Summary

| Feature | Purpose |
| --- | --- |
| `{% extends %}` | Connect child template with base |
| `{% block %}` | Placeholder area |
| `{% include %}` | Reuse small components |
| `include()` in urls | Connect app URL |
