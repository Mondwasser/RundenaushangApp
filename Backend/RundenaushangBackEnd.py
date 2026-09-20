import DataSimulator
from Writer.RabenthingPdfWriter import RabenthingPdfWriter
from Writer.SessionSheetWriterBase import SessionSheetWriterBase

# This class is for fast tests of writer classes

data_simulator = DataSimulator.DataSimulator()
session = data_simulator.all_is_well

print(SessionSheetWriterBase.get_all_writers())

target_folder = "D:\\Temp\\Sessions\\"
writer = RabenthingPdfWriter()

writer.write(session, target_folder)