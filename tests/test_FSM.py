from timeseries.FileStorageManager import FileStorageManager
from pytest import raises
def test_fsm():
	fsm = FileStorageManager()
	fsm.store_tv(123,[1,2,3],[4,5,6])