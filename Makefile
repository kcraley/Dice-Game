PWD:=$(shell pwd)

.PHONY: play
play:
	python $(PWD)/dice.py
