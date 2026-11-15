"""
File: temperatureconverter.py

A GUI-based program that converts temperatures between degrees
Fahrenheit and degrees Celsius.
"""

from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """Window with labeled Fahrenheit and Celsius fields and two
    conversion buttons."""

    def __init__(self):
        """Sets up the window and its widgets."""
        EasyFrame.__init__(self, title="Temperature Converter")

        # Row 0: labels
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        # Row 1: entry fields with start-up values
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0)
        self.celsField = self.addFloatField(value=0.0, row=1, column=1)

        # Row 2: command buttons
        self.addButton(text=">>>>", row=2, column=0,
                       command=self.computeCelsius)
        self.addButton(text="<<<<", row=2, column=1,
                       command=self.computeFahrenheit)

    def computeCelsius(self):
        """Converts the Fahrenheit value to Celsius."""
        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32) * 5 / 9
        self.celsField.setNumber(celsius)

    def computeFahrenheit(self):
        """Converts the Celsius value to Fahrenheit."""
        celsius = self.celsField.getNumber()
        fahr = celsius * 9 / 5 + 32
        self.fahrField.setNumber(fahr)


def main():
    """Instantiates and pops up the window."""
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()