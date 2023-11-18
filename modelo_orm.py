from peewee import *
# from gestionar_obras import *

sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class EntornoF(BaseModel):
    id = PrimaryKeyField()
    nombreEntorno = CharField(unique=True)
    def __str__(self):
        return self.nombreEntorno
    class Meta:
        db_table = "EntornoF"


class ObrasPublicas(BaseModel):
    ID = PrimaryKeyField()
    entorno = ForeignKeyField(EntornoF, backref="entorno")
    nombre = CharField(max_length=80)
    etapa = CharField(max_length=15)
    tipo = CharField(max_length=80)
    area_responsable = CharField(max_length=60)
    descripcion = CharField(max_length=255)
    monto_contrato = IntegerField()
    comuna = IntegerField()
    barrio = CharField(max_length=50)
    direccion = CharField(max_length=80)
    lat = CharField(max_length=20)
    lng = CharField(max_length=20)
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = FloatField()
    porcentaje_avance = FloatField()
    licitacion_oferta_empresa = CharField(max_length=60)
    licitacion_anio = IntegerField()
    contratacion_tipo = CharField(max_length=60)
    nro_contratacion = CharField(max_length=60)
    cuit_contratista = IntegerField()
    beneficiarios = CharField(max_length=60)
    mano_obra = CharField(max_length=40)
    compromiso = CharField(max_length=3)
    destacada = CharField(max_length=3)
    ba_elige = CharField(max_length=3)
    link_interno = CharField(max_length=80)
    pliego_descarga = CharField(max_length=80)
    expediente_numero = CharField(max_length=80)
    estudio_ambiental_descarga = CharField(max_length=80)
    financiamiento = CharField(max_length=20)
    def __str__(self):
        pass
    class meta:
        db_table = 'DatosObra'




