from __future__ import annotations
from smbus2 import SMBus
from .constants import *
from .helpers.delay import delay, delay_us, delay_ms
from .custom_chars import default_custom_chars, replazable_chars, available_chars_ROM_A00

class CursorHandler():
    def __init__(self, lcd: LCD_I2C) -> None:
        self._lcd = lcd
    # Turns the underline cursor on/off ----------------------------------------
    def on(self):
        self._lcd._display_control |= LCD_CURSORON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)
    def off(self):
        self._lcd._display_control &= ~LCD_CURSORON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)
    def toggle(self):
        if self._lcd._display_control | LCD_CURSORON == self._lcd._display_control:
            # It is on, so we turn it off
            self.off()
        else:
            self.on()
    # --------------------------------------------------------------------------
    
    # These commands move the cursor left or right -----------------------------
    def setPos(self, row: int, col: int):
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row > self._lcd._rows-1:
            row = self._lcd._rows-1    # we count rows starting w/0
        self._lcd.command(LCD_SET_DDRAM_ADDR | (col + row_offsets[row]))
    def moveLeft(self):
        self._lcd.command(LCD_CURSORSHIFT | LCD_MOVELEFT)
    def moveRight(self):
        self._lcd.command(LCD_CURSORSHIFT | LCD_MOVERIGHT)
    # --------------------------------------------------------------------------
    
    @property
    def blink(self):
        return BlinkHandler(self._lcd)

class BlinkHandler():
    def __init__(self, lcd: LCD_I2C) -> None:
        self._lcd = lcd
    
    # Turn on and off the blinking cursor --------------------------------------
    def off(self):
        self._lcd._display_control &= ~LCD_BLINKON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)
    
    def on(self):
        self._lcd._display_control |= LCD_BLINKON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)
    
    def toggle(self):
        if self._lcd._display_control | LCD_BLINKON == self._lcd._display_control:
            self.off()
        else:
            self.on()
    # --------------------------------------------------------------------------

class BacklightHandler():
    def __init__(self, lcd: LCD_I2C) -> None:
        self._lcd = lcd
    
    # Turn the (optional) backlight off/on
    def off(self):
        self._lcd._backlight = LCD_NOBACKLIGHT
        self._lcd.expanderWrite(0)

    def on(self):
        self._lcd._backlight = LCD_BACKLIGHT
        self._lcd.expanderWrite(0)

    def set(self, val: bool):
        if val == True:
            self.on()
        else:
            self.off()
    
    def toggle(self):
        if self._lcd._backlight == LCD_BACKLIGHT:
            self.off()
        else:
            self.on()
    
    def flash(self, n: int = 3):
        initial_state = self._lcd._backlight == LCD_BACKLIGHT
        self.off()
        delay_ms(50)
        for i in range(n*2):
            self.toggle()
            delay_ms(50)
        self.set(initial_state)

class DisplayHandler():
    def __init__(self, lcd: LCD_I2C) -> None:
        self._lcd = lcd
    
    def off(self):
        self._lcd._display_control &= ~LCD_DISPLAYON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)

    def on(self):
        self._lcd._display_control |= LCD_DISPLAYON
        self._lcd.command(LCD_DISPLAYCONTROL | self._lcd._display_control)
    
    def toggle(self):
        if self._lcd._display_control | LCD_DISPLAYON == self._lcd._display_control:
            self.off()
        else:
            self.on()
    
    # These commands scroll the display without changing the RAM
    def scrollLeft(self):
        self._lcd.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)
    
    def scrollRight(self):
        self._lcd.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

