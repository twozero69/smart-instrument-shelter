#tkinter
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image

#requests
import requests, json

#utility
import time


class weather_GUI():
    def __init__(self):
        #####     GUI setting     #####

        #main window
        self.__window = tk.Tk()
        self.__window.geometry('800x480')
        self.__window.title("weather GUI")
        self.__window.attributes('-fullscreen', True)
        self.__window.configure(cursor='none')
        self.__window.bind('<Escape>', self.typeESC)
        self.__window.bind('<Alt-Return>', self.typeALTENT)


        #weather image
        img_size=170
        self.__day_sun_img = ImageTk.PhotoImage(Image.open('day/sun.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__day_cloud_img = ImageTk.PhotoImage(Image.open('day/cloud.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__day_rain_img = ImageTk.PhotoImage(Image.open('day/rain.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__day_snow_img = ImageTk.PhotoImage(Image.open('day/snow.png').resize((img_size, img_size), Image.ANTIALIAS))

        self.__night_moon_img = ImageTk.PhotoImage(Image.open('night/moon.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__night_cloud_img = ImageTk.PhotoImage(Image.open('night/cloud.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__night_rain_img = ImageTk.PhotoImage(Image.open('night/rain.png').resize((img_size, img_size), Image.ANTIALIAS))
        self.__night_snow_img = ImageTk.PhotoImage(Image.open('night/snow.png').resize((img_size, img_size), Image.ANTIALIAS))

        self.__weather_img = tk.Label(self.__window, image=self.__day_sun_img)
        self.__weather_img.place(x=50, y=30)


        #date and location
        big_font=tk.font.Font(family="맑은 고딕", size=20)
        
        self.__date_label = tk.Label(self.__window, text='', font=big_font)
        self.__date_label.place(x=400, y=80)
        
        self.__location_label = tk.Label(self.__window, text='위도 ㅁㅁㅁ / 경도 ㅁㅁㅁ', font=big_font)
        self.__location_label.place(x=400, y=130)


        #weather information
        frame_width = 700
        frame_height = 200
        label_width = 10
        label_height = 2

        small_font=tk.font.Font(family='맑은 고딕', size=15)
        info_frame = tk.Frame(self.__window, width=frame_width, height=frame_height, borderwidth=2, relief=tk.GROOVE)

        temperature_labelframe = tk.LabelFrame(info_frame, text='기온', font=small_font)
        self.__temperature_label = tk.Label(temperature_labelframe, width=label_width, height=label_height, text='23°C', font=small_font)
        self.__temperature_label.pack()
        temperature_labelframe.grid(row=0, column=0, padx=10, pady=10)

        humidity_labelframe = tk.LabelFrame(info_frame, text='습도', font=small_font)
        self.__humidity_label = tk.Label(humidity_labelframe, width=label_width, height=label_height, text='32%', font=small_font)
        self.__humidity_label.pack()
        humidity_labelframe.grid(row=0, column=1, padx=10, pady=10)

        windspeed_labelframe = tk.LabelFrame(info_frame, text='풍속', font=small_font)
        self.__windspeed_label = tk.Label(windspeed_labelframe, width=label_width, height=label_height, text='3m/s', font=small_font)
        self.__windspeed_label.pack()
        windspeed_labelframe.grid(row=0, column=2, padx=10, pady=10)

        cloud_labelframe = tk.LabelFrame(info_frame, text='구름', font=small_font)
        self.__cloud_label = tk.Label(cloud_labelframe, width=label_width, height=label_height, text='흐림', font=small_font)
        self.__cloud_label.pack()
        cloud_labelframe.grid(row=0, column=3, padx=10, pady=10)

        pressure_labelframe = tk.LabelFrame(info_frame, text='기압', font=small_font)
        self.__pressure_label = tk.Label(pressure_labelframe, width=label_width, height=label_height, text='hPa', font=small_font)
        self.__pressure_label.pack()
        pressure_labelframe.grid(row=0, column=4, padx=10, pady=10)

        rain_labelframe = tk.LabelFrame(info_frame, text='비', font=small_font)
        self.__rain_label = tk.Label(rain_labelframe, width=label_width, height=label_height, text='내림', font=small_font)
        self.__rain_label.pack()
        rain_labelframe.grid(row=1, column=0, padx=10, pady=10)

        precipitation_labelframe = tk.LabelFrame(info_frame, text='예상강수량', font=small_font)
        self.__precipitation_label = tk.Label(precipitation_labelframe, width=label_width, height=label_height, text='30mm', font=small_font)
        self.__precipitation_label.pack()
        precipitation_labelframe.grid(row=1, column=1, padx=10, pady=10) 

        thunderdist_labelframe = tk.LabelFrame(info_frame, text='낙뢰거리', font=small_font)
        self.__thunderdist_label = tk.Label(thunderdist_labelframe, width=label_width, height=label_height, text='3초후', font=small_font)
        self.__thunderdist_label.pack()
        thunderdist_labelframe.grid(row=1, column=2, padx=10, pady=10)

        discomfort_labelframe = tk.LabelFrame(info_frame, text='불쾌지수', font=small_font)
        self.__discomfort_label = tk.Label(discomfort_labelframe, width=label_width, height=label_height, text='32(불쾌)', font=small_font)
        self.__discomfort_label.pack()
        discomfort_labelframe.grid(row=1, column=3, padx=10, pady=10)

        windchill_labelframe = tk.LabelFrame(info_frame, text='체감온도', font=small_font)
        self.__windchill_label = tk.Label(windchill_labelframe, width=label_width, height=label_height, text='16°C', font=small_font)
        self.__windchill_label.pack()
        windchill_labelframe.grid(row=1, column=4, padx=10, pady=10)

        info_frame.place(x=35, y=240)



        #####     http setting     #####
        URL_head='http://'
        URL_IP='localhost:8000'
        URL_tail1='/whiteshelter/sensor-data/one/'
        URL_tail2='/whiteshelter/gps-data/one/'
        URL_tail3='/whiteshelter/img-processing-data/one/'
        self.__sensor_URL=URL_head+URL_IP+URL_tail1
        self.__gps_URL=URL_head+URL_IP+URL_tail2
        self.__img_processing_URL=URL_head+URL_IP+URL_tail3
        self.__sensor_data={}
        self.__gps_data={}
        self.__img_processing_data={}


        # start GUI
        self.start_GUI()




    def typeESC(self, event):
        self.__window.attributes('-fullscreen', False)


    def typeALTENT(self, event):
        self.__window.attributes('-fullscreen', True)


    def get_data(self):
        self.__sensor_data=requests.get(self.__sensor_URL).json()
        self.__gps_data=requests.get(self.__gps_URL).json()
        self.__img_processing_data=requests.get(self.__img_processing_URL).json()
    
    
    def update_GUI(self):
        #date_label
        date_struct=time.localtime(time.time())
        date_str=str(date_struct.tm_year)+'년 '+str(date_struct.tm_mon)+'월 '+str(date_struct.tm_mday)+'일 '+str(date_struct.tm_hour)+'시 '+str(date_struct.tm_min)+'분'
        self.__date_label.config(text=date_str)
        
        
        #location_label
        latitude=round(self.__gps_data['latitude'], 4)
        longitude=round(self.__gps_data['longitude'], 4)
        location_str='위도 '+str(latitude)+' / '+'경도 '+str(longitude)
        self.__location_label.config(text=location_str)
        
        
        #temperature_label
        temperature=round(self.__sensor_data['temperature'], 1)
        temperature_str=str(temperature)+'°C'
        self.__temperature_label.config(text=temperature_str)

        
        #humidity_label
        humidity=round(self.__sensor_data['humidity'], 1)
        humidity_str=str(humidity)+'%'
        self.__humidity_label.config(text=humidity_str)

        
        #windspeed_label
        windspeed=round(self.__sensor_data['windspeed'], 1)
        windspeed_str=str(windspeed)+'m/s'
        if windspeed >= 10:
        	self.__windspeed_label.config(text=windspeed_str, fg='red')
        elif windspeed >= 5:
        	self.__windspeed_label.config(text=windspeed_str, fg='OrangeRed2')
        else:
        	self.__windspeed_label.config(text=windspeed_str, fg='black')

        
        #rain_label
        rain=self.__sensor_data['rain']
        if rain > 500:
            self.__rain_label.config(text='안 내림')
        else:
            self.__rain_label.config(text='내림')


        #pressure_label
        pressure=round(self.__sensor_data['pressure'], 1)
        pressure_str=str(pressure)+'hPa'
        self.__pressure_label.config(text=pressure_str)

        
        #cloud_label
        cloud=round(self.__img_processing_data['cloud'], 0)
        if cloud <= 2:#0~2
            self.__cloud_label.config(text='맑음')
        elif cloud <= 4:#2~4
            self.__cloud_label.config(text='구름 조금')
        elif cloud <= 6:#4~6
            self.__cloud_label.config(text='구름 많음')
        else:#6~8
            self.__cloud_label.config(text='흐림')

        
        #precipitation_label
        precipitation=self.__img_processing_data['precipitation']
        precipitation_str=str(precipitation)+'mm'
        self.__precipitation_label.config(text=precipitation_str)
        
        
        #thunderdist_label
        thunderdist=round(self.__img_processing_data['thunderdist'], 1)
        thunderdist_str=str(thunderdist)+'km'
        self.__thunderdist_label.config(text=thunderdist_str)
        
        
        #discomfort_label
        DI=int(1.8*temperature-0.55*(1-humidity*0.01)*(1.8*temperature-26)+32)
        if DI >= 80:
            self.__discomfort_label.config(text=str(DI)+'(매우 불쾌)')
        elif DI >= 75:
            self.__discomfort_label.config(text=str(DI)+'(불쾌)')
        elif DI > 68:
            self.__discomfort_label.config(text=str(DI)+'(보통)')
        else:
            self.__discomfort_label.config(text=str(DI)+'(쾌적)')

        
        #windchill_label
        windchill=round(13.12+0.6215*temperature-11.37*(windspeed**0.16)+0.3965*(windspeed**0.16)*temperature, 1)
        windchill_str=str(windchill)+'°C'
        if windchill >= 32:
            self.__windchill_label.config(text=windchill_str, fg='red')
        elif windchill >= 24:
            self.__windchill_label.config(text=windchill_str, fg='black')
        elif windchill >= 18:
            self.__windchill_label.config(text=windchill_str, fg='black')
        elif windchill >= 5:
            self.__windchill_label.config(text=windchill_str, fg='sky blue')
        elif windchill >= -18:
            self.__windchill_label.config(text=windchill_str, fg='blue')
        else:
            self.__windchill_label.config(text=windchill_str, fg='navy')


        #weather_img
        if 6 <= date_struct.tm_hour and date_struct.tm_hour < 18:#day
            if rain > 500:#안 내림
                if cloud >= 4:#cloud
                    self.__weather_img.config(image=self.__day_cloud_img)
                else:#none cloud
                    self.__weather_img.config(image=self.__day_sun_img)
            else:#내림
                if temperature > 3:#rain
                    self.__weather_img.config(image=self.__day_rain_img)
                else:#snow
                    self.__weather_img.config(image=self.__day_snow_img)
            
        else:#night
            if rain > 500:#안 내림
                if cloud >= 4:#cloud
                    self.__weather_img.config(image=self.__night_cloud_img)
                else:#none cloud
                    self.__weather_img.config(image=self.__night_moon_img)
            else:#내림
                if temperature > 3:#rain
                    self.__weather_img.config(image=self.__night_rain_img)
                else:#snow
                    self.__weather_img.config(image=self.__night_snow_img)
        
            
        
        #update!!
        self.__window.update()


    def start_GUI(self):
        try:
            while True:
                self.get_data()
                self.update_GUI()
                time.sleep(0.5)

        except KeyboardInterrupt:
            print('finish')





def main():
    weather_GUI()


if __name__ == "__main__":
    main()
