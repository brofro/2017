from test.Services.WeatherService import WeatherService

service = WeatherService('WeatherService', 'WeatherEndpoint')
print service.Name
print service.Endpoint

service.Start()
service.Stop()