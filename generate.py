# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Arlos(models.Model):
    carlos = models.IntegerField(primary_key=True)
    cbarras = models.CharField(max_length=50)
    cgpo = models.ForeignKey('Gpos', models.DO_NOTHING, db_column='cgpo')
    ncorto = models.CharField(max_length=20)
    nlargo = models.CharField(max_length=100)
    canti = models.DecimalField(max_digits=15, decimal_places=2)
    vcosto = models.DecimalField(max_digits=15, decimal_places=2)
    ifcostear = models.CharField(max_length=1)
    ifpvfijo = models.CharField(max_length=1)
    cesdo = models.ForeignKey('Esdos', models.DO_NOTHING, db_column='cesdo')
    ciudad = models.ForeignKey('Ciudades', models.DO_NOTHING, db_column='ciudad')
    ivas_civa = models.ForeignKey('Ivas', models.DO_NOTHING, db_column='ivas_civa')
    stomin = models.DecimalField(max_digits=15, decimal_places=2)
    stomax = models.DecimalField(max_digits=15, decimal_places=2)
    pvta1 = models.DecimalField(max_digits=15, decimal_places=2)
    pvta2 = models.DecimalField(max_digits=15, decimal_places=2)
    pvta3 = models.DecimalField(max_digits=15, decimal_places=2)
    pvta4 = models.DecimalField(max_digits=15, decimal_places=2)
    pvta5 = models.DecimalField(max_digits=15, decimal_places=2)
    pvta6 = models.DecimalField(max_digits=15, decimal_places=2)
    citerce1 = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce1')
    vcosto1 = models.DecimalField(max_digits=15, decimal_places=2)
    fcosto1 = models.DateField()
    citerce2 = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce2')
    vcosto2 = models.DecimalField(max_digits=15, decimal_places=2)
    fcosto2 = models.DateField()
    citerce3 = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce3')
    vcosto3 = models.DecimalField(max_digits=15, decimal_places=2)
    fcosto3 = models.DateField()
    ifedinom = models.CharField(max_length=1)
    refe = models.CharField(max_length=20)
    cmarca = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='cmarca')
    ifdesglo = models.CharField(max_length=1)
    mesesgara = models.IntegerField()
    cubica = models.ForeignKey('Ubica', models.DO_NOTHING, db_column='cubica')
    porult1 = models.DecimalField(max_digits=6, decimal_places=2)
    porult2 = models.DecimalField(max_digits=6, decimal_places=2)
    porult3 = models.DecimalField(max_digits=6, decimal_places=2)
    porult4 = models.DecimalField(max_digits=6, decimal_places=2)
    porult5 = models.DecimalField(max_digits=6, decimal_places=2)
    porult6 = models.DecimalField(max_digits=6, decimal_places=2)
    foto1 = models.CharField(max_length=250, blank=True, null=True)
    foto2 = models.CharField(max_length=250, blank=True, null=True)
    foto3 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arlos'


class Arlosdesglo(models.Model):
    carlosp = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlosp')
    itglo = models.CharField(max_length=4)
    carlosglo = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlosglo')
    cantiglo = models.DecimalField(max_digits=15, decimal_places=2)
    costoglo = models.DecimalField(max_digits=15, decimal_places=2)
    vtoglo = models.DecimalField(max_digits=15, decimal_places=2)
    cesdo = models.ForeignKey('Esdos', models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'arlosdesglo'
        unique_together = (('carlosp', 'itglo'),)


class Autorre(models.Model):
    cautorre = models.AutoField(primary_key=True)
    nautorre = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'autorre'


class Bode(models.Model):
    cbode = models.AutoField(primary_key=True)
    nbode = models.CharField(max_length=80)
    esbode = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'bode'


class Ciudades(models.Model):
    cciu = models.AutoField(primary_key=True)
    nciu = models.CharField(max_length=40)
    cdepar = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='cdepar')

    class Meta:
        managed = False
        db_table = 'ciudades'


class Departamentos(models.Model):
    cdepar = models.AutoField(primary_key=True)
    ndepar = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Esdos(models.Model):
    cesdo = models.AutoField(primary_key=True)
    nesdo = models.CharField(max_length=40)
    estavali = models.CharField(max_length=10)
    colfon = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'esdos'


class Gpos(models.Model):
    cgpo = models.IntegerField(primary_key=True)
    ngpo = models.CharField(max_length=80)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'gpos'


class Invinicab(models.Model):
    cii = models.AutoField(primary_key=True)
    fii = models.DateTimeField()
    fuaii = models.DateTimeField()
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'invinicab'


class Invinideta(models.Model):
    cii = models.ForeignKey(Invinicab, models.DO_NOTHING, db_column='cii')
    carlos = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlos')
    nlargo = models.CharField(max_length=100)
    canti = models.DecimalField(max_digits=15, decimal_places=2)
    vunita = models.DecimalField(max_digits=15, decimal_places=2)
    vtotal = models.DecimalField(max_digits=15, decimal_places=2)
    cancalcu = models.DecimalField(max_digits=15, decimal_places=2)
    ajuent = models.DecimalField(max_digits=15, decimal_places=2)
    ajusal = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'invinideta'
        unique_together = (('carlos', 'cii'),)


