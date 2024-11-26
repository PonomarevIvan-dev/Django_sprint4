# django_sprint4
Здравстуйте, подскажите пожалуйста, какой вариант написания проекта в теории лучше? Если бы у меня в файле views было написано все через функции или лучше делать вот так в классах как в данном проекте? Я начал делать через функции просто, но в общей группе прочел такое мнение, что некоторым ребятам прям на ревью сказали писать через классы и тоже переделал вот таким методом, но есть половина проекта написаная через функции.. Ниже скину пример того, что я имею ввиду, надеюсь я понятно сформулировал свой вопрос..

def post_detail(request, pk): post = get_object_or_404(Post, pk=pk) return render(request, 'blog/post_detail.html', {'post': post})

def edit_post(request, pk): post = get_object_or_404(Post, pk=pk)

if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', pk=post.pk)
else:
    form = PostForm(instance=post)

return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

вот и все в таком духе без классов.