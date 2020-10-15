# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Distributor(models.Model):
    distributorname = models.CharField(db_column='DistributorName', primary_key=True, max_length=10)  # Field name made lowercase.
    distributortelephone = models.CharField(db_column='DistributorTelephone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    storing = models.CharField(db_column='Storing', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distributor'


class Firm(models.Model):
    firmno = models.CharField(db_column='FirmNo', primary_key=True, max_length=10)  # Field name made lowercase.
    firmname = models.CharField(db_column='FirmName', max_length=10)  # Field name made lowercase.
    firmtelephone = models.CharField(db_column='FirmTelephone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    firmemail = models.CharField(db_column='FirmEmail', max_length=12, blank=True, null=True)  # Field name made lowercase.
    firmaddress = models.CharField(db_column='FirmAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firm'


class Plant(models.Model):
    plantationno = models.ForeignKey('Plantation', models.DO_NOTHING, db_column='PlantationNo', primary_key=True)  # Field name made lowercase.
    seedno = models.ForeignKey('Seed', models.DO_NOTHING, db_column='SeedNo')  # Field name made lowercase.
    planting = models.DateTimeField(db_column='Planting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant'
        unique_together = (('plantationno', 'seedno'),)


class Plantation(models.Model):
    plantationno = models.CharField(db_column='PlantationNo', primary_key=True, max_length=10)  # Field name made lowercase.
    plantationname = models.CharField(db_column='PlantationName', max_length=10)  # Field name made lowercase.
    plantationtelephone = models.CharField(db_column='PlantationTelephone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    plantationaddress = models.CharField(db_column='PlantationAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plantation'


class Process(models.Model):
    plantationno = models.ForeignKey(Plantation, models.DO_NOTHING, db_column='PlantationNo', primary_key=True)  # Field name made lowercase.
    productno = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductNo')  # Field name made lowercase.
    firmno = models.ForeignKey(Firm, models.DO_NOTHING, db_column='FirmNo')  # Field name made lowercase.
    acquisition = models.DateTimeField(db_column='Acquisition', blank=True, null=True)  # Field name made lowercase.
    processing = models.CharField(db_column='Processing', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packing = models.DateTimeField(db_column='Packing', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'process'
        unique_together = (('plantationno', 'productno', 'firmno'),)


class Product(models.Model):
    productno = models.CharField(db_column='ProductNo', primary_key=True, max_length=10)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=10)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Provide(models.Model):
    firmno = models.ForeignKey(Firm, models.DO_NOTHING, db_column='FirmNo', primary_key=True)  # Field name made lowercase.
    productno = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductNo')  # Field name made lowercase.
    distrbutorname = models.ForeignKey(Distributor, models.DO_NOTHING, db_column='DistrbutorName')  # Field name made lowercase.
    stock = models.DateTimeField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provide'
        unique_together = (('firmno', 'productno', 'distrbutorname'),)


class Seed(models.Model):
    seedno = models.CharField(db_column='SeedNo', primary_key=True, max_length=10)  # Field name made lowercase.
    its1 = models.CharField(db_column='ITS1', max_length=50)  # Field name made lowercase.
    its2 = models.CharField(db_column='ITS2', max_length=50)  # Field name made lowercase.
    rcrrelf = models.CharField(db_column='RCRRELF', max_length=50)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=5, blank=True, null=True)  # Field name made lowercase.
    support = models.CharField(db_column='Support', max_length=10, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seed'


class Sell(models.Model):
    productno = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductNo', primary_key=True)  # Field name made lowercase.
    distrbutorname = models.ForeignKey(Distributor, models.DO_NOTHING, db_column='DistrbutorName')  # Field name made lowercase.
    storename = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreName')  # Field name made lowercase.
    purchase = models.DateTimeField(db_column='Purchase', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sell'
        unique_together = (('productno', 'distrbutorname', 'storename'),)


class Store(models.Model):
    storename = models.CharField(db_column='StoreName', primary_key=True, max_length=10)  # Field name made lowercase.
    storetelephone = models.CharField(db_column='StoreTelephone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    storeaddress = models.CharField(db_column='StoreAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'

