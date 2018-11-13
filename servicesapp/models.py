# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountingArea(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounting_area'


class Activities(models.Model):
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING)
    activitytype = models.ForeignKey('Activitytype', models.DO_NOTHING)
    contact = models.CharField(max_length=255, blank=True, null=True)
    comment_start_activity = models.CharField(max_length=255, blank=True, null=True)
    error_description = models.CharField(max_length=255, blank=True, null=True)
    serviceprovider = models.ForeignKey('Addresses', models.DO_NOTHING, blank=True, null=True, related_name='serviceprovider_Activities_set')
    offer_requested_date = models.DateField(blank=True, null=True)
    offer_date = models.DateField(blank=True, null=True)
    offer_number = models.CharField(max_length=32, blank=True, null=True)
    offer_position = models.CharField(max_length=32, blank=True, null=True)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    costcenter = models.ForeignKey('Costcenter', models.DO_NOTHING, blank=True, null=True)
    group_po_number = models.CharField(max_length=32, blank=True, null=True)
    rma_number = models.CharField(max_length=32, blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    deliveryaddress = models.ForeignKey('Addresses', models.DO_NOTHING, blank=True, null=True, related_name='deliveryaddress_Activities_set')
    expected_return_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    comment_progress = models.CharField(max_length=255, blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    offer_price_curr = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities'


class Activitytype(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activitytype'


class Addresses(models.Model):
    companyname = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=32)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    tel = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    contact_type = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'
        unique_together = (('companyname', 'department'),)


class Advatestmanager(models.Model):
    active_in_use = models.BooleanField()
    foldername = models.CharField(max_length=255)
    req_folder = models.BooleanField()
    copy_folderfiles = models.BooleanField()
    settingfiles = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey('Model', models.DO_NOTHING, blank=True, null=True, related_name='model_Advatestmanager_set')
    reg_found = models.BooleanField(blank=True, null=True)
    one_license_per_station = models.BooleanField(blank=True, null=True)
    software_req = models.BooleanField(blank=True, null=True)
    software_group = models.IntegerField(blank=True, null=True)
    software_default = models.BooleanField(blank=True, null=True)
    other_software_req = models.ForeignKey('Model', models.DO_NOTHING, db_column='other_software_req', blank=True, null=True, related_name='other_software_req_Advatestmanager_set')
    install_file = models.CharField(max_length=64, blank=True, null=True)
    bin_name = models.CharField(max_length=255, blank=True, null=True)
    innerapp_settings = models.CharField(max_length=255, blank=True, null=True)
    autostart = models.CharField(max_length=255, blank=True, null=True)
    desktop = models.CharField(max_length=255, blank=True, null=True)
    windowsservice = models.CharField(max_length=32, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    installorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advatestmanager'


class Applicant(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'applicant'


class BlacklistCf(models.Model):
    vendor = models.CharField(max_length=32)
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blacklist_cf'


class Calibrationinterval(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calibrationinterval'


class Cardfamily(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    macn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardfamily'


class Cardtype(models.Model):
    description = models.CharField(unique=True, max_length=32)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cardtype'


class Contactperson(models.Model):
    addresses = models.ForeignKey(Addresses, models.DO_NOTHING)
    role_function = models.CharField(max_length=255)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    tel1 = models.CharField(max_length=32, blank=True, null=True)
    tel2 = models.CharField(max_length=32, blank=True, null=True)
    tel3 = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    department_team = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactperson'


class Costcenter(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    description = models.CharField(max_length=255)
    contactperson = models.ForeignKey(Contactperson, models.DO_NOTHING)
    equipmentsite = models.ForeignKey('Equipmentsite', models.DO_NOTHING)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    accounting_area = models.ForeignKey(AccountingArea, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costcenter'


class Countryoforigin(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(unique=True, max_length=100)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'countryoforigin'


class Customer(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


class Deliverycondition(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'deliverycondition'


class Devicecondition(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'devicecondition'


class Document(models.Model):
    documenttype = models.ForeignKey('Documenttype', models.DO_NOTHING)
    docname = models.CharField(max_length=255)
    doclanguage = models.CharField(max_length=3)
    docid_agile = models.CharField(max_length=16, blank=True, null=True)
    revnr_agile = models.CharField(max_length=16, blank=True, null=True)
    where_saved = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class Documenttype(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documenttype'


class EepromDvEnums(models.Model):
    name = models.CharField(primary_key=True, max_length=256)
    value = models.BigIntegerField()
    groupname = models.ForeignKey('EepromDvGroups', models.DO_NOTHING, db_column='groupname')
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eeprom_dv_enums'
        unique_together = (('name', 'groupname'),)


class EepromDvGroups(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eeprom_dv_groups'


class EepromMapping(models.Model):
    partnr = models.CharField(max_length=32)
    partnr_sap = models.CharField(max_length=32)
    hwrev = models.CharField(max_length=32)
    hwrev_hidden = models.CharField(max_length=32)
    productfamily = models.ForeignKey('Productfamily', models.DO_NOTHING)
    cardfamily = models.ForeignKey(Cardfamily, models.DO_NOTHING)
    moduletypename = models.CharField(max_length=32, blank=True, null=True)
    unitname = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    eeprom_template = models.ForeignKey('EepromTemplate', models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eeprom_mapping'
        unique_together = (('cardfamily', 'partnr_sap', 'hwrev', 'hwrev_hidden'),)


class EepromTemplate(models.Model):
    partnr = models.CharField(max_length=32)
    hwrev = models.CharField(max_length=8)
    hwrev_hidden = models.CharField(max_length=8)
    eeprom_filename = models.CharField(max_length=256)
    cardtype = models.ForeignKey(Cardtype, models.DO_NOTHING, blank=True, null=True)
    moduletypename = models.CharField(max_length=32, blank=True, null=True)
    unitname = models.CharField(max_length=32, blank=True, null=True)
    vendid = models.CharField(max_length=32, blank=True, null=True)
    clei = models.CharField(max_length=32, blank=True, null=True)
    pcbtype = models.CharField(max_length=8, blank=True, null=True)
    pcbassemblyext = models.CharField(max_length=8, blank=True, null=True)
    pcbtypeext = models.CharField(max_length=8, blank=True, null=True)
    hwrev_ext = models.CharField(max_length=8, blank=True, null=True)
    board_dimensions = models.CharField(max_length=8, blank=True, null=True)
    maxpower = models.CharField(max_length=8, blank=True, null=True)
    maxpower2 = models.CharField(max_length=8, blank=True, null=True)
    reserved1 = models.CharField(max_length=32, blank=True, null=True)
    reserved2 = models.CharField(max_length=32, blank=True, null=True)
    reserved3 = models.CharField(max_length=32, blank=True, null=True)
    reserved4 = models.CharField(max_length=32, blank=True, null=True)
    bin_data1a = models.CharField(max_length=257, blank=True, null=True)
    bin_data1b = models.CharField(max_length=257, blank=True, null=True)
    bin_data2a = models.CharField(max_length=257, blank=True, null=True)
    bin_data2b = models.CharField(max_length=257, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eeprom_template'
        unique_together = (('partnr', 'hwrev', 'hwrev_hidden', 'eeprom_filename'),)


class Equipment(models.Model):
    model = models.ForeignKey('Model', models.DO_NOTHING)
    serialnumber = models.CharField(max_length=32, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    group_po_number = models.CharField(max_length=32, blank=True, null=True)
    id_number_old = models.CharField(max_length=32, blank=True, null=True)
    asset_number = models.CharField(max_length=32, blank=True, null=True)
    warranty_to = models.DateField(blank=True, null=True)
    calibration_paid_to = models.DateField(blank=True, null=True)
    accessories = models.CharField(max_length=255, blank=True, null=True)
    equipmentstatus = models.ForeignKey('Equipmentstatus', models.DO_NOTHING)
    diverse_number_old = models.CharField(max_length=32, blank=True, null=True)
    costcenter = models.ForeignKey(Costcenter, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    part_of_equip = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    matingcycles_max = models.IntegerField(blank=True, null=True)
    multiple_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment'
        unique_together = (('model', 'serialnumber'),)


class EquipmentCalibration(models.Model):
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    cal_date = models.DateField()
    cal_due_date = models.DateField(blank=True, null=True)
    cal_laboratory = models.ForeignKey(Addresses, models.DO_NOTHING)
    devicecond_received = models.ForeignKey(Devicecondition, models.DO_NOTHING, related_name='devicecond_received_EquipmentCalibration_set')
    devicecond_returned = models.ForeignKey(Devicecondition, models.DO_NOTHING, related_name='devicecond_returned_EquipmentCalibration_set')
    certificate_number = models.CharField(max_length=32)
    certificate = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipment_calibration'


class EquipmentCalibrationinterval(models.Model):
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    cal_liable = models.BooleanField(blank=True, null=True)
    calibrationinterval = models.ForeignKey(Calibrationinterval, models.DO_NOTHING, blank=True, null=True)
    change_comment = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipment_calibrationinterval'


class Equipmentsite(models.Model):
    description = models.CharField(unique=True, max_length=255)
    equipmentsite_admin = models.ForeignKey('EquipmentsiteAdmin', models.DO_NOTHING)
    addresses = models.ForeignKey(Addresses, models.DO_NOTHING)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipmentsite'


class EquipmentsiteAdmin(models.Model):
    description = models.CharField(max_length=255)
    responsible = models.ForeignKey(Contactperson, models.DO_NOTHING, related_name='responsible_EquipmentsiteAdmin_set')
    deputy = models.ForeignKey(Contactperson, models.DO_NOTHING, blank=True, null=True, related_name='deputy_EquipmentsiteAdmin_set')
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipmentsite_admin'


class Equipmentstatus(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipmentstatus'


class Errortype(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'errortype'


class Figo(models.Model):
    figonr = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    productfamily = models.ForeignKey('Productfamily', models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    cardfamily = models.ForeignKey(Cardfamily, models.DO_NOTHING, blank=True, null=True)
    test_tc_client_prompt = models.CharField(max_length=32, blank=True, null=True)
    tc_client_prompt = models.CharField(max_length=32, blank=True, null=True)
    fwp_pak_file_name = models.CharField(max_length=255, blank=True, null=True)
    programming_time_fwp = models.CharField(max_length=32, blank=True, null=True)
    programming_time_ptest = models.CharField(max_length=32, blank=True, null=True)
    programming_time_ptest_r = models.CharField(max_length=32, blank=True, null=True)
    boot_up_time_fwp = models.CharField(max_length=32, blank=True, null=True)
    boot_up_time_reduced = models.CharField(max_length=32, blank=True, null=True)
    slot_connection_position = models.CharField(max_length=32, blank=True, null=True)
    matingcycles_max = models.IntegerField(blank=True, null=True)
    productgroup = models.ForeignKey('Productgroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'figo'


class FigoDocuments(models.Model):
    figo_figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figo_figonr', blank=True, null=True)
    document = models.ForeignKey(Document, models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'figo_documents'


class FigoSettings(models.Model):
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    tablename = models.ForeignKey('SettingNaming', models.DO_NOTHING, db_column='tablename')
    fieldname = models.CharField(max_length=32)
    value = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=8)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'figo_settings'
        unique_together = (('figonr', 'fieldname'),)


class FigoWorkstep(models.Model):
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    workstep = models.ForeignKey('Workstep', models.DO_NOTHING)
    worksteporder = models.IntegerField()
    sequencefile = models.CharField(max_length=255)
    optional = models.BooleanField()
    limitfile = models.CharField(max_length=255, blank=True, null=True)
    spectable = models.CharField(max_length=255, blank=True, null=True)
    resulttable = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    worksteporder_back = models.IntegerField(blank=True, null=True)
    active_in_use = models.BooleanField()
    wipcheck_from = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'figo_workstep'
        unique_together = (('figonr', 'worksteporder'),)


class Locations(models.Model):
    description = models.CharField(unique=True, max_length=255)
    ip_address = models.CharField(max_length=32)
    port = models.CharField(max_length=32)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    active = models.BooleanField()
    db = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class MacaddressGlobal(models.Model):
    macaddress_start = models.TextField(unique=True)  # This field type is a guess.
    macaddress_end = models.TextField(unique=True)  # This field type is a guess.
    macaddress_warnlevel = models.TextField(unique=True)  # This field type is a guess.
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_global'


class MacaddressLicenses(models.Model):
    macaddress = models.ForeignKey('MacaddressSn', models.DO_NOTHING, db_column='macaddress', primary_key=True)
    tablename = models.ForeignKey('SettingNaming', models.DO_NOTHING, db_column='tablename')
    fieldname = models.CharField(max_length=32)
    value = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=8)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_licenses'
        unique_together = (('macaddress', 'fieldname', 'valid_from'),)


class MacaddressOwner(models.Model):
    contactperson = models.ForeignKey(Contactperson, models.DO_NOTHING)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_owner'


class MacaddressRange(models.Model):
    macaddress_global = models.ForeignKey(MacaddressGlobal, models.DO_NOTHING)
    macaddress_start = models.TextField(unique=True)  # This field type is a guess.
    quantity_macaddresses = models.IntegerField()
    macaddress_end = models.TextField(unique=True)  # This field type is a guess.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    productphase = models.ForeignKey('Productphase', models.DO_NOTHING)
    macaddress_owner = models.ForeignKey(MacaddressOwner, models.DO_NOTHING)
    applicant = models.ForeignKey(Applicant, models.DO_NOTHING)
    email_info = models.CharField(max_length=1000)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_range'


class MacaddressSn(models.Model):
    macaddress = models.TextField(primary_key=True)  # This field type is a guess.
    serialnr = models.CharField(max_length=32)
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    macaddress_global = models.ForeignKey(MacaddressGlobal, models.DO_NOTHING)
    station = models.ForeignKey('Station', models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_sn'


class MacaddressWarningmail(models.Model):
    macaddress = models.TextField(primary_key=True)  # This field type is a guess.
    email_address = models.CharField(max_length=1000)
    email_text = models.CharField(max_length=1000, blank=True, null=True)
    sent = models.BooleanField()
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'macaddress_warningmail'


class Manufacturer(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manufacturer'


class MatingcyclesSn(models.Model):
    serialnr = models.CharField(primary_key=True, max_length=32)
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    slotnr = models.IntegerField()
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    matingcycles = models.IntegerField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'matingcycles_sn'
        unique_together = (('serialnr', 'figonr', 'slotnr', 'uut_result', 'uut_result_loc'),)


class Messages(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    messagetext_de = models.CharField(unique=True, max_length=255)
    messagetext_en = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class Model(models.Model):
    modelnumber = models.CharField(max_length=64)
    devicename = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Addresses, models.DO_NOTHING)
    cal_laboratory = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True, related_name='cal_laboratory_Model_set')
    cal_last_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cal_laboratory_alt = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True, related_name='cal_laboratory_alt_Model_set')
    cal_last_price_alt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    voscal = models.BooleanField(blank=True, null=True)
    voscal_comment = models.CharField(max_length=255, blank=True, null=True)
    in_house_cal = models.BooleanField(blank=True, null=True)
    in_house_cal_woi = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    software = models.BooleanField(blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    cal_int_recomm_manuf = models.ForeignKey(Calibrationinterval, models.DO_NOTHING)
    end_of_support_date = models.DateField(blank=True, null=True)
    cal_last_price_curr = models.CharField(max_length=32, blank=True, null=True)
    cal_last_price_alt_curr = models.CharField(max_length=32, blank=True, null=True)
    calibration = models.BooleanField()
    functional_test = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'model'
        unique_together = (('modelnumber', 'manufacturer'),)


class Packingslip(models.Model):
    sender_address = models.ForeignKey(Addresses, models.DO_NOTHING)
    sender_person = models.ForeignKey(Contactperson, models.DO_NOTHING)
    serviceprovider = models.ForeignKey(Addresses, models.DO_NOTHING, related_name='serviceprovider_Packingslip_set')
    activities = models.CharField(max_length=255)
    deliveryaddress = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True, related_name='deliveryaddress_Packingslip_set')
    printed_date = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'packingslip'


class Product(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    macaddresses_per_unit = models.IntegerField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product'


class Productfamily(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    producttype = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'productfamily'


class Productgroup(models.Model):
    description = models.CharField(unique=True, max_length=32)
    manager = models.ForeignKey(Contactperson, models.DO_NOTHING)
    supplychain = models.ForeignKey('Supplychain', models.DO_NOTHING)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'productgroup'


class Productphase(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'productphase'


class Project(models.Model):
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    ordernr = models.CharField(max_length=32)
    customer_final = models.CharField(max_length=32, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    releasenr = models.CharField(max_length=32, blank=True, null=True)
    testcondition = models.ForeignKey('Testcondition', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    member = models.CharField(max_length=256, blank=True, null=True)
    closed = models.BooleanField()
    spare_staging = models.BooleanField()
    assembling_system = models.BooleanField()
    module_configuration = models.BooleanField()
    fwp = models.BooleanField()
    tests = models.BooleanField()
    reboot_test = models.BooleanField()
    traffic_test = models.BooleanField()
    documentation = models.BooleanField()
    preparing_shipping = models.BooleanField()
    ncu_database = models.ForeignKey(Deliverycondition, models.DO_NOTHING, db_column='ncu_database')
    shelf_internal_cables = models.BooleanField()
    shipping_documents = models.BooleanField()
    staging_documents = models.BooleanField()
    completeness_check = models.BooleanField()
    outgoinginspection = models.BooleanField()
    outinspection_user = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    station_id = models.CharField(max_length=16, blank=True, null=True)
    vex_tester = models.CharField(max_length=32, blank=True, null=True)
    other_tester = models.CharField(max_length=32, blank=True, null=True)
    traffic_doc_folder = models.CharField(max_length=255, blank=True, null=True)
    deliverynr = models.CharField(max_length=32, blank=True, null=True)
    ibase = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'
        unique_together = (('id', 'location'), ('location', 'ordernr'),)


class ProjectHist(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    project_loc = models.IntegerField()
    ordernr = models.CharField(max_length=32, blank=True, null=True)
    customer_final = models.CharField(max_length=32, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    releasenr = models.CharField(max_length=32, blank=True, null=True)
    testcondition_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    member = models.CharField(max_length=256, blank=True, null=True)
    closed = models.BooleanField()
    spare_staging = models.BooleanField()
    assembling_system = models.BooleanField()
    module_configuration = models.BooleanField()
    fwp = models.BooleanField()
    tests = models.BooleanField()
    reboot_test = models.BooleanField()
    traffic_test = models.BooleanField()
    documentation = models.BooleanField()
    preparing_shipping = models.BooleanField()
    ncu_database = models.IntegerField()
    shelf_internal_cables = models.BooleanField()
    shipping_documents = models.BooleanField()
    staging_documents = models.BooleanField()
    completeness_check = models.BooleanField()
    outgoinginspection = models.BooleanField()
    outinspection_user = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    station_id = models.CharField(max_length=16, blank=True, null=True)
    vex_tester = models.CharField(max_length=32, blank=True, null=True)
    other_tester = models.CharField(max_length=32, blank=True, null=True)
    traffic_doc_folder = models.CharField(max_length=255, blank=True, null=True)
    deliverynr = models.CharField(max_length=32, blank=True, null=True)
    ibase = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_hist'
        unique_together = (('id', 'project', 'project_loc'),)


class ProjectShelf(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    project_loc = models.IntegerField()
    node_shelf_name = models.CharField(max_length=64, blank=True, null=True)
    serialnr = models.CharField(max_length=32)
    articlenr = models.CharField(max_length=32, blank=True, null=True)
    articledesc = models.CharField(max_length=32, blank=True, null=True)
    no_shelf_kit = models.BooleanField()
    test_ip = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    shelfnr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_shelf'
        unique_together = (('id', 'project', 'project_loc'), ('project_loc', 'id', 'serialnr'), ('project_loc', 'project', 'shelfnr', 'node_shelf_name'),)


class Properties(models.Model):
    controlname = models.CharField(max_length=255)
    datafieldname = models.CharField(max_length=255, blank=True, null=True)
    datatype = models.CharField(max_length=32, blank=True, null=True)
    length = models.CharField(max_length=32, blank=True, null=True)
    label_de = models.CharField(max_length=255, blank=True, null=True)
    statustext_de = models.CharField(max_length=255, blank=True, null=True)
    label_en = models.CharField(max_length=255, blank=True, null=True)
    statustext_en = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    mandatory = models.BooleanField(blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    active_in_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'properties'
        unique_together = (('controlname', 'project'),)


class PsnSn(models.Model):
    psn = models.CharField(primary_key=True, max_length=32)
    serialnr = models.CharField(max_length=32)
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'psn_sn'
        unique_together = (('psn', 'serialnr'),)


class Release(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    optional = models.BooleanField()
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    releasefolder = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release'
# Unable to inspect table 'rep_location_master'
# The error was: FEHLER:  keine Berechtigung f�r Relation rep_location_master

# Unable to inspect table 'rep_master_location'
# The error was: FEHLER:  keine Berechtigung f�r Relation rep_master_location



class ResEdfa(models.Model):
    serialnr = models.CharField(primary_key=True, max_length=32)
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    product_order_number = models.CharField(max_length=32, blank=True, null=True)
    timestmp_created = models.DateTimeField()
    station_id = models.CharField(max_length=32)
    wip_number = models.CharField(max_length=32, blank=True, null=True)
    voadac = models.CharField(max_length=32, blank=True, null=True)
    urxloss = models.CharField(max_length=32, blank=True, null=True)
    s1postwdmil = models.CharField(max_length=32, blank=True, null=True)
    s1postipd2il = models.CharField(max_length=32, blank=True, null=True)
    s1outisotos1out = models.CharField(max_length=32, blank=True, null=True)
    voaildb = models.CharField(max_length=32, blank=True, null=True)
    s2postwdmil = models.CharField(max_length=32, blank=True, null=True)
    s2postipd4il = models.CharField(max_length=32, blank=True, null=True)
    s2ipbctoiwdmil = models.CharField(max_length=32, blank=True, null=True)
    erbiumloss = models.CharField(max_length=32, blank=True, null=True)
    gainripple = models.CharField(max_length=32, blank=True, null=True)
    gaintilt = models.CharField(max_length=32, blank=True, null=True)
    s1output = models.CharField(max_length=32, blank=True, null=True)
    s1and2output = models.CharField(max_length=32, blank=True, null=True)
    pump1_serial = models.CharField(max_length=32, blank=True, null=True)
    pump1_model = models.CharField(max_length=32, blank=True, null=True)
    pump1_power_mw = models.CharField(max_length=32, blank=True, null=True)
    pump1_curiop_ma = models.CharField(max_length=32, blank=True, null=True)
    pump1_curmon_ma = models.CharField(max_length=32, blank=True, null=True)
    pump1_wl_nm = models.CharField(max_length=32, blank=True, null=True)
    pump1_power_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump1_onlypower_mw = models.CharField(max_length=32, blank=True, null=True)
    pump1_onlypower_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump1_cur_ma = models.CharField(max_length=32, blank=True, null=True)
    pump1_tp_mv = models.CharField(max_length=32, blank=True, null=True)
    pump1_digipot_max = models.CharField(max_length=32, blank=True, null=True)
    pump1_digipot_cal = models.CharField(max_length=32, blank=True, null=True)
    pump2_serial = models.CharField(max_length=32, blank=True, null=True)
    pump2_model = models.CharField(max_length=32, blank=True, null=True)
    pump2_power_mw = models.CharField(max_length=32, blank=True, null=True)
    pump2_curiop_ma = models.CharField(max_length=32, blank=True, null=True)
    pump2_curmon_ma = models.CharField(max_length=32, blank=True, null=True)
    pump2_wl_nm = models.CharField(max_length=32, blank=True, null=True)
    pump2_power_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump2_onlypower_mw = models.CharField(max_length=32, blank=True, null=True)
    pump2_onlypower_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump2_cur_ma = models.CharField(max_length=32, blank=True, null=True)
    pump2_tp_mv = models.CharField(max_length=32, blank=True, null=True)
    pump2_digipot_max = models.CharField(max_length=32, blank=True, null=True)
    pump2_digipot_cal = models.CharField(max_length=32, blank=True, null=True)
    pump3_serial = models.CharField(max_length=32, blank=True, null=True)
    pump3_model = models.CharField(max_length=32, blank=True, null=True)
    pump3_power_mw = models.CharField(max_length=32, blank=True, null=True)
    pump3_curiop_ma = models.CharField(max_length=32, blank=True, null=True)
    pump3_curmon_ma = models.CharField(max_length=32, blank=True, null=True)
    pump3_wl_nm = models.CharField(max_length=32, blank=True, null=True)
    pump3_power_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump3_onlypower_mw = models.CharField(max_length=32, blank=True, null=True)
    pump3_onlypower_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump3_cur_ma = models.CharField(max_length=32, blank=True, null=True)
    pump3_tp_mv = models.CharField(max_length=32, blank=True, null=True)
    pump3_power_wdm_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump3_digipot_max = models.CharField(max_length=32, blank=True, null=True)
    pump3_digipot_cal = models.CharField(max_length=32, blank=True, null=True)
    pump4_serial = models.CharField(max_length=32, blank=True, null=True)
    pump4_model = models.CharField(max_length=32, blank=True, null=True)
    pump4_power_mw = models.CharField(max_length=32, blank=True, null=True)
    pump4_curiop_ma = models.CharField(max_length=32, blank=True, null=True)
    pump4_curmon_ma = models.CharField(max_length=32, blank=True, null=True)
    pump4_wl_nm = models.CharField(max_length=32, blank=True, null=True)
    pump4_power_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump4_onlypower_mw = models.CharField(max_length=32, blank=True, null=True)
    pump4_onlypower_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump4_cur_ma = models.CharField(max_length=32, blank=True, null=True)
    pump4_tp_mv = models.CharField(max_length=32, blank=True, null=True)
    pump4_power_wdm_dbm = models.CharField(max_length=32, blank=True, null=True)
    pump4_digipot_max = models.CharField(max_length=32, blank=True, null=True)
    pump4_digipot_cal = models.CharField(max_length=32, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    s1postipd1il = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_edfa'
        unique_together = (('serialnr', 'figonr'),)


class ResEeprom(models.Model):
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    serialnr = models.CharField(max_length=32)
    figonr = models.CharField(max_length=32)
    moduletype = models.CharField(max_length=32, blank=True, null=True)
    unitname = models.CharField(max_length=32, blank=True, null=True)
    eeprom_file = models.CharField(max_length=255, blank=True, null=True)
    bin_data1a = models.CharField(max_length=257, blank=True, null=True)
    bin_data1b = models.CharField(max_length=257, blank=True, null=True)
    bin_data2a = models.CharField(max_length=257, blank=True, null=True)
    bin_data2b = models.CharField(max_length=257, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'res_eeprom'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class ResEepromdata(models.Model):
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    shelf_ip = models.CharField(max_length=16, blank=True, null=True)
    node_id = models.CharField(max_length=6, blank=True, null=True)
    moduletype = models.CharField(max_length=32, blank=True, null=True)
    serialnr = models.CharField(max_length=32, blank=True, null=True)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    partnr = models.CharField(max_length=32, blank=True, null=True)
    spec_eepromdata_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=6, blank=True, null=True)
    contents = models.CharField(max_length=2048, blank=True, null=True)
    status = models.CharField(max_length=4, blank=True, null=True)
    info = models.CharField(max_length=2048, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'res_eepromdata'
        unique_together = (('id', 'uut_result_loc', 'uut_result'),)


class ResFilter(models.Model):
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    serialnr = models.CharField(max_length=32, blank=True, null=True)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    distributor = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    il_min = models.CharField(max_length=16, blank=True, null=True)
    il_max = models.CharField(max_length=16, blank=True, null=True)
    iso_min = models.CharField(max_length=16, blank=True, null=True)
    mux_demux = models.CharField(max_length=6)
    system_desc = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    test_datetime = models.DateTimeField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    il_avg = models.CharField(max_length=16, blank=True, null=True)
    iso_avg = models.CharField(max_length=16, blank=True, null=True)
    iso_tot = models.CharField(max_length=16, blank=True, null=True)
    iso_min_nadj = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_filter'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class ResInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    step_name = models.CharField(max_length=255)
    steptype = models.CharField(max_length=32)
    teststatus = models.CharField(max_length=32)
    report_text = models.CharField(max_length=2000, blank=True, null=True)
    min_limit = models.CharField(max_length=255, blank=True, null=True)
    step_value = models.CharField(max_length=255, blank=True, null=True)
    max_limit = models.CharField(max_length=255, blank=True, null=True)
    measunit = models.CharField(max_length=32, blank=True, null=True)
    comp = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'res_inventory'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class ResKzt(models.Model):
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    serialnr = models.CharField(max_length=32, blank=True, null=True)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    testdevice = models.CharField(max_length=32, blank=True, null=True)
    testcycles = models.CharField(max_length=16, blank=True, null=True)
    testcycle_currnr = models.CharField(max_length=16, blank=True, null=True)
    test_currnr = models.CharField(max_length=16, blank=True, null=True)
    testduration_s = models.CharField(max_length=16, blank=True, null=True)
    temp_celsius = models.CharField(max_length=16, blank=True, null=True)
    testresult = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'res_kzt'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class ResUtb(models.Model):
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    serialnr = models.CharField(max_length=32, blank=True, null=True)
    station_id = models.CharField(max_length=32, blank=True, null=True)
    utb_hardware_version = models.CharField(max_length=32, blank=True, null=True)
    utb_software_version = models.CharField(max_length=32, blank=True, null=True)
    utb_software_date = models.DateField(blank=True, null=True)
    adapter_type = models.CharField(max_length=32, blank=True, null=True)
    sadapter_name = models.CharField(max_length=32, blank=True, null=True)
    sadapter_timestmp = models.DateTimeField(blank=True, null=True)
    content_id = models.CharField(max_length=32, blank=True, null=True)
    content_version = models.CharField(max_length=32, blank=True, null=True)
    content_build_number = models.CharField(max_length=32, blank=True, null=True)
    content_length = models.CharField(max_length=32, blank=True, null=True)
    content_name = models.CharField(max_length=32, blank=True, null=True)
    content_date = models.DateField(blank=True, null=True)
    ptest_software_version = models.CharField(max_length=32, blank=True, null=True)
    ptest_software_date = models.DateField(blank=True, null=True)
    filecontents = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'res_utb'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class Retestrate(models.Model):
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    retestrate = models.IntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'retestrate'


class Retestreason(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'retestreason'


class SettingNaming(models.Model):
    tablename = models.CharField(max_length=32)
    fieldname = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'setting_naming'
        unique_together = (('tablename', 'fieldname'),)


class ShelfArticle(models.Model):
    project = models.ForeignKey(ProjectShelf, models.DO_NOTHING)
    project_loc = models.IntegerField()
    project_shelf_id = models.IntegerField()
    slot = models.CharField(max_length=16)
    serialnr = models.CharField(max_length=32)
    articlenr = models.CharField(max_length=32, blank=True, null=True)
    articledesc = models.CharField(max_length=32, blank=True, null=True)
    hwrev = models.CharField(max_length=16, blank=True, null=True)
    fwp = models.CharField(max_length=16, blank=True, null=True)
    deleted = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shelf_article'
        unique_together = (('id', 'project', 'project_loc'), ('project_loc', 'project_shelf_id', 'serialnr'), ('project_loc', 'project_shelf_id', 'slot'),)


class ShelfArticleSc(models.Model):
    project = models.ForeignKey(ProjectShelf, models.DO_NOTHING)
    project_loc = models.IntegerField()
    project_shelf_id = models.IntegerField()
    slot = models.CharField(max_length=16)
    serialnr = models.CharField(max_length=32)
    articlenr = models.CharField(max_length=32, blank=True, null=True)
    articledesc = models.CharField(max_length=32, blank=True, null=True)
    hwrev = models.CharField(max_length=16, blank=True, null=True)
    fwp = models.CharField(max_length=16, blank=True, null=True)
    deleted = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shelf_article_sc'
        unique_together = (('id', 'project', 'project_loc'), ('project_loc', 'project_shelf_id', 'serialnr'), ('project_loc', 'project_shelf_id', 'slot'),)


class SpecBundle(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    figonr = models.CharField(max_length=32)
    kitpart = models.CharField(max_length=32)
    slotid = models.CharField(max_length=32)
    dstat_offset = models.CharField(max_length=32, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_bundle'


class SpecCfpCommon(models.Model):
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr', primary_key=True)
    mating_cycles_allowed = models.IntegerField()
    tx_power_min_dbm = models.CharField(max_length=16)
    tx_power_max_dbm = models.CharField(max_length=16)
    tx_oop_mon_acc_db = models.CharField(max_length=16)
    tx_oop_mon_rep_db = models.CharField(max_length=16)
    tx_number_of_lanes = models.CharField(max_length=16)
    tx_test_datarate_gbits = models.CharField(max_length=16)
    tx_prbs = models.CharField(max_length=16)
    tx_tolerance_db = models.CharField(max_length=16)
    rx_power_max_dbm = models.CharField(max_length=16)
    rx_oip_mon_acc_db = models.CharField(max_length=16)
    rx_oip_mon_rep_db = models.CharField(max_length=16)
    rx_tolerance_db = models.CharField(max_length=16)
    losa_min_dbm = models.CharField(max_length=16)
    losd_max_dbm = models.CharField(max_length=16)
    los_hysteresis_min_db = models.CharField(max_length=16)
    los_hysteresis_max_db = models.CharField(max_length=16, blank=True, null=True)
    los_test_datarate_gbits = models.CharField(max_length=16)
    los_tolerance_db = models.CharField(max_length=16)
    gen_case_temp_max_c = models.CharField(max_length=16, blank=True, null=True)
    gen_current_max_33v_a = models.CharField(max_length=16, blank=True, null=True)
    gen_laser_bias_min_ma = models.CharField(max_length=16, blank=True, null=True)
    gen_laser_bias_max_ma = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_oma_min_dbm = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_oma_max_dbm = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_er_db = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_mask_test = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_prbs_eye_meas = models.CharField(max_length=16, blank=True, null=True)
    tx_laser_prbs_oma = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    nvr4_checksum_calc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spec_cfp_common'


class SpecCfpNvr(models.Model):
    figonr = models.ForeignKey(SpecCfpCommon, models.DO_NOTHING, db_column='figonr')
    register_address = models.CharField(max_length=16)
    register_name = models.CharField(max_length=255)
    register_size = models.IntegerField()
    expected_value = models.CharField(max_length=32)
    mask = models.CharField(max_length=16, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    report_check = models.BooleanField()
    active = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_cfp_nvr'
        unique_together = (('figonr', 'register_name'),)


class SpecCfpOsnr(models.Model):
    figonr = models.ForeignKey(SpecCfpCommon, models.DO_NOTHING, db_column='figonr')
    osnr_testnr = models.IntegerField()
    osnr_datarate_gbits = models.CharField(max_length=16, blank=True, null=True)
    osnr_dispersion_psnm = models.CharField(max_length=16, blank=True, null=True)
    osnr_rx_pow_dbm = models.CharField(max_length=16, blank=True, null=True)
    osnr_osnr_db = models.CharField(max_length=16, blank=True, null=True)
    osnr_testtime_s = models.CharField(max_length=16, blank=True, null=True)
    osnr_ber = models.CharField(max_length=16, blank=True, null=True)
    active = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_cfp_osnr'
        unique_together = (('figonr', 'osnr_testnr'),)


class SpecCfpSens(models.Model):
    figonr = models.ForeignKey(SpecCfpCommon, models.DO_NOTHING, db_column='figonr')
    sens_testnr = models.IntegerField()
    rx_sens_power_dbm = models.CharField(max_length=16)
    rx_sens_prbs = models.CharField(max_length=16)
    rx_sens_test_datarate_gbits = models.CharField(max_length=16)
    rx_sens_fibre_length_km = models.CharField(max_length=16)
    rx_sens_ber = models.CharField(max_length=16)
    rx_sens_traffic_test_time_s = models.CharField(max_length=16)
    rx_sens_stepsize_db = models.CharField(max_length=16)
    active = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_cfp_sens'
        unique_together = (('figonr', 'sens_testnr'),)


class SpecCfpWl(models.Model):
    figonr = models.ForeignKey(SpecCfpCommon, models.DO_NOTHING, db_column='figonr')
    lane = models.IntegerField()
    wl_min = models.CharField(max_length=32)
    wl_max = models.CharField(max_length=32)
    unit = models.CharField(max_length=3)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    wl_tolerance_nm = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_cfp_wl'
        unique_together = (('figonr', 'lane'),)


class SpecEepromdata(models.Model):
    id = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=32)
    value = models.CharField(max_length=256, blank=True, null=True)
    valuetype = models.CharField(max_length=8, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_eepromdata'
        unique_together = (('id', 'field'),)


class SpecEthernet(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    fmtver = models.CharField(max_length=32, blank=True, null=True)
    uname = models.CharField(max_length=32, blank=True, null=True)
    pn = models.CharField(max_length=32, blank=True, null=True)
    nummac = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_ethernet'


class SpecFilter(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING, unique=True)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    number_channels = models.IntegerField()
    mon_port = models.BooleanField()
    upg_port = models.BooleanField()
    reflected = models.BooleanField()
    inv_check = models.BooleanField()
    grid = models.CharField(max_length=32)
    adapt_conn = models.CharField(max_length=32)
    ilmax_mon = models.CharField(max_length=32, blank=True, null=True)
    ilmin_mon = models.CharField(max_length=32, blank=True, null=True)
    ilmax_upg = models.CharField(max_length=32, blank=True, null=True)
    ilmin_upg = models.CharField(max_length=32, blank=True, null=True)
    iso_upg = models.CharField(max_length=32, blank=True, null=True)
    start_wl_mon = models.CharField(max_length=32, blank=True, null=True)
    stop_wl_mon = models.CharField(max_length=32, blank=True, null=True)
    start_wl_upg_lower = models.CharField(max_length=32, blank=True, null=True)
    stop_wl_upg_lower = models.CharField(max_length=32, blank=True, null=True)
    start_wl_upg_upper = models.CharField(max_length=32, blank=True, null=True)
    stop_wl_upg_upper = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    fullband = models.BooleanField()
    iso_tot = models.CharField(max_length=32, blank=True, null=True)
    start_wl_upg_pass = models.CharField(max_length=32, blank=True, null=True)
    stop_wl_upg_pass = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_filter'


class SpecFilterchannel(models.Model):
    spec_filter = models.ForeignKey(SpecFilter, models.DO_NOTHING)
    mux_demux = models.CharField(max_length=32)
    channel = models.CharField(max_length=32)
    ilmax_chan = models.CharField(max_length=32)
    ilmin_chan = models.CharField(max_length=32)
    iso_ad_chan = models.CharField(max_length=32)
    iso_nad_chan = models.CharField(max_length=32)
    start_wl_chan = models.CharField(max_length=32)
    stop_wl_chan = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    wl_upg_minus_low = models.CharField(max_length=32, blank=True, null=True)
    wl_upg_minus_high = models.CharField(max_length=32, blank=True, null=True)
    wl_upg_plus_low = models.CharField(max_length=32, blank=True, null=True)
    wl_upg_plus_high = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_filterchannel'
        unique_together = (('spec_filter', 'mux_demux', 'channel'),)


class SpecGeneral(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    step_name = models.CharField(max_length=255)
    steptype = models.CharField(max_length=32)
    min_limit = models.CharField(max_length=255, blank=True, null=True)
    max_limit = models.CharField(max_length=255, blank=True, null=True)
    measunit = models.CharField(max_length=32, blank=True, null=True)
    comp = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    comments = models.CharField(max_length=255, blank=True, null=True)
    change_reason = models.CharField(max_length=255, blank=True, null=True)
    agile_pts = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_general'
        unique_together = (('figo_workstep', 'step_name'),)


class SpecInventory(models.Model):
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr')
    partnr = models.CharField(max_length=32, blank=True, null=True)
    moduletypename = models.CharField(max_length=32, blank=True, null=True)
    unitname = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    vendid = models.CharField(max_length=32, blank=True, null=True)
    clei = models.CharField(max_length=32, blank=True, null=True)
    pcbtype = models.CharField(max_length=32, blank=True, null=True)
    pcbtypeext = models.CharField(max_length=32, blank=True, null=True)
    pcbver = models.CharField(max_length=32, blank=True, null=True)
    pcbassembly = models.CharField(max_length=32, blank=True, null=True)
    pcbassemblyext = models.CharField(max_length=32, blank=True, null=True)
    hwrev = models.CharField(max_length=32, blank=True, null=True)
    hwrev_hidden = models.CharField(max_length=32, blank=True, null=True)
    hwrev_ext = models.CharField(max_length=32, blank=True, null=True)
    maxpower = models.CharField(max_length=32, blank=True, null=True)
    board_dimensions = models.CharField(max_length=32, blank=True, null=True)
    test_slot = models.IntegerField(blank=True, null=True)
    ucmtype = models.CharField(max_length=32, blank=True, null=True)
    ucmtypeext = models.CharField(max_length=32, blank=True, null=True)
    fwprev_img1 = models.CharField(max_length=32, blank=True, null=True)
    sw_image_file1 = models.CharField(max_length=255, blank=True, null=True)
    fwprev_img2 = models.CharField(max_length=32, blank=True, null=True)
    sw_image_file2 = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    card_type = models.CharField(max_length=32, blank=True, null=True)
    channel_inventory = models.CharField(max_length=32, blank=True, null=True)
    band_inventory = models.CharField(max_length=32, blank=True, null=True)
    subband_inventory = models.CharField(max_length=32, blank=True, null=True)
    group_inventory = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=32, blank=True, null=True)
    passive_shelf_pcb_type = models.CharField(max_length=32, blank=True, null=True)
    eeprom_device = models.CharField(max_length=32, blank=True, null=True)
    unique_shelf_id_hex = models.CharField(max_length=32, blank=True, null=True)
    pcb_type_hex = models.CharField(max_length=32, blank=True, null=True)
    supply_inventory = models.CharField(max_length=32, blank=True, null=True)
    fcu_max_power_dec = models.CharField(max_length=32, blank=True, null=True)
    dispersion_compensation = models.CharField(max_length=32, blank=True, null=True)
    dc_fiber_inventory = models.CharField(max_length=32, blank=True, null=True)
    channel_spacing = models.CharField(max_length=32, blank=True, null=True)
    fiber_type = models.CharField(max_length=32, blank=True, null=True)
    image_number = models.CharField(max_length=2, blank=True, null=True)
    bsd_label1 = models.CharField(max_length=32, blank=True, null=True)
    bsd_value1 = models.CharField(max_length=32, blank=True, null=True)
    bsd_label2 = models.CharField(max_length=32, blank=True, null=True)
    bsd_value2 = models.CharField(max_length=32, blank=True, null=True)
    bsd_label3 = models.CharField(max_length=32, blank=True, null=True)
    bsd_value3 = models.CharField(max_length=32, blank=True, null=True)
    bsd_label4 = models.CharField(max_length=32, blank=True, null=True)
    bsd_value4 = models.CharField(max_length=32, blank=True, null=True)
    bsd_label5 = models.CharField(max_length=32, blank=True, null=True)
    bsd_value5 = models.CharField(max_length=32, blank=True, null=True)
    spec_eepromdata_id = models.IntegerField()
    doc_item_number = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_inventory'


class SpecSanminareport(models.Model):
    figonr = models.ForeignKey(Figo, models.DO_NOTHING, db_column='figonr', blank=True, null=True)
    num_productfamily = models.CharField(max_length=32)
    cardname = models.CharField(max_length=32)
    testreportfolder = models.CharField(max_length=255)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_sanminareport'


class SpecSoftwarematrix(models.Model):
    hw_itemnumber = models.ForeignKey(Figo, models.DO_NOTHING, db_column='hw_itemnumber')
    sw_itemnumber = models.CharField(max_length=32)
    binfile = models.CharField(max_length=255)
    sw_version = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_softwarematrix'
        unique_together = (('sw_itemnumber', 'hw_itemnumber'),)


class SpecSpider(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    param1 = models.CharField(max_length=255, blank=True, null=True)
    param2 = models.CharField(max_length=255, blank=True, null=True)
    param3 = models.CharField(max_length=255, blank=True, null=True)
    param4 = models.CharField(max_length=255, blank=True, null=True)
    param5 = models.CharField(max_length=255, blank=True, null=True)
    param6 = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_spider'


class SpecTransceiver(models.Model):
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    figonr = models.CharField(max_length=32, blank=True, null=True)
    wavelength = models.ForeignKey('Wavelength', models.DO_NOTHING, blank=True, null=True)
    transceiver = models.ForeignKey('Transceiver', models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spec_transceiver'


class Station(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    description = models.CharField(max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    fsp_ip_addr = models.CharField(max_length=32, blank=True, null=True)
    subnet = models.CharField(max_length=32, blank=True, null=True)
    gateway = models.CharField(max_length=32, blank=True, null=True)
    cal_testsuite_filepath = models.CharField(max_length=255, blank=True, null=True)
    cal_date = models.DateTimeField(blank=True, null=True)
    cal_frequency = models.CharField(max_length=255, blank=True, null=True)
    doc_tss = models.CharField(max_length=255, blank=True, null=True)
    doc_tsd = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    computername = models.CharField(max_length=255, blank=True, null=True)
    active_in_use = models.BooleanField()
    confirm_date = models.DateField(blank=True, null=True)
    confirm_interval = models.CharField(max_length=32, blank=True, null=True)
    tms_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class StationContacts(models.Model):
    station = models.ForeignKey(Station, models.DO_NOTHING, unique=True)
    production_eng = models.ForeignKey(Contactperson, models.DO_NOTHING, blank=True, null=True, related_name='production_eng_StationContacts_set')
    test_eng = models.ForeignKey(Contactperson, models.DO_NOTHING, blank=True, null=True, related_name='test_eng_StationContacts_set')
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'station_contacts'


class StationEquipment(models.Model):
    station = models.ForeignKey(Station, models.DO_NOTHING)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    multiple_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_equipment'


class StationGeneralIni(models.Model):
    stationname = models.ForeignKey(Station, models.DO_NOTHING, db_column='stationname', primary_key=True)
    elsecheckboxtitle = models.CharField(max_length=32, blank=True, null=True)
    elsecheckboxdisplay = models.BooleanField(blank=True, null=True)
    addentry = models.CharField(max_length=32, blank=True, null=True)
    thirdinputdisplay = models.BooleanField(blank=True, null=True)
    socketcount = models.IntegerField(blank=True, null=True)
    containercount = models.IntegerField(blank=True, null=True)
    containernames = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'station_general_ini'


class StationRelhist(models.Model):
    station = models.ForeignKey(Station, models.DO_NOTHING)
    release = models.ForeignKey(Release, models.DO_NOTHING)
    changedate = models.DateTimeField()
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'station_relhist'


class StationSocketIni(models.Model):
    stationname = models.ForeignKey(StationGeneralIni, models.DO_NOTHING, db_column='stationname', primary_key=True)
    socketid = models.IntegerField()
    containerid = models.IntegerField()
    positionname = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'station_socket_ini'
        unique_together = (('stationname', 'containerid', 'socketid'),)


class StationWorkstep(models.Model):
    station = models.ForeignKey(Station, models.DO_NOTHING, related_name='stationWorksteps')
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    startseq_man = models.BooleanField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    active_in_use = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'station_workstep'
        unique_together = (('figo_workstep', 'station'),)


class StationequipSettings(models.Model):
    station_equipment = models.ForeignKey(StationEquipment, models.DO_NOTHING)
    setting_name = models.CharField(max_length=255)
    setting_type = models.CharField(max_length=32)
    min_limit = models.CharField(max_length=255, blank=True, null=True)
    max_limit = models.CharField(max_length=255, blank=True, null=True)
    measunit = models.CharField(max_length=32, blank=True, null=True)
    comp = models.CharField(max_length=32, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stationequip_settings'
        unique_together = (('station_equipment', 'setting_name'),)


class StepResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    uut_result = models.ForeignKey('UutResult', models.DO_NOTHING)
    uut_result_loc = models.IntegerField()
    step_name = models.CharField(max_length=255)
    steptype = models.CharField(max_length=32)
    teststatus = models.CharField(max_length=32)
    report_text = models.CharField(max_length=3000, blank=True, null=True)
    min_limit = models.CharField(max_length=255, blank=True, null=True)
    step_value = models.CharField(max_length=255, blank=True, null=True)
    max_limit = models.CharField(max_length=255, blank=True, null=True)
    measunit = models.CharField(max_length=32, blank=True, null=True)
    comp = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'step_result'
        unique_together = (('id', 'uut_result', 'uut_result_loc'),)


class StepSubresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    uut_result_id = models.IntegerField()
    uut_result_loc = models.IntegerField()
    step_result = models.ForeignKey(StepResult, models.DO_NOTHING)
    step_name = models.CharField(max_length=255)
    steptype = models.CharField(max_length=32)
    teststatus = models.CharField(max_length=32)
    report_text = models.CharField(max_length=2000, blank=True, null=True)
    min_limit = models.CharField(max_length=255, blank=True, null=True)
    step_value = models.CharField(max_length=255, blank=True, null=True)
    max_limit = models.CharField(max_length=255, blank=True, null=True)
    measunit = models.CharField(max_length=32, blank=True, null=True)
    comp = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'step_subresult'
        unique_together = (('id', 'step_result', 'uut_result_loc'),)


class Supplychain(models.Model):
    description = models.CharField(unique=True, max_length=255)
    owner = models.ForeignKey(Contactperson, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplychain'


class Tablesettings(models.Model):
    computername = models.CharField(primary_key=True, max_length=255)
    tablename = models.CharField(max_length=255)
    columnname = models.CharField(max_length=255)
    displayindex = models.IntegerField()
    width = models.IntegerField()
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tablesettings'
        unique_together = (('computername', 'tablename', 'columnname'),)


class Testcondition(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testcondition'


class Teststatus(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'teststatus'
# Unable to inspect table 'tms_filemover'
# The error was: FEHLER:  keine Berechtigung f�r Relation tms_filemover



class TmsSettings(models.Model):
    computername = models.CharField(primary_key=True, max_length=255)
    station_id = models.CharField(max_length=16, blank=True, null=True)
    version = models.CharField(max_length=16, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    updatepath = models.CharField(max_length=255, blank=True, null=True)
    loginuser = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    application = models.CharField(max_length=32)
    osname = models.CharField(max_length=64, blank=True, null=True)
    osversion = models.CharField(max_length=64, blank=True, null=True)
    oslanguage = models.CharField(max_length=10, blank=True, null=True)
    osinstalldate = models.DateTimeField(blank=True, null=True)
    os64bit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tms_settings'
        unique_together = (('computername', 'application'),)


class Transceiver(models.Model):
    description = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    articlenumber_rawmat = models.CharField(max_length=32, blank=True, null=True)
    threshold_test = models.BooleanField(blank=True, null=True)
    temp_hi_warn_celsius = models.CharField(max_length=16, blank=True, null=True)
    temp_hi_al_celsius = models.CharField(max_length=16, blank=True, null=True)
    temp_low_warn_celsius = models.CharField(max_length=16, blank=True, null=True)
    temp_low_al_celsius = models.CharField(max_length=16, blank=True, null=True)
    tx_pow_hi_al_dbm = models.CharField(max_length=16, blank=True, null=True)
    tx_pow_low_al_dbm = models.CharField(max_length=16, blank=True, null=True)
    rx_pow_hi_al_dbm = models.CharField(max_length=16, blank=True, null=True)
    rx_pow_low_al_dbm = models.CharField(max_length=16, blank=True, null=True)
    calc_delta_thresholds = models.CharField(max_length=16, blank=True, null=True)
    power_test = models.BooleanField(blank=True, null=True)
    tx_pow_ran_min_dbm = models.CharField(max_length=16, blank=True, null=True)
    tx_pow_ran_max_dbm = models.CharField(max_length=16, blank=True, null=True)
    rx_pow_ran_min_dbm = models.CharField(max_length=16, blank=True, null=True)
    rx_pow_ran_max_dbm = models.CharField(max_length=16, blank=True, null=True)
    calc_delta_power = models.CharField(max_length=16, blank=True, null=True)
    traffic_test = models.BooleanField(blank=True, null=True)
    datarate_traffic1_gbs = models.CharField(max_length=16, blank=True, null=True)
    datarate_traffic2_gbs = models.CharField(max_length=16, blank=True, null=True)
    datarate_traffic3_gbs = models.CharField(max_length=16, blank=True, null=True)
    test_time_traffic_s = models.CharField(max_length=16, blank=True, null=True)
    losa_min_dbm = models.CharField(max_length=16, blank=True, null=True)
    losa_max_dbm = models.CharField(max_length=16, blank=True, null=True)
    losd_max_dbm = models.CharField(max_length=16, blank=True, null=True)
    ext_ratio_min_db = models.CharField(max_length=16, blank=True, null=True)
    ext_ratio_max_db = models.CharField(max_length=16, blank=True, null=True)
    max_margin_percent = models.CharField(max_length=16, blank=True, null=True)
    eeprom_readwrite_test = models.BooleanField(blank=True, null=True)
    wavelength_test = models.BooleanField(blank=True, null=True)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    delta_threshold_temp_hi = models.CharField(max_length=255, blank=True, null=True)
    delta_threshold_temp_lo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transceiver'
        unique_together = (('description', 'manufacturer'),)


class TvStructure(models.Model):
    tv_order = models.CharField(primary_key=True, max_length=32)
    nodename = models.CharField(max_length=40)
    nodename_parent = models.CharField(max_length=40, blank=True, null=True)
    datatable = models.BooleanField()
    global_visible = models.BooleanField(blank=True, null=True)
    sheet = models.BooleanField()
    bitmap = models.CharField(max_length=32, blank=True, null=True)
    bitmap_sel = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    not_visible_group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tv_structure'
        unique_together = (('tv_order', 'nodename'),)


class UutResult(models.Model):
    location_id = models.IntegerField()
    serialnr = models.CharField(max_length=32)
    figonr = models.CharField(max_length=32)
    figo_description = models.CharField(max_length=255)
    figo_workstep_id = models.IntegerField()
    workstep_description = models.CharField(max_length=255)
    station_workstep_id = models.IntegerField()
    station_id = models.CharField(max_length=16)
    testsocket = models.IntegerField()
    seqfile_version = models.CharField(max_length=255, blank=True, null=True)
    ordernr_sap = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    execution_time = models.IntegerField(blank=True, null=True)
    resulttable = models.CharField(max_length=255, blank=True, null=True)
    teststatus = models.CharField(max_length=32, blank=True, null=True)
    errortype = models.ForeignKey(Errortype, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()
    wait_time = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    wip = models.BooleanField(blank=True, null=True)
    retestreason_id = models.IntegerField(blank=True, null=True)
    errorcause = models.CharField(max_length=255, blank=True, null=True)
    retest_approver = models.CharField(max_length=255, blank=True, null=True)
    debug = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uut_result'
        unique_together = (('id', 'location_id'),)


class Wavelength(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    frequency_thz = models.CharField(max_length=32, blank=True, null=True)
    wavelength_nm = models.CharField(max_length=32)
    tolerance_min_nm = models.CharField(max_length=32)
    tolerance_max_nm = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wavelength'


class WipSn(models.Model):
    serialnr = models.CharField(primary_key=True, max_length=32)
    figo_workstep = models.ForeignKey(FigoWorkstep, models.DO_NOTHING)
    wiporder = models.IntegerField()
    wiporder_back = models.IntegerField(blank=True, null=True)
    executed = models.BooleanField(blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wip_sn'
        unique_together = (('serialnr', 'figo_workstep'),)


class Workstep(models.Model):
    description = models.CharField(unique=True, max_length=255)
    information = models.CharField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=32)
    timestmp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'workstep'
