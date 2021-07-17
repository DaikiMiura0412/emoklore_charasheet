from django.db import models


class CharacterData(models.Model):
    name = models.CharField('名前',max_length=255)
    pl = models.CharField('PL',max_length=255)
    kyomei_level = models.IntegerField('共鳴レベル',default=1)
    kyomei_omote = models.CharField('共鳴感情(表)',max_length=255)
    kyomei_ura = models.CharField('共鳴感情(裏)',max_length=255)
    kyomei_root = models.CharField('共鳴感情(ルーツ)',max_length=255)
    shintai = models.IntegerField('身体')
    kiyou = models.IntegerField('器用')
    seishin = models.IntegerField('精神')
    gokan = models.IntegerField('語感')
    chiryoku = models.IntegerField('知力')
    miryoku = models.IntegerField('魅力')
    shakai = models.IntegerField('社会')
    unsei = models.IntegerField('運勢')
    age = models.IntegerField('年齢')
    gender = models.CharField('性別',max_length=255)
    occupation = models.CharField('職業',max_length=255)
    shusshin = models.CharField('出身',max_length=255)
    hp = models.IntegerField('HP')
    mp = models.IntegerField('MP')
    chat_pallet = models.CharField('チャパレ',max_length=255)

    def __str__(self):
        return self.name