# 7 Million records EDA Exploratory Data Analysis
This project provides an exploratory data analysis (EDA) of a comprehensive dataset with 7 Million records covering traffic accidents across 49 states in the USA. The aim is to derive insightful patterns, understand contributing factors to traffic accidents, and identify areas for potential road safety improvements.
## Dataset Description
The dataset spans from February 2016 to March 2023, containing approximately 7.7 million traffic accident records. It was compiled from multiple APIs providing real-time traffic incident data from various sources, including departments of transportation, law enforcement agencies, traffic cameras, and road network sensors.
## Libraries Used
- `Pandas` for data manipulation and analysis.
- `NumPy` for numerical operations.
- `Matplotlib` and `Seaborn` for data visualization.
- `Folium` for geospatial analysis and creating interactive maps.

## Key Findings

### Geographic Insights
- **Accident Hotspots**: Miami emerges as the city with the highest number of accidents, while California (CA) is the state leading in accident counts.
  
![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/f700e5e3-9360-4174-b01b-0fa35ba04b55)


![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/e928b208-921b-4681-98ed-25b211b00edb)


![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/d9a3c2de-7ffa-46c1-b6d9-ecf8452ab6d0)


![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/418d2cb8-6f2a-47d6-aeca-814cdc681261)



- **New York's Absence**: Despite its high population, New York is conspicuously absent from the list of cities with the highest accidents, attributed to its exclusion from the dataset.
  
- **Low Incident Cities**: A vast majority of cities (over 3,100) reported fewer than 5 accidents per year, suggesting potential underreporting or data collection gaps. It's advisable to consider removing these cities from certain analyses to prevent skewed interpretations.

### Temporal Patterns
- **Commute Hours**: A significant share of accidents occurs between 7-10 AM and 3-7 PM, aligning with typical commuting hours, suggesting that work-related traffic significantly contributes to accident volumes.

![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/4099af2a-e100-4324-9a5c-2be3a8188fec)


- **Weekday Predominance**: Accidents are more prevalent on weekdays compared to weekends, further emphasizing the role of work commuting in traffic accidents.

![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/3bb2cd4f-031e-42d5-babb-c94c3336afd7)


### Data Quality and Reporting
- **Data Inconsistencies**: The analysis unveiled inconsistencies in data collection across years, with Source2 providing more balanced data compared to Source1, indicating potential data gaps in the latter.

![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/eee6609d-be69-44b0-8f39-10b332c3494c)


![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/7d453d0f-22d2-47c4-8618-fa8a7d0ad12a)


- **Weather Conditions**: Contrary to common assumptions, the analysis indicates that weather conditions have a negligible impact on the frequency of accidents, challenging conventional wisdom on weather-related driving risks.

![image](https://github.com/Rithvik97/7-Million-records-EDA-Exploratory-Data-Analysis/assets/145782290/f460a705-713e-4841-9f06-c9709030c08b)


## Conclusion
The exploratory analysis of US traffic accident data highlights critical areas for intervention, notably around high-traffic urban areas and during peak commuting times. It also underscores the necessity for consistent and comprehensive data collection to accurately assess and address the factors contributing to road accidents.
