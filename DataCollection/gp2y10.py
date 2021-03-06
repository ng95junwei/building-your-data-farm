# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 27
MISO = 22
MOSI = 23
CS   = 24
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def get_value():
	return mcp.read_adc(1)  # I used CH1 for the optical dust sensor 
