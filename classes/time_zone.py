from datetime import timedelta
import numbers


class TimeZone:
    def __init__(self, name: str, offset_hours: numbers.Integral, offset_minutes: numbers.Integral):
        if name is None or len(name.strip()) == 0:
            raise ValueError('timezone name can not be none')
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('hour offset must be integer')
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('minutes offset must be integer')
        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')

        self._name = name.strip()
        self._offset_minutes = offset_minutes
        self._offset_hours = offset_hours
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}), offset_hour={self._offset_hours}), (offset_minute={self._offset_minutes})'
