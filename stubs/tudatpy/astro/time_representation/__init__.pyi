from __future__ import annotations
import tudatpy.kernel.astro.time_representation
from tudatpy.kernel.astro.time_representation import DateTime
from tudatpy.kernel.astro.time_representation import TAI_to_TT
from tudatpy.kernel.astro.time_representation import TCB_to_TDB
from tudatpy.kernel.astro.time_representation import TCG_to_TT
from tudatpy.kernel.astro.time_representation import TDB_to_TCB
from tudatpy.kernel.astro.time_representation import TDB_to_TT
from tudatpy.kernel.astro.time_representation import TT_to_TAI
from tudatpy.kernel.astro.time_representation import TT_to_TCG
from tudatpy.kernel.astro.time_representation import TT_to_TDB
from tudatpy.kernel.astro.time_representation import TT_to_TDB_approximate
from tudatpy.kernel.astro.time_representation import Time
from tudatpy.kernel.astro.time_representation import TimeScaleConverter
from tudatpy.kernel.astro.time_representation import TimeScales
from tudatpy.kernel.astro.time_representation import add_days_to_datetime
from tudatpy.kernel.astro.time_representation import add_seconds_to_datetime
from tudatpy.kernel.astro.time_representation import calculate_seconds_in_current_julian_day
from tudatpy.kernel.astro.time_representation import calendar_date_to_days_since_epoch
from tudatpy.kernel.astro.time_representation import calendar_date_to_julian_day
from tudatpy.kernel.astro.time_representation import calendar_date_to_julian_day_since_epoch
from tudatpy.kernel.astro.time_representation import date_time_components_to_epoch
from tudatpy.kernel.astro.time_representation import date_time_components_to_epoch_time_object
from tudatpy.kernel.astro.time_representation import date_time_from_epoch
from tudatpy.kernel.astro.time_representation import date_time_from_iso_string
from tudatpy.kernel.astro.time_representation import datetime_to_python
from tudatpy.kernel.astro.time_representation import datetime_to_tudat
from tudatpy.kernel.astro.time_representation import default_time_scale_converter
from tudatpy.kernel.astro.time_representation import epoch_from_date_time_components
from tudatpy.kernel.astro.time_representation import epoch_from_date_time_iso_string
from tudatpy.kernel.astro.time_representation import get_days_in_month
from tudatpy.kernel.astro.time_representation import is_leap_year
from tudatpy.kernel.astro.time_representation import iso_string_to_epoch
from tudatpy.kernel.astro.time_representation import iso_string_to_epoch_time_object
from tudatpy.kernel.astro.time_representation import julian_day_to_calendar_date
from tudatpy.kernel.astro.time_representation import julian_day_to_modified_julian_day
from tudatpy.kernel.astro.time_representation import julian_day_to_python_datetime
from tudatpy.kernel.astro.time_representation import julian_day_to_seconds_since_epoch
from tudatpy.kernel.astro.time_representation import modified_julian_day_to_julian_day
from tudatpy.kernel.astro.time_representation import python_datetime_to_days_since_epoch
from tudatpy.kernel.astro.time_representation import python_datetime_to_julian_day
from tudatpy.kernel.astro.time_representation import seconds_since_epoch_to_julian_centuries_since_epoch
from tudatpy.kernel.astro.time_representation import seconds_since_epoch_to_julian_day
from tudatpy.kernel.astro.time_representation import seconds_since_epoch_to_julian_years_since_epoch
from tudatpy.kernel.astro.time_representation import year_and_days_in_year_to_calendar_date
__all__: list[str] = ['DateTime', 'TAI_to_TT', 'TCB_to_TDB', 'TCG_to_TT', 'TDB_to_TCB', 'TDB_to_TT', 'TT_to_TAI', 'TT_to_TCG', 'TT_to_TDB', 'TT_to_TDB_approximate', 'Time', 'TimeScaleConverter', 'TimeScales', 'add_days_to_datetime', 'add_seconds_to_datetime', 'calculate_seconds_in_current_julian_day', 'calendar_date_to_days_since_epoch', 'calendar_date_to_julian_day', 'calendar_date_to_julian_day_since_epoch', 'date_time_components_to_epoch', 'date_time_components_to_epoch_time_object', 'date_time_from_epoch', 'date_time_from_iso_string', 'datetime_to_python', 'datetime_to_tudat', 'default_time_scale_converter', 'epoch_from_date_time_components', 'epoch_from_date_time_iso_string', 'get_days_in_month', 'is_leap_year', 'iso_string_to_epoch', 'iso_string_to_epoch_time_object', 'julian_day_to_calendar_date', 'julian_day_to_modified_julian_day', 'julian_day_to_python_datetime', 'julian_day_to_seconds_since_epoch', 'modified_julian_day_to_julian_day', 'python_datetime_to_days_since_epoch', 'python_datetime_to_julian_day', 'seconds_since_epoch_to_julian_centuries_since_epoch', 'seconds_since_epoch_to_julian_day', 'seconds_since_epoch_to_julian_years_since_epoch', 'tai_scale', 'tdb_scale', 'tt_scale', 'ut1_scale', 'utc_scale', 'year_and_days_in_year_to_calendar_date']
tai_scale: tudatpy.kernel.astro.time_representation.TimeScales  # value = <TimeScales.tai_scale: 0>
tdb_scale: tudatpy.kernel.astro.time_representation.TimeScales  # value = <TimeScales.tdb_scale: 2>
tt_scale: tudatpy.kernel.astro.time_representation.TimeScales  # value = <TimeScales.tt_scale: 1>
ut1_scale: tudatpy.kernel.astro.time_representation.TimeScales  # value = <TimeScales.ut1_scale: 4>
utc_scale: tudatpy.kernel.astro.time_representation.TimeScales  # value = <TimeScales.utc_scale: 3>
