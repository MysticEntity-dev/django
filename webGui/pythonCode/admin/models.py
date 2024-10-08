# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Villages(models.Model):
    village_id = models.BigAutoField(primary_key=True)
    owner = models.IntegerField()
    world = models.ForeignKey('World', models.DO_NOTHING, db_column='world')
    abandoned = models.IntegerField()
    palast = models.IntegerField()
    farm = models.IntegerField()
    mine = models.IntegerField()
    clay_pit = models.IntegerField()
    timber_camp = models.IntegerField()
    wall = models.IntegerField()
    village_center = models.IntegerField()
    warehouse = models.IntegerField()
    statue = models.IntegerField()
    barracks = models.IntegerField()
    workshop = models.IntegerField()
    smithy = models.IntegerField()
    stable = models.IntegerField()
    manor = models.IntegerField()
    market = models.IntegerField()
    church = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'villages'


class World(models.Model):
    speed = models.SmallIntegerField(blank=True, null=True)
    modus = models.CharField(max_length=50, blank=True, null=True)
    win_con = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world'
