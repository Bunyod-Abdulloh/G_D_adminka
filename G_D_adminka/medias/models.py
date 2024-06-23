from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True, default=1)

    def __str__(self):
        return f"{self.id}.{self.telegram_id} - {self.full_name}"


class BaseLessonModel(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", primary_key=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=150, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=150, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=150, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=150, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.TextField(verbose_name="Tavsif", max_length=4000, null=True)

    class Meta:
        abstract = True


class Table1(BaseLessonModel):
    class Meta:
        verbose_name = 'Psixoterapiya va psixologiya asoslari'
        verbose_name_plural = 'Psixoterapiya va psixologiya asoslari'


class Table2(BaseLessonModel):
    class Meta:
        verbose_name = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'
        verbose_name_plural = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'


class Table3(BaseLessonModel):
    class Meta:
        verbose_name = 'Miyaning neyroplastikligi va neyrobika'
        verbose_name_plural = 'Miyaning neyroplastikligi va neyrobika'


class Table4(BaseLessonModel):
    class Meta:
        verbose_name = 'Ta\'lim va ruhiyat'
        verbose_name_plural = 'Ta\'lim va ruhiyat'


class Table5(BaseLessonModel):
    class Meta:
        verbose_name = 'Farzandim va jigarbandim'
        verbose_name_plural = 'Farzandim va jigarbandim'


class Table6(BaseLessonModel):
    class Meta:
        verbose_name = 'Nafs diagnostikasi'
        verbose_name_plural = 'Nafs diagnostikasi'


class Table7(BaseLessonModel):
    class Meta:
        verbose_name = 'Sharq psixologiyasi va psixoterapiya'
        verbose_name_plural = 'Sharq psixologiyasi va psixoterapiya'


class Table8(BaseLessonModel):
    class Meta:
        verbose_name = 'Ruhiy salomatlik'
        verbose_name_plural = 'Ruhiy salomatlik'


class Table9(models.Model):
    sequence = models.IntegerField(verbose_name="Tartib raqami")
    audio_id = models.CharField(verbose_name="Audio ID", max_length=150, blank=True)
    photo_id = models.CharField(verbose_name="Photo ID", max_length=150, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=150, blank=True)
    voice_id = models.CharField(verbose_name="Voice ID", max_length=150, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=150, blank=True)
    category = models.CharField(verbose_name="Kategoriya", max_length=150, null=True)
    subcategory = models.CharField(verbose_name="Subkategoriya", max_length=150, null=True)
    caption = models.TextField(verbose_name="Tavsif", null=True)
    link = models.CharField(verbose_name="Youtube link", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Suhbat va loyihalar'
        verbose_name_plural = 'Suhbat va loyihalar'


class Table10(models.Model):
    id = models.AutoField(verbose_name="Tartib raqami", primary_key=True)
    file_name = models.CharField(verbose_name="Maqola nomi", max_length=150, null=True)
    link = models.CharField(verbose_name="Maqola linki", max_length=150, null=True)

    class Meta:
        verbose_name = 'Maqolalar'
        verbose_name_plural = 'Maqolalar'


class Tables(models.Model):
    table_number = models.IntegerField(verbose_name='Tartib raqami:', primary_key=True, null=False)
    table_name = models.CharField(verbose_name='Nomi:', max_length=200, null=True)
    table_type = models.CharField(verbose_name='Turi:', max_length=100, null=True)
    channel_id = models.CharField(verbose_name='Kanal ID raqami:', max_length=150, null=True, blank=True)
    comment = models.TextField(verbose_name='Izohlar:', null=True, blank=True)
    files = models.BooleanField(verbose_name='Fayllar yuklangan bo\'lsa katakchani belgilab qo\'ying',
                                default=False)

    class Meta:
        verbose_name = 'Dars va kurslar jadvali'
        verbose_name_plural = 'Dars va kurslar jadvali'