class Ivas(models.Model):
    civa = models.AutoField(primary_key=True)
    niva = models.CharField(max_length=40)
    poriva = models.DecimalField(max_digits=6, decimal_places=2)
    idtira = models.CharField(max_length=1)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'ivas'


class Marcas(models.Model):
    cmarca = models.AutoField(primary_key=True)
    nmarca = models.CharField(max_length=60)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'marcas'


class Mven(models.Model):
    cmven = models.AutoField(primary_key=True)
    fmven = models.DateTimeField()
    docrefe = models.CharField(max_length=10)
    citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
    ctimo = models.ForeignKey('Timo', models.DO_NOTHING, db_column='ctimo')
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
    vttotal = models.DecimalField(max_digits=15, decimal_places=2)
    descri = models.CharField(max_length=250)
    detaanula = models.CharField(max_length=250)
    cbode0 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode0')
    cbode1 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode1')

    class Meta:
        managed = False
        db_table = 'mven'


class Mvendeta(models.Model):
    cmven = models.ForeignKey(Mven, models.DO_NOTHING, db_column='cmven')
    it = models.CharField(max_length=4)
    carlos = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlos')
    nlargo = models.CharField(max_length=100)
    canti = models.DecimalField(max_digits=15, decimal_places=2)
    vunita = models.DecimalField(max_digits=15, decimal_places=2)
    vtotal = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'mvendeta'
        unique_together = (('cmven', 'it'),)


class Mvsa(models.Model):
    cmvsa = models.AutoField(primary_key=True)
    fmvsa = models.DateTimeField()
    docrefe = models.CharField(max_length=10)
    citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
    ctimo = models.ForeignKey('Timo', models.DO_NOTHING, db_column='ctimo')
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
    vttotal = models.DecimalField(max_digits=15, decimal_places=2)
    descri = models.CharField(max_length=250)
    detaanula = models.CharField(max_length=250)
    cbode0 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode0')
    cbode1 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode1')

    class Meta:
        managed = False
        db_table = 'mvsa'


class Mvsadeta(models.Model):
    cmvsa = models.ForeignKey(Mvsa, models.DO_NOTHING, db_column='cmvsa')
    it = models.CharField(max_length=4)
    citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
    nlargo = models.CharField(max_length=100)
    canti = models.DecimalField(max_digits=15, decimal_places=2)
    vunita = models.DecimalField(max_digits=15, decimal_places=2)
    vtotal = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'mvsadeta'
        unique_together = (('cmvsa', 'it'),)


class Regiva(models.Model):
    cregiva = models.AutoField(primary_key=True)
    nregiva = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'regiva'


class Rutas(models.Model):
    cruta = models.AutoField(primary_key=True)
    nruta = models.CharField(max_length=45)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'rutas'


class Terceros(models.Model):
    citerce = models.AutoField(primary_key=True)
    idterce = models.CharField(max_length=20)
    dv = models.CharField(max_length=1)
    ctiide = models.ForeignKey('Tiide', models.DO_NOTHING, db_column='ctiide')
    rasocial = models.CharField(max_length=200)
    nomcomer = models.CharField(max_length=200)
    ape1 = models.CharField(max_length=40)
    ape2 = models.CharField(max_length=40)
    nom1 = models.CharField(max_length=40)
    nom2 = models.CharField(max_length=40)
    sigla = models.CharField(max_length=100)
    nomegre = models.CharField(max_length=100)
    replegal = models.CharField(max_length=100)
    dirterce = models.CharField(max_length=80)
    telterce = models.CharField(max_length=20)
    faxterce = models.CharField(max_length=20)
    cciu = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='cciu')
    email = models.CharField(max_length=40)
    contacto = models.CharField(max_length=20)
    cregiva = models.ForeignKey(Regiva, models.DO_NOTHING, db_column='cregiva')
    cautorre = models.ForeignKey(Autorre, models.DO_NOTHING, db_column='cautorre')
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
    cvende = models.ForeignKey('Vende', models.DO_NOTHING, db_column='cvende')
    topcxc = models.DecimalField(max_digits=15, decimal_places=2)
    ndiacxc = models.IntegerField()
    czona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='czona')
    clipre = models.IntegerField()
    fnaci = models.DateField()
    naju = models.IntegerField()
    cruta = models.ForeignKey(Rutas, models.DO_NOTHING, db_column='cruta')
    ordenruta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'terceros'


class Tiide(models.Model):
    idtiide = models.AutoField(primary_key=True)
    ntiide = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tiide'


class Timo(models.Model):
    ctimo = models.IntegerField(primary_key=True)
    ntimo = models.CharField(max_length=40)
    prefijo = models.CharField(max_length=4)
    filas = models.IntegerField()
    nrepo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timo'


class Ubica(models.Model):
    cubica = models.AutoField(primary_key=True)
    nubica = models.CharField(max_length=80)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'ubica'


class Vende(models.Model):
    cvende = models.AutoField(primary_key=True)
    nvende = models.CharField(max_length=80)
    porventa = models.DecimalField(max_digits=7, decimal_places=4)
    cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

    class Meta:
        managed = False
        db_table = 'vende'


class Zonas(models.Model):
    czona = models.AutoField(primary_key=True)
    nzona = models.CharField(max_length=40)
    activo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'zonas'
