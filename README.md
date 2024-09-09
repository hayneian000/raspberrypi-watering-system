# Automatic Watering System using Raspberry Pi

## Description
This project is an **automatic watering system** powered by a Raspberry Pi. It monitors soil moisture levels and activates a water pump to keep plants hydrated automatically. This is ideal for small gardens, indoor plants, or any system requiring scheduled or monitored watering.

## Table of Contents
1. [Project Features](#project-features)
2. [Components Used](#components-used)
3. [Installation](#installation)

## Project Features
- **Moisture Sensing**: Using a sensor, the system continuously monitors soil moisture levels.
- **Automated Watering**: When the soil is dry, the Raspberry Pi triggers the water pump to water the plants.
- **Customization**: Easily adjust moisture thresholds and watering intervals.

## Components Used
- Raspberry Pi (any model)
- Soil moisture sensor
- Water pump
- Tubing (carries water from the pump to the plant)
- Relay module (to control the pump)
- Wires
- Breadboard
- Power supply (for pump). We used two double A batteries in a battery back.

## Installation

### Hardware Setup
1. Connect the soil moisture sensor to the Raspberry Pi’s GPIO pins.
    -Place the soil moisture sensor deep into the soil to ensure an accurate reading. 
2. Connect the water pump to the relay, and the relay to the Raspberry Pi.
3. Make sure the water pump is submerged in a water container and connected to the plant via tubing.
    -We found it helpful to stick the tube deeper in the pot to help disperse the water.
4. Power the Raspberry Pi and the water pump.

### Software Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automatic-watering-system.git


## Usage
Once the script is running, the Raspberry Pi will monitor the soil moisture in real time.
If the soil is dry, the water pump will be activated automatically to water the plants.
Adjust settings in the config.py file to control the moisture threshold and watering intervals.
The web server allows you to manually turn on the pumps and monitor them. 



