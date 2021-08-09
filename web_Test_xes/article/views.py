from django.http import HttpResponse
from django.shortcuts import render

from article import models
import time




def index(request):
    return render(request, 'index.html')


def create_article(request):
    return render(request,'create_article.html')



def create_tag(request):
    return render(request,'create_tag.html')



def tag(request):
    tag_name = request.POST.get('tag_name', '默认标题')  ##get是根据参数名称从form表单页获取内容
    tag_type = request.POST.get('tag_type', '默认内容')
    parent_id = request.POST.get('parent_id', '父级ID')
    create_time = request.POST.get('create_time', '创建时间')
    update_time = request.POST.get('update_time', '更新时间')
    status = request.POST.get('status', '更新时间')
    ##保存数据
    models.Tag.objects.create(tag_name=tag_name, tag_type=tag_type,parent_id = parent_id,create_time = create_time,update_time=update_time,status=status)
    # articles = models.Article.objects.all()
    return render(request, 'tag.html')

def general_column(request):
    return render(request, 'special_column.html')


def lecture_column(request):
    return render(request, 'lecture_column.html')


#创建图文素材banner
def add_banner():
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    creator = '80'
    end_time = '2029-06-26 11:54:45'
    material_id = 126513
    material_type = 6
    material_description = '自动创建'
    priority = 8
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    status = 2
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    new_banner_image_url = 'https://static-xesapi.speiyou.cn/content-center/image/2019-08-01/1564647398367.png'
    new_banner_image_id = 2514
    position = 1
    banner_type = 1
    is_delete = 0
    models.Banner.objects.create(create_time=create_time, creator=creator, end_time = end_time, material_id = material_id ,
                                 material_type=material_type,material_description=material_description,priority=priority,
                                 start_time=start_time,status=status,update_time=update_time,new_banner_image_url=new_banner_image_url,
                                 new_banner_image_id=new_banner_image_id,position=position,banner_type=banner_type,is_delete=is_delete)
def add_article():
    author = 'auto'
    cover_photo_show_type = 1
    cover_photo_url = 'https://static-xesapi.speiyou.cn/content-center/image/2019-08-01/1564625967580.jpg'
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    creator = 80
    end_time = '2019-08-31 16:16:17'
    priority = 6
    source = 10
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    status = 1
    title = 'auto文章标题'
    topping = 1
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    pic_width = 750
    pic_height = 320
    like_num = 0
    collect_num = 0
    read_num = 0
    start_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    content_url = 'https://static-xesapi.speiyou.cn/content-center/html/2019-08-05//1564992941753.html'
    is_delete = 0
    launch_status = 1
    support_comment = 0
    digest = '自动'
    update_user = 80
    models.Article.objects.create(author = author,cover_photo_show_type = cover_photo_show_type,cover_photo_url = cover_photo_url,
    create_time = create_time,creator = creator,end_time = end_time,priority = priority,source = source,
    start_time =start_time,status = status,title = title,topping =topping,update_time =update_time,pic_width = pic_width,
    pic_height = pic_height,like_num = like_num,collect_num = collect_num,read_num = read_num,start_timestamp = start_timestamp,
    content_url = content_url,is_delete = is_delete,launch_status = launch_status,support_comment = support_comment,
    digest = digest,update_user = update_user,)


def create_article_action(request):

    if request.method=="POST":
        article_num = request.POST.get('article_num', '1')
        if article_num == '':
            return HttpResponse('没有输入创建数量，请返回输入！')
        else:
            article_num = int(float(article_num))
            for i in range(1, article_num + 1):
                add_article()
                return HttpResponse(str(article_num)+'个已上架的文章创建成功，快去看看吧～')



def create_banner(request):
    return render(request, 'create_banner.html')


def create_banner_action(request):

    if request.method=="POST":
        banner_num = request.POST.get('banner_num', '1')
        select_name = request.POST.get('cars',None)
        if banner_num == '':
            return HttpResponse('没有输入创建数量，请返回输入！')
        else:
            banner_num = int(float(banner_num))
            for banner_num in range(1, banner_num + 1):
                if select_name == 'H5':
                    add_banner()
                    return HttpResponse(str(banner_num)+'个已上架的图文banner创建成功，快去看看吧～')
                if select_name == 'APP':
                    #add_banner()
                    return HttpResponse('暂时还没写完，请稍后再试吧～')
                if select_name == 'ARTICLE':
                    #add_banner()
                    return HttpResponse('暂时还没写完，请稍后再试吧～')



