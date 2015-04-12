from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from wiki.models import Page, PageForm

def Index(request):
  latest_added_pages = Page.objects.order_by('-pub_date')[:20]
  context = {'latest_added_pages': latest_added_pages}
  return render(request, 'wiki/index.html', context)

def WikiPage(request, title):
  try:
    page = Page.objects.get(title=title)
    return render(request, 'wiki/page.html', {'page': page})
  except Page.DoesNotExist:
    return HttpResponseRedirect(reverse('wiki:editpage', args=(title,)))

def EditPage(request, title):
  try:
    page = Page.objects.get(title=title)
  except Page.DoesNotExist:
    page = Page(title=title, content="")


  if request.method == 'GET':
    form = PageForm(instance=page)
    return render(request, 'wiki/edit.html', {'page': page, 'form' : form})

  if request.method == 'POST':
    form = PageForm(request.POST, instance=page)
    form.save()
    #page.content = request.POST['content']
    #page.save()
    return HttpResponseRedirect(reverse('wiki:wikipage', args=(title,)))
    
  

def HistoryPage(request, title):
  page = get_object_or_404(Page, title=title)
  return render(request, 'wiki/page.html', {'page': page})






#########
##class Handler(webapp2.RequestHandler):
##  def write(self, *a, **kw):
##    self.response.out.write(*a, **kw)
##
##  def render(self, template, **kw):
##    t = jinja_env.get_template(template)
##    self.write(t.render(kw))
##        
##class EditPage(Handler):
##    def get(self, path):
##        username = None
##        user_cookie = self.request.cookies.get('user_id')
##        if user_cookie:
##            username = user_cookie.split('|')[0]
##            if check_secure_val(user_cookie) == username:
##                pass
##            else:
##                self.response.delete_cookie('user_id')
##                self.redirect("/login")
##        else:
##           self.redirect("/login")
##
##        v = self.request.get('v')
##        page = ver_check(v, path)
##
##        if page == None or page.content == None:
##            content = ''
##        else:
##            content = page.content
##        self.render("edit.html", username=username, url=path ,content=content)
##
##    def post(self, path):
##        content = self.request.get("content")
##        old_page = Page.by_path(path).get()
##
##        if not (old_page or content):
##            return
##        elif not old_page or old_page.content != content:
##            p = Page(parent = Page.parent_key(path), content = content)
##            p.put()
##            
##        self.redirect(path)
##
##class HistoryPage(Handler):
##    def get(self, path):
##        q = Page.by_path(path)
##        q.fetch(limit = 100)
##
##        posts = list(q)
##        if posts:
##            self.render("history.html", url = path, posts = posts)
##        else:
##            self.redirect("/_edit" + path)
##
##class WikiPage(Handler):
##    def get(self, path):
##        username = None
##        user_cookie = self.request.cookies.get('user_id')
##        if user_cookie:
##            username = user_cookie.split('|')[0]
##            if check_secure_val(user_cookie) == username:
##                pass
##            else:
##                self.response.delete_cookie('user_id')
##                username = None
##
##        v = self.request.get('v')
##        page = ver_check(v, path)      
##        
##        if page:
##            self.render("test.html", username=username, url=path, content=page.content)
##        else:
##            self.redirect("/_edit" + path)
##        
##
##class SignupHandler(Handler):
##
##    def get(self):
##        self.render("signup.html")
##
##    def post(self):
##        have_error = False
##        username = self.request.get('username')
##        password = self.request.get('password')
##        verify = self.request.get('verify')
##        email = self.request.get('email')
##
##        params = dict(username = username,
##                      email = email)
##
##        if not valid_username(username):
##            params['user_error'] = "That's not a valid username."
##            have_error = True
##
##        if not valid_password(password):
##            params['pass_error'] = "That wasn't a valid password."
##            have_error = True
##        elif password != verify:
##            params['verify_error'] = "Your passwords didn't match."
##            have_error = True
##
##        if not valid_email(email):
##            params['email_error'] = "That's not a valid email."
##            have_error = True
##
##        users = db.GqlQuery("select user_id from Users")
##        for user in users:
##            if username == user.user_id:
##                params['user_error'] = "That user already exists"
##                have_error = True
##
##        if have_error:
##            self.render("signup.html", **params)
##        else:
##            pwh = make_pw_hash(username, password)
##            u = Users(user_id=username, email=email, password=pwh)
##            u.put()
##
##            self.response.headers['Content-Type'] = 'text/plain'
##            user_cookie_str = self.request.cookies.get('user_id')
##            if user_cookie_str:
##                cookie_val = check_secure_val(user_cookie_str)
##                if cookie_val:
##                    self.redirect("/welcome")
##
##            new_user_val = make_secure_val(str(username))
##            self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_user_val)
##            self.redirect("/")
##
##class LogIn(Handler):
##
##    def get(self):
##        self.render("login.html")
##
##    def post(self):
##        have_error = False
##        username = self.request.get('username')
##        password = self.request.get('password')
##        
##        checkUserName = Users.all()
##        checkUserName.filter('user_id', username)
##        userNameResult = checkUserName.get()
##
##        params ={}
##
##        if userNameResult:
##            pwh = userNameResult.password
##            if check_pw(username, password, pwh):
##                user_val = make_secure_val(str(username))
##                self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % user_val)
##                self.redirect("/")
##            else:
##                params['invalid_login'] = "This is an invalid login."
##                self.render('login.html', **params)
##        else:
##            params['invalid_login'] = "This is an invalid login."
##            self.render('login.html', **params)
##            
##class LogOut(Handler):
##
##    def get(self):
##        self.response.delete_cookie('user_id')
##        self.redirect("/")
