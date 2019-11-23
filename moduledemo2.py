#!/usr/bin/env python

from classdemo import ScientificCalculator,quickAdd

print 'quick Add a+b: %d' %quickAdd(10,20)

ins = ScientificCalculator(5,6)

print '%d' %ins.power()
