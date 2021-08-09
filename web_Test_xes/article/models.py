# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    business_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    cover_photo_show_type = models.IntegerField(blank=True, null=True)
    cover_photo_url = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    topping = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    pic_width = models.IntegerField(blank=True, null=True)
    pic_height = models.IntegerField(blank=True, null=True)
    like_num = models.PositiveIntegerField(blank=True, null=True)
    collect_num = models.PositiveIntegerField(blank=True, null=True)
    read_num = models.PositiveIntegerField(blank=True, null=True)
    start_timestamp = models.DateTimeField(blank=True, null=True)
    content_url = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    material_id = models.BigIntegerField(blank=True, null=True)
    launch_status = models.IntegerField(blank=True, null=True)
    support_comment = models.PositiveIntegerField(blank=True, null=True)
    digest = models.CharField(max_length=128, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    source_city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleCity(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    city_code = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'article_city'


class ArticleGrade(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    grade = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'article_grade'


class ArticleTopic(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    topic = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'article_topic'


class AudioActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    first_column_title = models.CharField(max_length=30)
    second_column_title = models.CharField(max_length=30, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.CharField(max_length=20)
    content_type = models.IntegerField()
    user_type = models.IntegerField(blank=True, null=True)
    column_id = models.BigIntegerField()
    column_name = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_activity'


class AudioActivityAudio(models.Model):
    id = models.BigAutoField(primary_key=True)
    audio_activity_id = models.BigIntegerField()
    audio_id = models.BigIntegerField()
    type = models.IntegerField()
    special_type = models.CharField(max_length=30, blank=True, null=True)
    special_id = models.BigIntegerField(blank=True, null=True)
    sort_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_activity_audio'


class AudioActivityCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    audio_activity_id = models.BigIntegerField()
    city = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'audio_activity_city'


class AudioActivityGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    audio_activity_id = models.BigIntegerField()
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_activity_grade'


class AudioAlbum(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_type = models.IntegerField()
    course_title = models.CharField(max_length=255)
    course_second_title = models.CharField(max_length=255)
    category = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    required_course = models.IntegerField(blank=True, null=True)
    required_course_title = models.CharField(max_length=255, blank=True, null=True)
    course_sum = models.IntegerField()
    course_pic_little = models.CharField(max_length=255, blank=True, null=True)
    course_pic_big = models.CharField(max_length=255, blank=True, null=True)
    course_big_info = models.CharField(max_length=255, blank=True, null=True)
    course_lecturer = models.CharField(max_length=255, blank=True, null=True)
    course_lecturer_info = models.CharField(max_length=255, blank=True, null=True)
    course_desc = models.CharField(max_length=500)
    update_notice = models.CharField(max_length=255)
    update_rate = models.CharField(max_length=255)
    publish_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    creator = models.CharField(max_length=10)
    update_user = models.CharField(max_length=10)
    status = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)
    source_city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_album'


class AudioAlbumClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    period_id = models.BigIntegerField(blank=True, null=True)
    class_num = models.IntegerField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    material_id = models.BigIntegerField(blank=True, null=True)
    creator = models.CharField(max_length=10)
    update_user = models.CharField(max_length=10)
    status = models.IntegerField(blank=True, null=True)
    source_city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_album_class'


class AuthInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_id = models.CharField(max_length=255)
    app_key = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    desc = models.CharField(max_length=255)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_info'


class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.CharField(max_length=20)
    end_time = models.DateTimeField()
    material_id = models.BigIntegerField()
    material_type = models.IntegerField()
    material_description = models.CharField(max_length=255)
    priority = models.IntegerField()
    start_time = models.DateTimeField()
    status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    new_banner_image_url = models.CharField(max_length=255, blank=True, null=True)
    new_banner_image_id = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField()
    banner_type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'


class BannerCity(models.Model):
    banner = models.ForeignKey(Banner, models.DO_NOTHING, db_column='Banner_id')  # Field name made lowercase.
    city = models.CharField(max_length=11, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'banner_city'


class BannerGrade(models.Model):
    banner = models.ForeignKey(Banner, models.DO_NOTHING, db_column='Banner_id')  # Field name made lowercase.
    grade = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'banner_grade'


class ColumnActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    status = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    material_id = models.BigIntegerField()
    material_description = models.CharField(max_length=255)
    material_url = models.CharField(max_length=1024)
    material_type = models.IntegerField()
    image_id = models.BigIntegerField()
    image_url = models.CharField(max_length=255)
    priority = models.IntegerField()
    creator = models.CharField(max_length=20)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    activity_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'column_activity'


class ColumnActivityCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    column_activity = models.ForeignKey(ColumnActivity, models.DO_NOTHING)
    city = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'column_activity_city'


class ColumnActivityColumnId(models.Model):
    id = models.BigAutoField(primary_key=True)
    column_activity = models.ForeignKey(ColumnActivity, models.DO_NOTHING)
    column_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'column_activity_column_id'


class ColumnActivityGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    column_activity = models.ForeignKey(ColumnActivity, models.DO_NOTHING)
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'column_activity_grade'


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255)
    update_time = models.TextField(blank=True, null=True)
    height = models.IntegerField()
    type = models.IntegerField()
    url = models.CharField(max_length=255)
    width = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    source_city = models.CharField(max_length=10, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


class Material(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=10)
    update_time = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    url = models.TextField()
    update_user = models.CharField(max_length=10)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    material_tag = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    source_city = models.CharField(max_length=10, blank=True, null=True)
    cover_image = models.TextField(blank=True, null=True)
    check_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'material'


class MaterialActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    material_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    activity_type = models.IntegerField()
    is_delete = models.IntegerField()
    material_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'material_activity'


class MaterialTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    material_id = models.BigIntegerField()
    tag_id = models.BigIntegerField()
    belong_type = models.IntegerField()
    creator = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'material_tag'


class PublicLecture(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    status = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    material_description = models.CharField(max_length=255)
    material_url = models.CharField(max_length=1024)
    material_type = models.IntegerField()
    big_image_id = models.BigIntegerField()
    big_image_url = models.CharField(max_length=255)
    small_image_id = models.BigIntegerField()
    small_image_url = models.CharField(max_length=255)
    priority = models.IntegerField()
    creator = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    lecture_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_lecture'


class PublicLectureCity(models.Model):
    public_lecture = models.ForeignKey(PublicLecture, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'public_lecture_city'


class PublicLectureColumnId(models.Model):
    public_lecture = models.ForeignKey(PublicLecture, models.DO_NOTHING)
    column_id = models.BigIntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'public_lecture_column_id'


class PublicLectureGrade(models.Model):
    public_lecture = models.ForeignKey(PublicLecture, models.DO_NOTHING)
    grade = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'public_lecture_grade'


class SpecialActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    image_id = models.BigIntegerField()
    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=30)
    special_id = models.BigIntegerField()
    column_id = models.BigIntegerField()
    column_name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    priority = models.IntegerField()
    creator = models.CharField(max_length=20)
    content_type = models.IntegerField()
    user_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_activity'


class SpecialActivityCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    special_activity_id = models.BigIntegerField()
    city = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'special_activity_city'


class SpecialActivityGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    special_activity_id = models.BigIntegerField()
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_activity_grade'


class SpecialColumn(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    creator = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_column'


class SpecialColumnCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    special_column = models.ForeignKey(SpecialColumn, models.DO_NOTHING)
    city_code = models.CharField(max_length=11)
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'special_column_city'


class SpecialColumnGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    special_column = models.ForeignKey(SpecialColumn, models.DO_NOTHING)
    grd_id = models.IntegerField()
    grd_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'special_column_grade'


class Tag(models.Model):
    tag_id = models.BigAutoField(primary_key=True)
    tag_name = models.CharField(max_length=8, blank=True, null=True)
    tag_type = models.IntegerField()
    parent_id = models.IntegerField()
    author = models.CharField(max_length=50, blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.IntegerField()


    def __str__(self):  # 增加该方法
        return self.tag_name

    class Meta:
        managed = False
        db_table = 'tag'
