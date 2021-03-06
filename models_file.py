# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Synesisit(models.Model):
    meter_no = models.IntegerField(db_column='Meter_no')  # Field name made lowercase.
    connected_load = models.IntegerField(db_column='Connected_load')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    phase_1_line_to_neutral_volts = models.CharField(max_length=50)
    phase_1_current = models.CharField(max_length=50)
    phase_1_power = models.CharField(max_length=50)
    phase_1_volt_amps = models.CharField(max_length=50)
    phase_1_volt_amps_reactive = models.CharField(max_length=50)
    phase_1_power_factor = models.CharField(max_length=50)
    phase_2_line_to_neutral_volts = models.CharField(max_length=50)
    phase_2_current = models.CharField(max_length=50)
    phase_2_power = models.CharField(max_length=50)
    phase_2_volt_amps = models.CharField(max_length=50)
    phase_2_volt_amps_reactive = models.CharField(max_length=50)
    phase_2_power_factor = models.CharField(max_length=50)
    phase_3_line_to_neutral_volts = models.CharField(max_length=50)
    phase_3_current = models.CharField(max_length=50)
    phase_3_power = models.CharField(max_length=50)
    phase_3_volt_amps = models.CharField(max_length=50)
    phase_3_volt_amps_reactive = models.CharField(max_length=50)
    phase_3_power_factor = models.CharField(max_length=50)
    average_line_to_neutral_volts = models.CharField(max_length=50)
    average_line_current = models.CharField(max_length=50)
    sum_of_line_currents = models.CharField(max_length=50)
    total_system_power = models.CharField(max_length=50)
    total_system_volt_amps = models.CharField(max_length=50)
    total_system_var = models.CharField(max_length=50)
    total_system_power_factor = models.CharField(max_length=50)
    total_system_phase_angle = models.CharField(max_length=50)
    frequency_of_supply_voltages = models.CharField(max_length=50)
    import_wh_since_last_reset = models.CharField(max_length=50)
    export_wh_since_last_reset = models.CharField(max_length=50)
    import_varh_since_last_reset = models.CharField(max_length=50)
    export_varh_since_last_reset = models.CharField(max_length=50)
    line_1_to_line_2_volts = models.CharField(max_length=50)
    line_2_to_line_3_volts = models.CharField(max_length=50)
    line_3_to_line_1_volts = models.CharField(max_length=50)
    average_line_to_line_volts = models.CharField(max_length=50)
    neutral_current = models.CharField(max_length=50)
    total_kwh = models.CharField(max_length=50)
    total_kvarh = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'SynesisIT'
