from nose.tools import *
import godaddy_ddns

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!")