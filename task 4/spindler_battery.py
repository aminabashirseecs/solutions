from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date, service_interval=2):
        super().__init__(current_date, last_service_date)
        self.service_interval = service_interval

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= self.service_interval
