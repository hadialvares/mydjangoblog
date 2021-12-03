from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg',blank=True)

    # in add author

    def __str__(self):        # توی پوشه ارتیکل برای عنوان مفاله تایتل را نشان میدهد
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'     # بجای اینکه کل مقاله را نشان دهد فقط 50 کاراکتر نشان میدهد