class LCD_I2C():
    
    def __private_init_to_4bit_mode(self):

        # SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
        # according to datasheet, we need at least 40ms after power rises above 2.7V
        # before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
        delay_ms(50)

        # Now we pull both RS and R/W low to begin commands
        self.expanderWrite(self._backlight) # reset expander and turn backlight off (Bit 8 =1)
        delay_ms(1000)

        # put the LCD into 4 bit mode
        # this is according to the hitachi HD44780 datasheet figure 24, pg 46

        # // we start in 8bit mode, try to set 4 bit mode
        self.write4bits(0x03 << 4) # 0011 0000
        delay_us(4500) # // wait min 4.1ms

        # // second try
        self.write4bits(0x03 << 4) # 0011 0000
        delay_us(4500) # // wait min 4.1ms

        # // third go!
        self.write4bits(0x03 << 4) # 0011 0000
        delay_us(150)

        # // finally, set to 4-bit interface
        self.write4bits(0x02 << 4) # 0010 0000

    def __private_init_other_settings(self):
        # set # lines, font size, etc.
        self.command(LCD_FUNCTIONSET | self._display_function)

        # turn the display on with no cursor or blinking default
        self._display_control = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
        self.display.on()

        # clear it off
        self.clear()

        # Initialize to default text direction (for roman languages)
        self._display_mode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT

        # set the entry mode
        self.command(LCD_ENTRYMODESET | self._display_mode)

        self.home()

    def __init__(self, address: int, cols: int, rows: int, dotsize_5x10: bool = False) -> None:
        
        self._bus = SMBus(1)
        self._address = address
        self._cols = cols
        self._rows = rows
        self._backlight = LCD_NOBACKLIGHT
        self._oled = False

        # self = LowLevel(self._bus, self._address, self._backlight)
        self.load_default_custom_chars()

        self._display_function = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS
        
        if rows > 1:
            self._display_function |= LCD_2LINE
        if dotsize_5x10:
            self._display_function |= LCD_5x10DOTS
        
        self.__private_init_to_4bit_mode()
        self.__private_init_other_settings()

    def load_default_custom_chars(self):
        for i in range(len(default_custom_chars.keys())):
            custom_char = default_custom_chars[list(default_custom_chars.keys())[i]]
            self.createChar(i, custom_char)
    
    def createChar(self, location: int, chars: list[int]):
        # we only have 8 locations 0-7 available to store custom chars
        location &= 0x7
        self.command(LCD_SET_CGRAM_ADDR | (location << 3))
        for i in range(8):
            self.write(chars[i])        

    def write(self, value: int):
        self.send(value, RS_BIT)

    def command(self, value: int):
        self.send(value, 0)
    
    def home(self):
        self.command(LCD_RETURNHOME) # // set cursor position to zero
        delay_us(2000) # // this command takes a long time!

    def clear(self):
        self.command(LCD_CLEARDISPLAY) # clear display, set cursor position to zero
        delay_us(2000)   # this command takes a long time!
        # if (_oled) self.setCursor(0,0)
    
    # Turn the display on/off (quickly) ----------------------------------------
    @property
    def display(self):
        return DisplayHandler(self)

    @property
    def cursor(self):
        return CursorHandler(self)
    
    @property
    def blink(self):
        return BlinkHandler(self)
    
    @property
    def backlight(self):
        return BacklightHandler(self)

    # This will 'left justify' text from the cursor
    def noAutoscroll(self):
        self._display_mode &= ~LCD_ENTRYSHIFTINCREMENT
        self.command(LCD_ENTRYMODESET | self._display_mode)

    # This will 'right justify' text from the cursor
    def autoscroll(self):
        self._display_mode |= LCD_ENTRYSHIFTINCREMENT
        self.command(LCD_ENTRYMODESET | self._display_mode)
    
    def toggleAutoscroll(self):
        if self._display_mode | LCD_ENTRYSHIFTINCREMENT == self._display_mode:
            self.noAutoscroll()
        else:
            self.autoscroll()
    
    # This is for text that flows Left to Right
    def leftToRight(self):
        self._display_mode |= LCD_ENTRYLEFT
        self.command(LCD_ENTRYMODESET | self._display_mode)

    # This is for text that flows Right to Left
    def rightToLeft(self):
        self._display_mode &= ~LCD_ENTRYLEFT
        self.command(LCD_ENTRYMODESET | self._display_mode)
    
    # Low level functions
    def send(self, value: int, mode: int):
        high_nibble: int = value & 0xf0         # 1111 0000
        low_nibble: int = (value<<4) & 0xf0     # 1111 0000
        self.write4bits(high_nibble|mode)
        self.write4bits(low_nibble|mode)

    def write4bits(self, value: int):
        self.expanderWrite(value)
        self.pulseEnable(value)

    def expanderWrite(self, _data: int):                                        
        self._bus.write_byte_data(self._address, 0, _data | self._backlight)

    def pulseEnable(self, _data: int):
        self.expanderWrite(_data | EN_BIT)  # ENABLE_BIT high
        # delay_us(1) # enable pulse must be >450ns

        self.expanderWrite(_data & ~EN_BIT) # ENABLE_BIT low
        # delay_us(50) # commands need > 37us to settle

    def write_text(self, text: str, encoding: str = 'utf-8'):
        for char in text:
            if char in replazable_chars:
                byte = available_chars_ROM_A00.find(char)
                self.write(byte)
            else:
                byte_arr = bytes(char, encoding=encoding)
                for byte in byte_arr:
                    self.write(byte)
    
    def displayAllKeyCodes(self, delay_seconds: int = 3, i_from: int = 0x00, i_to: int = 0xff, row: int = None):
        if row != None:
            i_from = row*16
            i_to = row*16+15
        i: int = i_from
        self.backlight.on()
        while i <= i_to:
            self.clear()
            hex_from = i.to_bytes(1, 'big').hex()
            hex_to = (i+15).to_bytes(1, 'big').hex()
            self.write_text(f"Codes 0x{hex_from}-0x{hex_to}")
            self.cursor.setPos(1, 0)
            for j in range(16):
                if i+j <= i_to:
                    self.write(i+j)
            i+=16
            delay(delay_seconds)


if __name__ == "__main__":
    print("will create instance")
    lcd = LCD_I2C(39, 16, 2)
    delay(1)

    print("Will set backlight on")
    lcd.backlight.on()
    delay(1)

    print("Will make it blink")
    lcd.blink.on()
    delay(3)

    print("Will set cursor to C3R2")
    lcd.cursor.setPos(1, 3)
    delay(1)

    print("Will write text 'hola'")
    lcd.write_text('Hola')

    print("Will print all available characters in ROM")
    lcd.displayAllKeyCodes()
    