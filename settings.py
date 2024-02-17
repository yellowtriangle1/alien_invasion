class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # self.ship_speed = 3.0

        # self.bullet_speed = 6.0
        self.ship_limit = 3
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 to right, -1 to left
        # self.fleet_direction = 1

        self.speedup_scale = 1.9
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.bullet_speed = 6.0
        self.alien_speed = 2.0
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
       