#根据创建人获取名下可用专栏
def search_special_column(request):
    creator = request.POST.get('creator','1')
    #creator = models.
    special_columns = models.SpecialColumn.objects.filter(creator=creator,type = 1,status= 1)
    #special_columns = models.SpecialColumn.objects.all()
    return render(request,'special_column.html', {'special_columns': special_columns})

def search_lecture_column(request):
    creator = request.POST.get('creator','1')
    #creator = models.
    lecture_columns = models.SpecialColumn.objects.filter(creator=creator,type = 3,status= 1)
    #special_columns = models.SpecialColumn.objects.all()
    return render(request,'lecture_column.html', {'lecture_columns': lecture_columns})


def create_columnactivity():
    title = '自动化通用专栏活动'
    status = 2
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    end_time = '2029-06-27 20:23:00'
    material_id = 3646
    material_description = '秋天来了'
    material_url = 'www.baidu.com'
    material_type = 1
    image_id = 2321
    image_url = 'https://static-xesapi.speiyou.cn/1537845631611.jpg'
    priority = 7
    creator = 80
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    activity_type = 1
    user_type = 1
    is_delete = 0
    columnactivity = models.ColumnActivity.objects.create(title=title, status=status, start_time=start_time,end_time=end_time,material_id=material_id,
                          material_description=material_description, material_url=material_url,material_type=material_type,
                          image_id=image_id,image_url=image_url,priority=priority,creator=creator,create_time=create_time,
                          update_time=update_time,activity_type=activity_type,user_type=user_type,is_delete=is_delete)
    return columnactivity.id

def create_lectureactivity():
    title = '自动创建视频活动'
    status = 2
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    end_time = '2029-06-27 20:23:00'
    material_description = '我是一个自动描述'
    material_url = 'http://lighthouse-test.xesapp.com/#/page/locationManage/columnActivity/publicLecture/editLecture?id=1162&page=1&_k=8xr4ht'
    material_type = 1
    big_image_id =2536
    big_image_url = 'https://static-xesapi.speiyou.cn/1545987949750.gif'
    small_image_id = 1431
    small_image_url = 'https://static-xesapi.speiyou.cn/1545987953596.jpg'
    priority = 2
    creator = 80
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #lecture_type =  NULL
    #user_type = NULL
    begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    video_url = 'https://lighthousevideo-online.oss-cn-beijing.aliyuncs.com/2018-12-28%2F1545987977262%2FHello+English+Plus%E5%AE%A3%E4%BC%A0%E7%89%87_01.mp4'
    is_delete = 0
    lectureactivitys = models.PublicLecture.objects.create(title=title, status=status, start_time=start_time,end_time=end_time,
                          material_description=material_description, material_url=material_url,material_type=material_type,big_image_id=big_image_id,
                          big_image_url=big_image_url,small_image_id=small_image_id,small_image_url=small_image_url,priority=priority,
                          creator=creator,create_time=create_time,update_time=update_time,
                          begin_time=begin_time,video_url=video_url,is_delete=is_delete)
    return lectureactivitys.id

#新建通用专栏活动并绑定
def create_special_column_activity(request):
    column_activity_id = str(create_columnactivity())
    column_id = request.POST.get('column_id', '535')
    models.ColumnActivityColumnId.objects.create(column_activity_id=column_activity_id, column_id=column_id)

def create_lecture_column_activity(request):
    column_activity_id = str(create_lectureactivity())
    column_id = request.POST.get('column_id', '535')
    models.ColumnActivityColumnId.objects.create(column_activity_id=column_activity_id, column_id=column_id)

#绑循环
def add_special_column_activity(request):
    activity_num = request.POST.get('activity_num','1')

    if activity_num =='':
        return HttpResponse('没有输入创建数量，请返回输入！')
    else:
        activity_num = int(float(activity_num))
        for i in range(1, activity_num + 1):
            create_special_column_activity(request)
            return HttpResponse(str(activity_num) + '个已上架的通用专栏活动创建成功，快去看看吧～')



def add_lecture_column_activity(request):
    activity_num = request.POST.get('activity_num','1')

    if activity_num =='':
        return HttpResponse('没有输入创建数量，请返回输入！')
    else:
        activity_num = int(float(activity_num))
        for i in range(1, activity_num + 1):
            create_lecture_column_activity(request)
            return HttpResponse(str(activity_num) + '个已上架的视频专栏活动创建成功，快去看看吧～')