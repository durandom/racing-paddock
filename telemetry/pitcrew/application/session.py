from telemetry.models import Car, Driver, Game, SessionType, Track


class Session:
    def __init__(self, filter={}):
        if filter:
            self.id = filter["SessionId"]
            self.game = Game.objects.get_or_create(name=filter["GameName"])[0]
            self.track = self.game.tracks.get_or_create(name=filter["TrackCode"])[0]
            self.car = self.game.cars.get_or_create(name=filter["CarModel"])[0]
            self.session_type = SessionType.objects.get_or_create(type=filter["SessionType"])[0]
            self.driver = Driver.objects.get_or_create(name=filter["Driver"])[0]
        else:
            self.id = ""
            self.track = Track()
            self.car = Car()
            self.game = Game()
            self.session_type = SessionType()
            self.driver = Driver()

    def track_length(self) -> float:
        if self.track.length:
            return self.track.length
        else:
            return 1.0
