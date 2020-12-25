#!/bin/bash
pyuic5 panel.ui -o panel.py
pyrcc5 gui_source.qrc -o gui_source_rc.py