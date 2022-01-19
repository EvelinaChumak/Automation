from tests.models.base_model.base_model import BaseModel

class WeatherAPI(BaseModel):
    
    
    class Coord(BaseModel):
        
        def __init__(self, **kwargs):
            self.lon = kwargs.get('lon')
            self.lat = kwargs.get('lat')
            
    class Weather(BaseModel):
        
        def __init__(self, **kwargs):
            self.id = kwargs.get('id')
            self.main = kwargs.get('main')
            self.description = kwargs.get('description')
            self.icon = kwargs.get('icon')
            
    class Main(BaseModel):
        
        def __init__(self, **kwargs):
            self.temp = kwargs.get('temp')
            self.feels_like = kwargs.get('feels_like')
            self.temp_min = kwargs.get('temp_min')
            self.temp_max = kwargs.get('temp_max')
            self.pressure = kwargs.get('pressure')
            self.humidity = kwargs.get('humidity')
            
    class Wind(BaseModel):
        
        def __init__(self, **kwargs):
            self.speed = kwargs.get('speed')
            self.deg = kwargs.get('deg')
            
    class Clouds(BaseModel):
        
        def __init__(self, **kwargs):
            self.all = kwargs.get('all')
            
    class Sys(BaseModel):
        
        def __init__(self, **kwargs):
            self.type = kwargs.get('type')
            self.id = kwargs.get('id')
            self.message = kwargs.get('message')
            self.country = kwargs.get('country')
            self.sunrise = kwargs.get('sunrise')
            self.sunset = kwargs.get('sunset')
    
    
    def __init__(self, **kwargs):
        self.coord = kwargs.get('coord')
        self.weather = kwargs.get('weather')
        self.base = kwargs.get('base')
        self.main = kwargs.get('main')
        self.visibility = kwargs.get('visibility')
        self.wind = kwargs.get('wind')
        self.clouds = kwargs.get('clouds')
        self.dt = kwargs.get('dt')
        self.sys = kwargs.get('sys')
        self.timezone = kwargs.get('timezone')
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.cod = kwargs.get('cod')
    
    SELF_FIELDS = {
        'coord' : Coord,
        'weather' : Weather,
        'main' : Main,
        'wind' : Wind,
        'clouds': Clouds,
        'sys': Sys   
    }    
    
    def get_status(self):
        return self.response.get_status()
    
    